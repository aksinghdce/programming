#!/usr/bin/env python
"""
install load balancer RPMs if the hostname has "*lb*" in it
"""
import socket
import os.path
import re
import subprocess

RPMS = ['haproxy-1.5.2-2.el6.x86_64.rpm', 'keepalived-1.2.13-4.el6.x86_64.rpm']
HOSTNAME_KEY = r"-lb[0-9]+$"

class InstallLoadBalancer:
    """
    installs load balancer rpms idempotently if the hostname has "*lb*"
    """
    def __init__(self, path=""):
        if not path:
            raise ValueError
        self.path = path
        
        
    def check_hostname(self):
        """
        check is the hostname is suitable to install the load balancer rpms
        """
        try:
            self.hostname = socket.gethostname()
            print("hostname:", self.hostname, "path:", self.path)
        except:
            raise Exception("problem with getting hostname")
        
        try:
            match_pattern = re.compile(r"\S+" + HOSTNAME_KEY)
            proceed = match_pattern.match(self.hostname)
            if not proceed:
                raise Exception("its not a load balancer machine")
            return True
        except:
            raise Exception("not a load balancer machine")
        
        return False
        
    def check_rpms(self):
        """
        check is rpms exist and if they are already installed.
        If already installed, then nothing needs to be done.
        """
        try:
            self.rpms = [self.path + '/' + rpm for rpm in RPMS]
            for files in self.rpms:
                if not os.path.exists(files):
                    raise IOError
            return True
        except:
            raise Exception("RPMs do not exist")
        
        return False
        
    def install_rpms(self):
        """
        install rpms
        """
        if self.check_hostname() and self.check_rpms():
            for name in RPMS:
                try:
                    subprocess.check_call(["rpm", "-q", name[:-4]])
                except:
                    print(name, "is not installed, instlling now")
                    try:
                        subprocess.check_call(["rpm", "-ivh", self.path + "/" + name])
                    except:
                        print("rpm:", name, " could not be installed")
            print("rpms installed")

if __name__ == '__main__':
    print("hello world")
    installer = InstallLoadBalancer(path = "/var/opt/dsp/images/lb")
    installer.install_rpms()
# Practice of Python Skills with YouTube Video Creation Pipeline:

Reade my gists here - https://gist.github.com/aksinghdce

# Fundamental Concepts for Quick Look-Up

## geeksforgeeks.org | Python Tricks for Competitive Programming

1. The Counter Package
Analyses a list/string and provides top 'n' most frequent items with the frequency.
`from collections import Counter
arr = [1,3,4,1,2,1,1,3,4,3,5,1,2,5,3,4,5]
counter = Counter(arr)
top_three = counter.most_common(3)
print(top_three)
`
2. heapq package
`import heapq
print(heapq.nlargest(3, arr))
print(heapq.nsmallest(4, arr))
`

3. zipping dictionaries
`stocks = {
    'Goog' : 520.54,
    'FB' : 39.28,
    'AMZN' : 306.21,
    'yhoo' : 39.28,
    'APPL' : 99.76
    }
zipped_1 = zip(stocks.values(), stocks.keys())
print(sorted(zipped_1)) # sorted according to values
zipped_2 = zip(stocks.keys(), stocks.values())
print(sorted(zipped_2)) # sorted according to keys

4. mapped functions
apply first argument, which is a function that takes one argument of type of data the list in the second argument has, to each element of the list and resurn the result in the form of list of outputs.

# 50 Questions
# 128 Questions
# Leetcode, top 100 questions 
	11. Container With Most Water
	You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

	`class Solution:
	    def maxArea(self, height: List[int]) -> int:
		from collections import defaultdict
		areas = defaultdict(int)
		for i in range(len(height)):
		    for j in range(i+1, len(height)):
			areas[(i,j)] = min(height[i], height[j]) * (j - i)
		sorted_by_area = sorted(zip(areas.values(), areas.keys()))
		return sorted_by_area[-1][0]`

Time limit exceeded for large input. How to fix it?
I am sorting. Can I just use a heap because all I care about it the max area.

	`class Solution:
	    def maxArea(self, height: List[int]) -> int:
		max_area = 0
		for i in range(len(height)):
		    for j in range(i+1, len(height)):
			area = min(height[i], height[j]) * (j - i)
			if area > max_area:
			    max_area = area
		return max_area`

with this the earlier input was solved within time, so there's an improvement. How can I make it better? I can use memoization.

	`class Solution:
	    def maxArea(self, height: List[int]) -> int:
		from collections import defaultdict
		areas = defaultdict(int)
		max_area = 0
		for i in range(len(height)):
		    for j in range(i+1, len(height)):
			if 0 == areas[tuple(sorted([i,j]))]:
			    areas[tuple(sorted([i,j]))] = min(height[i], height[j]) * (j - i)
			    max_area = max(areas[tuple(sorted([i,j]))], max_area)
		return max_area`

memoization didn't help either because it's still the brute force approach.
We need to leverage the fact that priority is to look at highese distance first.Second, we need to move forward from left towards right if doing so increases the minimum height of the pair.

	`class Solution:
	    def maxArea(self, height: List[int]) -> int:
		from collections import defaultdict
		i = 0
		j = len(height) - 1
		max_area = 0
		while j > i:
		    width = j - i
		    max_area = max(max_area, min(height[j], height[i])*width)
		    if height[i] <= height[j]:
			i += 1
		    else:
			j -= 1
		return max_area`



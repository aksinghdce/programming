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

# DailyCodingProblem
My coding for problem issued by many entreprise while job's interview.
My goal is to familiar with Python and brainstorm for coding

## Problem 0:
In the first case, we can climb to staircase by one or two steps with our choise
We need to count all possible ways
I found the rule:
	N = 1 : [1]
	N = 2 : [1,1], [2]
	N = 3 : [1,1,1], [1,2], [2,1]
	N = 4 : [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
source: dailycodingproblem.com/?ref=csdojo

## Problem 1:
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

## Problem 2:
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

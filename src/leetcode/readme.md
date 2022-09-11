**239. Sliding Window Maximum**


Problem:
You are given an array of integers nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.



Scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.

1.At each i, keep "promising" elements, which are potentially max number in window `[i-(k-1),i]` or any subsequent window. This means
If an element in the deque and it is out of i-(k-1), discard them. We just need to poll from the head, 
as we are using a deque and elements are ordered as the sequence in the array

2.Now only those elements within `[i-(k-1),i]` are in the deque. We then discard elements smaller than `a[i]` from the tail. 
This is because if `a[x] <a[i]` and x<i, then `a[x]` has no chance to be the "max" in `[i-(k-1),i]`, 
or any other subsequent window: `a[i]` would always be a better candidate.

3.As a result elements in the deque are ordered in both sequence in array and their value. 
At each step the head of the deque is the max element in `[i-(k-1),i]`.



**76. Minimum Window Substring**

Problem :
Given two strings s and t of lengths `m` and `n` respectively, return the minimum window substring of `s`
such that every character in `t` (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".


We can use a simple sliding window approach to solve this problem.

We keep expanding the window by moving the right pointer and stores the characters those are present in `t` in the deque. 
When the window has all the desired characters, we contract (if possible) and save the smallest window till now.

Time Complexity: O(|S| + |T|)

Space Complexity: O(|S| + |T|)

45. Jump Game II

Problem:
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.


The main idea is based on greedy. Let's say the range of the current jump is `[curBegin, curEnd]`, 
curFarthest is the farthest point that all points in `[curBegin, curEnd]` can reach. 
Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, 
then keep the above steps.

Time Complexity: O(N)


**2135. Count Words Obtained After Adding a Letter**

Problem:
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.



Solution:

Idea here is calculate bitmask of each word of startWords and store them in a unordered_set / hashset for that.
Doing this we can take care of Rearrage operation (if any) as given in question.

Now, we iterate over each targetWords. Again for this first we need to calculate bitmask to take care of rearrangement.

For each word we skip one character say and then check if that resultant word is present in our startSet or not.
If not, then we skip next character and again check
If yes, then we increment count and break.
Since we have found a startWord in set ,
which can be converted to current targetWord.

Time Complexity: O(Mn) + O(Nn)
M = # of startWords
m = Avg length of startWords
N = # of targetWords
m = Avg length of targetWords




**91. Decode Ways**

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").



Solution:
For a character s[i], we have 2 ways to decode:
Single digit: Require s[i] != '0' (decoded to 1..9)
Two digits: Require i + 1 < len(s) and (s[i] == 1 (decoded to 10..19) or s[i] == 2 and s[i+1] <= '6') (decoded to 20..26).

Time Complexity: O(N)
Space Complexity: O(N)


**134. Gas Station**

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

**Solution**

Start the trip from beginning and continue until the car runs out of gas
to go to the next station. Then, start the trip again at the next station.


We are skipping all the other stations between the beginning and 
the last station we reached because if `ith` station is the first one we cannot reach 
from the starting point or `0th` station, then we cannot also reach `ith` station starting from any
station between the `0th` to `(i-1)th` station. We will be at some kind of deficit comparing our 
fuel accumulation to our fuel consumption. So, this means we can start trying 
at the `ith` station. So, hopefully now you understand how this O(N) solution will takes place.


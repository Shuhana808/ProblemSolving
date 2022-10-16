##### 11. Container With Most Water

**Problem:**

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of 
the ith line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Solution:**

The intuition is that the area formed between the lines will 
always be limited by the height of the shorter line. 
Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of 
the array constituting the length of the lines. Futher, we maintain 
a variable `maxarea` to store the maximum area obtained 
till now. At every step, we find out the area formed between them, 
update `maxarea` and move the pointer pointing to the shorter line towards the other end by one step.

Time complexity: O(n)

Space complexity: O(1)

##### 91. Decode Ways

**Problem:**

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

**Solution:**
Let dp[ i ] = the number of ways to parse the string s[0: i-1]
    dp[0] = 1
    dp[i] = dp[i-1] consider s[i-1] represents a char 
    dp[i] += dp[i-2] consider s[i-2:i-1] can be grouped to
                     represent a char

Time complexity: O(n)

Space complexity: O(n), can be reduced to o(1) if just 
last two dp values are stored


##### 802. Find Eventual Safe States


**Problem:**
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
The graph is represented by a 0-indexed 2D integer array graph where graph[i] is 
an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting 
from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



**Solution:**

Let, value of color represents three states:

0:have not been visited

1:unsafe

2:safe

For DFS, we need to do some optimization. When we travel a path,we 
mark the node with 1 which represents having been visited,and when 
we encounter a node which results in a cycle,we return false,all node 
in the path stays 1 and it represents unsafe.And in the following traveling,
whenever we encounter a node which points to a node marked with 1,we know 
it will results in a cycle,so we can stop traveling.On the contrary,when a node
is safe,we can mark it with 1 and whenever we encounter a safe node,we know it
will not results in a cycle.


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

**Another Approach:**
We can iterate over all indices maintaining the furthest reachable position from current index - maxReachable and currently furthest reached position - lastJumpedPos. Everytime we will try to update lastJumpedPos to furthest possible reachable index - maxReachable.

Updating the lastJumpedPos separately from maxReachable allows us to maintain track of minimum jumps required. Each time lastJumpedPos is updated, jumps will also be updated and store the minimum jumps required to reach lastJumpedPos (On the contrary, updating jumps with maxReachable won't give the optimal (minimum possible) value of jumps required).

We will just return it as soon as lastJumpedPos reaches(or exceeds) last index.

We can try to understand the steps in code below as analogous to those in BFS as -

maxReachable = max(maxReachable, i + nums[i]) : Updating the range of next level. Similar to queue.push(node) step of BFS but here we are only greedily storing the max reachable index on next level.

i == lastJumpedPos : When it becomes true, current level iteration has been completed.

lastJumpedPos = maxReachable : Set range till which we need to iterate the next level

jumps++ : Move on to the next level.

return jumps : The final answer will be number of levels in BFS traversal.

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


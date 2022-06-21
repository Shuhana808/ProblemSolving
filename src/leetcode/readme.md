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

Time Complexity: O(|S| + |T|)O(∣S∣+∣T∣) 

Space Complexity: O(|S| + |T|)O(∣S∣+∣T∣)
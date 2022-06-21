from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Dictionary which keeps a count of all the unique characters in t.
        target_count = {}

        # Dictionary which keeps a count of all the unique characters in the current window.
        current_window_count = {}

        # Stores only the character in s that is present in t.
        dq = deque([])

        min_window = 1000000
        start_ind = -1
        end_ind = -1
        for c in t:
            if c in target_count:
                target_count[c] = target_count[c] + 1
            else:
                target_count[c] = 1

        total_distinct_chars = len(target_count.keys())
        window_len = 0

        for i in range(0, len(s)):

            if s[i] in target_count:

                dq.append((s[i], i))

                c = s[i]
                if c in current_window_count:
                    current_window_count[c] = (current_window_count[c][0] + 1, current_window_count[c][1])
                else:
                    current_window_count[c] = (1, 0)

                if current_window_count[c][1] == 0 and current_window_count[c][0] == target_count[c]:
                    current_window_count[c] = (current_window_count[c][0], 1)
                    window_len = window_len + 1

            while window_len == total_distinct_chars:

                start = dq[0][1]
                end = dq[-1][1]

                if end - start < min_window:
                    min_window = end - start
                    start_ind = start
                    end_ind = end

                char, ind = dq.popleft()
                current_window_count[char] = (current_window_count[char][0] - 1, current_window_count[char][1])
                if current_window_count[char][0] < target_count[char]:
                    current_window_count[char] = (current_window_count[char][0], 0)
                    window_len = window_len - 1

        return s[start_ind:end_ind + 1]





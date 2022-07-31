class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        fruit_types = {}

        start = 0
        end = 0

        collected = 0
        max_collected = 0
        fruit_type_count = 0

        for i in range(0, n):
            fruit = fruits[i]

            if fruit in fruit_types:

                fruit_types[fruit] += 1

                if fruit_types[fruit] == 1:
                    fruit_type_count += 1
            else:
                fruit_types[fruit] = 1
                fruit_type_count += 1

            # print(max_collected)
            while fruit_type_count == 3:

                if i - start > max_collected:
                    max_collected = i - start

                fruit_types[fruits[start]] -= 1

                if fruit_types[fruits[start]] == 0:
                    fruit_type_count -= 1

                start += 1

        if fruit_type_count < 3 and n - start > max_collected:
            max_collected = n - start

        return max_collected

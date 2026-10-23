from os import popen


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        return self.on_single_stack(heights)

    def on2_brute_force(self, heights: list[int]) -> int:
        max_size = 0
        for i in range(0, len(heights)):
            left = i
            for index1 in range(i - 1, -1, -1):
                if heights[index1] < heights[i]:
                    break
                left = index1

            right = i
            for index2 in range(i + 1, len(heights), 1):
                if heights[index2] < heights[i]:
                    break
                right = index2

            width = right - left + 1
            height = heights[i]
            max_size = max(height * width, max_size)

        return max_size

    def on_single_stack(self, heights: list[int]) -> int:
        max_size = 0
        heights.append(0)
        s = []
        for i in range(len(heights)):
            if len(s) == 0 or heights[s[-1]] <= heights[i]:
                s.append(i)
                continue

            while len(s) > 0 and heights[s[-1]] > heights[i]:
                top = s.pop()
                left_index = s[-1] if s else -1
                right_index = i
                width = right_index - left_index - 1
                height = heights[top]
                max_size = max(max_size, width * height)
            s.append(i)
        return max_size

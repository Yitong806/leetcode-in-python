class Solution:
    def trap(self, height: list[int]) -> int:
        return self.on_dual_pointer(height)

    def on2_brute_force(self, height: list[int]) -> int:
        # Time: 00:28:00.48
        # Date: 2026.10.12
        storage = 0
        for i in range(1, len(height) - 1):
            left = i - 1
            right = i + 1
            left_local_maximum, right_local_maximum = height[left], height[right]
            while left >= 0:
                left_local_maximum = max(left_local_maximum, height[left])
                left -= 1
            while right <= len(height) - 1:
                right_local_maximum = max(right_local_maximum, height[right])
                right += 1

            min_height = min(left_local_maximum, right_local_maximum)

            possible_storage = max(min_height - height[i], 0)

            storage += possible_storage

        return storage

    def on_left_right_max(self, height: list[int]) -> int:
        # Time: 00:39:26.64-00:28:00.48=00:11:26.16
        # Date: 2026.10.12
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        for i in range(len(height)):
            left_max[i] = max(height[i], left_max[i - 1] if i > 0 else 0)
        for j in range(len(height) - 1, -1, -1):
            right_max[j] = max(height[j], right_max[j + 1] if j < len(height) - 1 else 0)

        storage = 0
        for i in range(0, len(height)):
            min_height = min(left_max[i], right_max[i])
            possible_storage = max(min_height - height[i], 0)
            storage += possible_storage

        return storage

    def on_dual_pointer(self, height: list[int]) -> int:
        # Time: 01:13:22.10-00:39:26.64=00:33:55.46
        # Date: 2026.10.12
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        storage = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                storage += left_max - height[left]
                left += 1
            else:
                storage += right_max - height[right]
                right -= 1
        return storage
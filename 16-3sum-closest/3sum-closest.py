class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for i in range(0, len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum
                
                if currentSum == target:
                    return currentSum
                elif currentSum < target:
                    left += 1
                else:
                    right -= 1

        return closestSum
        
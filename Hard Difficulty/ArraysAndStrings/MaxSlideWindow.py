from collections import deque
def maxSlidingWindow( nums, k):
    windowQueue = deque()
    maxSlide = []
    for i in range(len(nums)):
        if windowQueue and windowQueue[0] == (i-k):
            windowQueue.popleft()
        while windowQueue and nums[i] > nums[windowQueue[-1]]:
            windowQueue.pop()
        windowQueue.append(i)

        if i >= k-1:
            maxSlide.append(nums[windowQueue[0]])

    return maxSlide


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
import heapq

class Solution:
    def filterFunc(self, x, w):
        if x > w:
            return False
        else:
            return True    

    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort()
        i = 0
        pq = []
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                heapq.heappush(pq, -arr[i][1])
                i += 1
            if pq:
                w -= heapq.heappop(pq)
            else:
                break
        return w
            
print(Solution().findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
print(Solution().findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
print(Solution().findMaximizedCapital(1, 2, [1,2,3], [1,1,2]))
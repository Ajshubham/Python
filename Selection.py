class Solution:
    def SelectionSort(self, arr : list[int]) -> list[int]:
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

# n = int(input())
arr = list(map(int, input().split()))
sort = Solution()
print(sort.SelectionSort(arr))
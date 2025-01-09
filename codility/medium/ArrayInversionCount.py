# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
sys.setrecursionlimit(10**6)

def solution(A):
    def merge(left, right):
        count = 0
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
                count += len(left)-i
        
        result.extend(left[i:])
        result.extend(right[j:])

        return [result, count]


    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = merge_sort(arr[:mid])
        right, right_count = merge_sort(arr[mid:])
        total, total_count = merge(left, right)

        return total, left_count+right_count+total_count

    _, ans = merge_sort(A)

    return ans if ans <= 1000000000 else -1

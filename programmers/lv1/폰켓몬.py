def solution(nums):
    pon = set()
    for num in nums:
        pon.add(num)
        
    return min(len(pon), len(nums)//2)
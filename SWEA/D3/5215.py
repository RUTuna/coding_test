import sys
sys.stdin = open("5215_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def DFS(score, remainCalrory, foodInfo):
    if remainCalrory == 0 or len(foodInfo) == 0:
        return score
    
    childrend = []
    for i, food in enumerate(foodInfo):
        if remainCalrory - food[1] >= 0:
            tmp = foodInfo[i:]
            tmp.pop(0)
            childrend.append(DFS(score+food[0], remainCalrory-food[1], tmp))
    
    return max(childrend) if len(childrend) else score
    
    
for test_case in range(1, T + 1):
    # DFS 방식
    foodNum, calrory = map(int, input().split())
    foodInfo = []
    
    for i in range(foodNum):
        foodInfo.append(list(map(int, input().split())))

    ans = DFS(0, calrory, foodInfo)

    print('#'+str(test_case), ans)
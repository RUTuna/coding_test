import sys
sys.stdin = open("1208_input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())
    boxes = [ int(x) for x in input().split() ]
    
    while dump > 0:
        maxBoxIndex = boxes.index(max(boxes))
        minBoxIndex = boxes.index(min(boxes))
        
        if boxes[maxBoxIndex] - boxes[minBoxIndex] < 2:
            break;
        
        dump -= 1
        boxes[maxBoxIndex] -= 1
        boxes[minBoxIndex] += 1
        
    
    maxBoxIndex = boxes.index(max(boxes))
    minBoxIndex = boxes.index(min(boxes))
    print('#'+str(test_case), boxes[maxBoxIndex] - boxes[minBoxIndex])

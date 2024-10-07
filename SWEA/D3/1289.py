import sys
sys.stdin = open("1289_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    memory = input()
    count = 0
    now = '0'
    for b in memory:
        if b != now:
            count += 1
            now = b
            
    print('#'+str(test_case),count)
import sys
sys.stdin = open('1218_input.txt','r')

T = 10

for test_case in range(1,T + 1):
    length = int(input())
    string = input()
    
    isPossible = True
    couple = {')':'(', ']':'[', '}':'{', '>':'<'}
    stack = []
    
    for s in string:
        if s == '(' or s == '[' or s == '{' or s == '<' :
            stack.append(s)
        else:
            top = stack.pop()
            if top != couple[s]:
                isPossible = False
                break
    
    print('#'+str(test_case), int(isPossible))
            
    
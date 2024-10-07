# 기존 코드

"""
import sys

L, C = map(int, sys.stdin.readline().split())
string = sys.stdin.readline().split()
string.sort()

def count_Vowels(path):
    count = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        if i in path:
            count += 1
            
    return count     

def DFS(depth, path):
    if len(path) == L:
        num_vow = count_Vowels(path)
        if num_vow >= 1 and L-num_vow >= 2:
            print(path)
            return
        
    if depth == C:
        return
    
    DFS(depth+1, path+string[depth])
    DFS(depth+1, path)

DFS(0, '')
"""

# 개선 코드

import sys

L, C = map(int, sys.stdin.readline().split())
string = sys.stdin.readline().split()
string.sort()

vowels = set('aeiou')

def DFS(depth, path, num_vow, num_con):
    if len(path) == L:
        if num_vow >= 1 and num_con >= 2:
            print(''.join(path))
        return
    
    if depth == C:
        return

    if string[depth] in vowels:
        DFS(depth + 1, path + [string[depth]], num_vow + 1, num_con)
    else:
        DFS(depth + 1, path + [string[depth]], num_vow, num_con + 1)

    DFS(depth + 1, path, num_vow, num_con)

DFS(0, [], 0, 0)
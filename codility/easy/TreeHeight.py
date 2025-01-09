# from extratypes import Tree  # library with types used in the task

from dataclasses import dataclass, field

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None
    
def solution(T):
    if not T:
        return -1
    answer, depth = 0, 0

    def DFS(now):
        nonlocal answer, depth
        answer = max(answer, depth)

        if now.l:
            depth += 1
            DFS(now.l)
            depth -= 1
        if now.r:
            depth += 1
            DFS(now.r)
            depth -= 1
    DFS(T)

    return answer


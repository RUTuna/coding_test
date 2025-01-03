from collections import deque

def solution(begin, target, words):
    words = [begin] + words
    maps = [[0] * len(words) for _ in range(len(words))]
    start, end = 0, 0
    
    for index, word in enumerate(words):
        if word == target:
            end = index
        
        for cIndex, cWord in enumerate(words):
            count = 0
            for i in range(len(word)):
                if not word[i] == cWord[i]:
                    count += 1
                if count > 1:
                    break
                    
            maps[index][cIndex] = 0 if count > 1 else 1
            
    queue = deque([(0, 0)])
    isVisited = [False] * len(words)

    while queue:
        now, depth = queue.popleft()
        if isVisited[now]:
            continue
        isVisited[now] = True
        
        if now == end:
            return depth
        
        for nxt in range(len(words)):
            if maps[now][nxt] and not isVisited[nxt]:
                queue.append((nxt, depth+1))
    
    return 0
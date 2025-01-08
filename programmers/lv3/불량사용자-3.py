import re

def solution(user_id, banned_id):
    candidate = []
    
    for i, banned in enumerate(banned_id):
        candidateList = []
        pattern = re.compile(banned.replace('*','.'))
        for user in user_id:
            if re.fullmatch(pattern, user):
                candidateList.append(user)
        candidate.append(candidateList)
        
    answer = set()
    final = []
    
    def DFS(depth):
        if depth == len(banned_id):
            answer.add(tuple(sorted(final)))
            return
        
        for cand in candidate[depth]:
            if not cand in final:
                final.append(cand)
                DFS(depth+1)
                final.pop()
    
    DFS(0)    
    return len(answer)
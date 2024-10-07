import sys
from itertools import combinations

answer = []
game = list(combinations(range(6), 2))
games_res = []
isAble = False

def match(round):
    global isAble
    
    if round == 15:
        for one in games_res:
            if sum(one) != 0:
                isAble = False
                return
            
        isAble = True
        return
    
    team_a, team_b = game[round]
    for a, b in [(0,2), (1,1), (2,0)]: # a승리, 무승부, b승리
        if games_res[team_a][a] > 0 and games_res[team_b][b] > 0:
            games_res[team_a][a] -= 1
            games_res[team_b][b] -= 1
            match(round+1)
            games_res[team_a][a] += 1
            games_res[team_b][b] += 1
    

for _ in range(4):
    games_res = list(map(int, sys.stdin.readline().split()))
    games_res = [ games_res[i:i+3] for i in range(0, 16, 3)]
    isAble = False
    match(0)
    answer.append(1 if isAble else 0)
    
print(*answer)
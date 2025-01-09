import sys

def solution(alp, cop, problems):
    dp = [[sys.maxsize]*152 for _ in range(152)]
    dp[alp][cop] = 0
    target_alp, target_cop = alp, cop
    
    for alp_req, cop_req, _, _, _ in problems:
        target_alp = max(target_alp, alp_req)
        target_cop = max(target_cop, cop_req)

    for a in range(alp, target_alp+1):
        for c in range(cop, target_cop+1):
            if dp[a][c] == sys.maxsize:
                continue
                
            dp[a+1][c] = min(dp[a+1][c], dp[a][c]+1)
            dp[a][c+1] = min(dp[a][c+1], dp[a][c]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= a and cop_req <= c:
                    nxt_alp, nxt_cop = min(target_alp, a+alp_rwd), min(target_cop, c+cop_rwd)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[a][c]+cost)
                
    return dp[target_alp][target_cop]
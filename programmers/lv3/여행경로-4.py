from collections import defaultdict
import heapq

def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list)
    for start, end in tickets:
        heapq.heappush(graph[start], end)  # 우선순위 큐에 삽입 (알파벳 순서)

    route = []

    def dfs(airport):
        while graph[airport]:
            next_airport = heapq.heappop(graph[airport])  # 알파벳 순서로 방문
            dfs(next_airport)
        route.append(airport)

    dfs("ICN")
    return route[::-1]  # 경로를 역순으로 반환
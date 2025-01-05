def solution(n, costs):
    # 간선들을 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    # 부모 노드 배열 초기화
    parent = list(range(n))

    # 부모 노드를 찾는 함수
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    # 두 노드를 합치는 함수
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    total_cost = 0
    for s, d, c in costs:
        # 두 노드가 같은 그룹에 있지 않으면 선택
        if find(s) != find(d):
            union(s, d)
            total_cost += c

    return total_cost
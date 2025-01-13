function solution(sales, links) {
  const MAX_NUM = Number.MAX_SAFE_INTEGER;
  const graph = {};
  for (let [a, b] of links) {
    if (Object.hasOwn(graph, a - 1)) graph[a - 1].push(b - 1);
    else graph[a - 1] = [b - 1];
  }

  const dp = Array.from({ length: sales.length }, () => Array(2).fill(0));

  // 팀장을 겸직하거나 두개의 팀의 팀원이 될 순 없으니 중복 확인 안해도 됨
  function DFS(now) {
    dp[now][1] = sales[now];
    if (!Object.hasOwn(graph, now)) return dp[now]; // only 팀원

    let extra_cost = MAX_NUM;
    for (let child of graph[now]) {
      let child_result = DFS(child);
      dp[now][1] += Math.min(child_result[0], child_result[1]); // 참석 하면 자식 중 작은 값
      dp[now][0] += Math.min(child_result[0], child_result[1]);
      // 자식 중 아무도 참석 안했을 경우를 위해 자식이 참석했을 때 코스트 차가 젤 작은거 저장
      extra_cost = Math.min(extra_cost, child_result[1] - child_result[0]);
    }

    // extra_cost 가 0보다 작으면 적어도 한명은 참석함
    if (extra_cost > 0) dp[now][0] += extra_cost;

    return dp[now];
  }

  return Math.min(...DFS(0));
}

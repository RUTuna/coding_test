class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  pop() {
    if (this.size() === 0) throw Error("Empty Heap");
    if (this.size() === 1) return this.heap.pop();

    let top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return top;
  }

  bubbleUp() {
    let nowIdx = this.size() - 1;
    let parentIdx = Math.floor((nowIdx - 1) / 2);

    while (this.heap[parentIdx] && this.heap[parentIdx][1] > this.heap[nowIdx][1]) {
      this.swap(nowIdx, parentIdx);
      nowIdx = parentIdx;
      parentIdx = Math.floor((nowIdx - 1) / 2);
    }
  }

  bubbleDown() {
    let nowIdx = 0;
    let leftIdx = nowIdx * 2 + 1;
    let rightIdx = nowIdx * 2 + 2;

    while ((this.heap[leftIdx] && this.heap[leftIdx][1] < this.heap[nowIdx][1]) || (this.heap[rightIdx] && this.heap[rightIdx][1] < this.heap[nowIdx][1])) {
      let swapIdx = this.heap[rightIdx] && this.heap[leftIdx][1] > this.heap[rightIdx][1] ? rightIdx : leftIdx;
      this.swap(nowIdx, swapIdx);
      nowIdx = swapIdx;
      leftIdx = nowIdx * 2 + 1;
      rightIdx = nowIdx * 2 + 2;
    }
  }
}

function solution(n, paths, gates, summits) {
  let summitsSet = new Set(summits);
  let visited = Array(n + 1).fill(false);
  let maps = Array.from({ length: n + 1 }, () => []);
  let cost = Array(n + 1).fill(Number.MAX_SAFE_INTEGER);
  let heap = new MinHeap();

  for (let [i, j, w] of paths) {
    maps[i].push([j, w]);
    maps[j].push([i, w]);
  }

  for (let g of gates) {
    heap.add([g, 0]);
    cost[g] = 0;
  }

  while (heap.size() > 0) {
    let [now, intensity] = heap.pop();
    if (visited[now]) continue;
    if (summitsSet.has(now) || cost[now] < intensity) continue;

    visited[now] = true;
    for (let [nxt, nxtIntensity] of maps[now]) {
      if (nxtIntensity && !visited[nxt]) {
        let newIntensity = Math.max(intensity, nxtIntensity);
        if (cost[nxt] > newIntensity) {
          cost[nxt] = newIntensity;
          heap.add([Number(nxt), newIntensity]);
        }
      }
    }
  }

  let answer = [n + 1, 10000001];
  for (let s of summits.sort((a, b) => a - b)) {
    if (answer[1] > cost[s]) answer = [s, cost[s]];
  }

  return answer;
}

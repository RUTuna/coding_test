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

    while (this.heap[parentIdx] && this.heap[parentIdx] > this.heap[nowIdx]) {
      this.swap(nowIdx, parentIdx);
      nowIdx = parentIdx;
      parentIdx = Math.floor((nowIdx - 1) / 2);
    }
  }

  bubbleDown() {
    let nowIdx = 0;
    let leftIdx = nowIdx * 2 + 1;
    let rightIdx = nowIdx * 2 + 2;

    while ((this.heap[leftIdx] && this.heap[leftIdx] < this.heap[nowIdx]) || (this.heap[rightIdx] && this.heap[rightIdx] < this.heap[nowIdx])) {
      let swapIdx = this.heap[rightIdx] && this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
      this.swap(nowIdx, swapIdx);
      nowIdx = swapIdx;
      leftIdx = nowIdx * 2 + 1;
      rightIdx = nowIdx * 2 + 2;
    }
  }
}

let heap = new MinHeap();
heap.add(1);
heap.add(4);
heap.add(5);
heap.add(2);

console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());

import heapq

def solution(scoville, K):
    # 최소 힙
    # 최소 힙에 데이터 삽입
    # 앞의 값 확인 -> k 보다 크면 종료, 안 크면 밑에 과정 진행
    # 앞에 두개 꺼내서, 계산 후 삽입 -> 여기까지 과정 += 1

    count = 0
    scovilleHeap = []

    for i in scoville:
        heapq.heappush(scovilleHeap, i)

    while len(scovilleHeap) > 1 and scovilleHeap[0] < K:
        score = heapq.heappop(scovilleHeap) + heapq.heappop(scovilleHeap) * 2
        heapq.heappush(scovilleHeap, score)
        count += 1

    if scovilleHeap[0] >= K:
        return count
    else:
        return -1
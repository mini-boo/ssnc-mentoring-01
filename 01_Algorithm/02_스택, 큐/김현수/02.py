import math

def solution(progresses, speeds):
    answer = []

    # 1. 100-progresses
    transformed = [100 - x for x in progresses]

    # 2. 나누기
    remain = []
    for i in range(len(transformed)):
        if speeds[i] == 0:
            remain.append(None)
        else:
            val = transformed[i] / speeds[i]
            remain.append(math.ceil(val))

    #3. 기능 배포 날짜 계산하기
    # 1) 현재 작업(day)가 가장 오래 걸리는 작업(max_day)보다 빨리 완료되는 경우 +1
    # 2) max_day보다 오래 걸리는 경우, 정답 배열에 추가하고 현재 작업을 max_day로 지정+카운트를 초기화
    max_day = remain[0]
    count = 1

    for day in remain[1:]:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1

    answer.append(count)

    return answer
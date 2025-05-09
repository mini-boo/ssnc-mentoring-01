def solution(participant, completion):
    answer = ''

    a ={}

    # 마라톤 참여 선수 목록
    for i in range(len(participant)):
        a[participant[i]] = a.get(participant[i], 0) + 1

    # 마라톤 완주 선수 제거
    for i in range(len(completion)):
        a[completion[i]] -= 1
        if a[completion[i]] == 0:
            del a[completion[i]]

    # 남은 선수 출력
    for name in a:
        answer = name

    return answer
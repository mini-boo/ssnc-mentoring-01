def solution(nums):
    answer = 0

    a = {}

    # 폰켓몬 종류 별 개수
    for i in range(len(nums)):
        a[nums[i]] = a.get(nums[i], 0) + 1

    if(len(nums)/2 < len(a)):
        answer = len(nums)/2
    else:
        answer = len(a)

    return answer
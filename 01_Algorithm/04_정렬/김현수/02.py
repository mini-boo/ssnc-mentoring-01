def solution(numbers):
    answer = ''

    #문자열로 변환
    num = list(map(str, numbers))

    #numbers의 원소는 1의 자리에서 1000자리까지 가능
    # x*3은 숫자를 세 번 정렬함
    # ex) [3, 30, 34] => 333, 303030, 343434
    # 자리마다 숫자 비교: 첫번째 자리 [3, 3, 3] / 두 번째 자리 [3,0,4] -> 34, 3, 30이 큼
    #reverse로 큰 수부터 정렬
    s = sorted(num,key=lambda x: x*3,reverse=True)

    #문자를 공백 없이 붙이기
    answer += ''.join(s)

    #정수로 변환
    return str(int(answer))
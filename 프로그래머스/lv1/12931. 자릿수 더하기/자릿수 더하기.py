def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    num = str(n)
    for i in num :
        answer += int(i)

    return answer
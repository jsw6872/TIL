def solution(n):
    str_dict = {0:'수', 1: '박'}
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += str_dict[0]
        else:
            answer += str_dict[1]
    return answer
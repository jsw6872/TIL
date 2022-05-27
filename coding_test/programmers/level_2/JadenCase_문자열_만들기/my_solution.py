def solution(s):
    s_list = s.split(' ')
    answer = ''
    for i in s_list:
        answer += i.capitalize() + ' '
    return answer[:-1]
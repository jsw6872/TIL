def solution(s):
    l = s.split()
    l = [int(i) for i in l]
    l.sort()
    answer = f'{l[0]} {l[-1]}'
    return answer
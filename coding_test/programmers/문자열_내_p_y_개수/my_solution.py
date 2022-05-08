def solution(s):
    p_c = 0
    y_c = 0
    s = s.lower()
    for i in s:
        if i == 'p':
            p_c += 1
        elif i == 'y':
            y_c += 1
    return True if p_c == y_c else False
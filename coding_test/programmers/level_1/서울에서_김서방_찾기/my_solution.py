def solution(seoul):
    for idx, item in enumerate(seoul):
        if item == 'Kim':
            return f'김서방은 {idx}에 있다'
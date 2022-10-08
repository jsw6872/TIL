def solution(quiz):
    answer = []
    for problem in quiz:        
        if eval(problem.split('=')[0]) == eval(problem.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
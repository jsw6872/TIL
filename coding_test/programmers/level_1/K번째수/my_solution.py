def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new_arr = sorted(array[commands[i][0]-1:commands[i][1]])
        num = new_arr[commands[i][2]-1]
        answer.append(num)
    return answer
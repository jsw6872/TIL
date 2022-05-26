def solution(absolutes, signs):
    answer = 0
    for num, boolean in zip(absolutes, signs):
        if boolean == True:
            answer += num
        else:
            answer -= num
    return answer
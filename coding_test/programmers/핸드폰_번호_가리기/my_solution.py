def solution(phone_number):
    answer = ''
    for idx, i in enumerate(phone_number):
        if idx > (len(phone_number)-5):
            answer += i
        else :
            answer += '*'
    return answer
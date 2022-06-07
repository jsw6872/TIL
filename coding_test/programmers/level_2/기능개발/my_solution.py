def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        count = 0
        while (progress < 100) :
            progress += speed
            count += 1
        days.append(count)

    answer = []
    count = 0
    for i in days:
        if i > count:
            answer.append(1)
            count = i
        else:
            answer[-1] += 1

    return answer
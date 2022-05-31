def solution(participant, completion):
    completion.sort()
    participant.sort()
    for a in range(len(completion)):
        if participant[a] != completion[a]:
            return participant[a]
    return participant[a+1]
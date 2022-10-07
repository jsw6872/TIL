def solution(spell, dic):
    for word in dic:
        count = 0
        for i in range(len(spell)):        
            if spell[i] in word:
                count += 1
        if count == len(spell):
            return 1
    return 2
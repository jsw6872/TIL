def solution(lottos, win_nums):
    best_rank = 0
    worst_rank = 0
    rank_dict = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5}
    lottos.reverse()
    
    for idx in range(len(lottos)):
        if lottos[idx] in win_nums:
            win_nums.pop(win_nums.index(lottos[idx]))
            best_rank += 1
            worst_rank += 1
        elif lottos[idx] == 0:
            if len(lottos) >= 1:
                best_rank += 1

    if best_rank < 2:
        best_score = 6
        worst_score = 6
    elif worst_rank < 2:
        best_score = rank_dict[best_rank]
        worst_score = 6
    else:
        best_score = rank_dict[best_rank]
        worst_score = rank_dict[worst_rank]
    
    return [best_score, worst_score]
from collections import Counter

def solution(array):
    count_dict = Counter(array)

    max_num = max(count_dict.values())
    
    count = 0
    r_key = None
    
    for key in count_dict:
        if count_dict[key] == max_num:
            count += 1
            r_key = key
    if count == 1:
        return r_key
    else:
        return -1
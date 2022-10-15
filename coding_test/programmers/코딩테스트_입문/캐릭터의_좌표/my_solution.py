def solution(denum1, num1, denum2, num2):
    top_num = denum1*num2 + num1*denum2
    bottom_num = num1 * num2
    
    if bottom_num == top_num:
        return [1, 1]
    
    if top_num % bottom_num == 0:
        return [top_num // bottom_num, 1]
    
    maxnum = 1
    for num in range(maxnum, bottom_num):
        if bottom_num % num == 0 and top_num % num == 0:
            maxnum = num 
    
    return [top_num // maxnum, bottom_num // maxnum]
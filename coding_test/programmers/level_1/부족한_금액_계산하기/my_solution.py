def solution(price, money, count):
    answer = 0
    for num in range(1,count+1):
        answer += num * price
    if answer < money:
        return 0
    return (answer - money)
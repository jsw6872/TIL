# 외계어 사전
## 문제
첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

재한사항
- 0 <denum1, num1, denum2, num2 < 1,000


|denum1|num1|denum2|num2|result|
|:---:|:---:|:---:|:---:|:---:|
|1| 2 | 3 |4|[5,4]|
|9|2| 1 |3|[29,6]|

## 걸린시간
17분 - 예외 상황이 많아서 오래걸림
## 나의 풀이
```python
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
```

## 다른 풀이
math 모듈을 이용하여 최소공배수를 구할 수 있음
```python 
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
```

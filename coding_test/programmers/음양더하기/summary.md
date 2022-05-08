# 나누어 떨어지는 숫자 배열
## 문제
어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
## example

|absolute|signs|result|
|:---:|:---:|:---:|
|[4,7,12]| [true,false,true] | 9 |
|[1,2,3]| 	[false,false,true] | 0 |

## 걸린시간
6분
## 나의 풀이
```python
def solution(absolutes, signs):
    answer = 0
    for num, boolean in zip(absolutes, signs):
        if boolean == True:
            answer += num
        else:
            answer -= num
    return answer
```
---
## 다른 사람의 풀이 (똑같은데 sum이랑 한 줄로 짬)
```python
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
```

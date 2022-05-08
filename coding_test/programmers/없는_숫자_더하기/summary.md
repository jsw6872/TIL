# 없는 숫자 더하기
## 문제
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
## example
|numbers|result|
|:---:|:---:|
|[1,2,3,4,6,7,8,0]| 14  |
|[5,8,4,0,6,7,9]| 6|
		
## 걸린시간
4분
## 나의 풀이
```python
def solution(numbers):
    answer = 0
    for i in range(0,10):
        if i not in numbers:
            answer += i
    return answer
```
---
## 다른 사람의 풀이 (sum 이용)
```python
def solution(numbers):
    return 45 - sum(numbers)
```

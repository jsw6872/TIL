# 두 정수 사이의 합
## 문제
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
## 걸린시간
4분
## 나의 풀이
```python
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for num in range(a,b+1):
        answer += num
    return answer
```
---
## 다른 사람의 풀이 (sum & max & min)
```python
def adder(a, b):
    return sum(range(min(a,b),max(a,b)+1))
```
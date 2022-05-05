# 수박수박수박수
## 문제
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
## example
input : ["Jane", "Kim"]  
output : "김서방은 1에 있다"
## 걸린시간
4분
## 나의 풀이
```python
def solution(seoul):
    for idx, item in enumerate(seoul):
        if item == 'Kim':
            return f'김서방은 {idx}에 있다'
```
---
## 다른 사람의 풀이 (리스트 index 및 format 함수)
```python
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
```
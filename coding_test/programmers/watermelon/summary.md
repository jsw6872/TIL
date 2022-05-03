# 수박수박수박수
## 문제
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
## 걸린시간
3분
## 나의 풀이
```python
def solution(n):
    str_dict = {0:'수', 1: '박'}
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += str_list[0]
        else:
            answer += str_list[1]
    return answer
```
---
## 다른 사람의 풀이 (문자열 슬라이싱)
```python
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)
```
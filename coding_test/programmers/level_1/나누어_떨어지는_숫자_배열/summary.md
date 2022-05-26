# 나누어 떨어지는 숫자 배열
## 문제
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
## example

|arr|divisor|return|
|:---:|:---:|:---:|
|[5, 9, 7, 10]| 5  | [5, 10]  |
|[2, 36, 1, 3]| 1| [1, 2, 3, 36]  |
| [3,2,6]|10|[-1]|
		
## 걸린시간
6분
## 나의 풀이
```python
def solution(arr, divisor):
    arr.sort()
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        answer = [-1]
    return answer
```
---
## 다른 사람의 풀이 (빈 리스트는 False로 처리돼서 or 뒤가 연산됨)
```python
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
```

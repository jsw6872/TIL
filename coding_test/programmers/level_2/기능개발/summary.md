# 최댓값과 최솟값
## 문제
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.  

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.  

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.  

## 제한조건
- 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
## example

|progresses|speeds|return|
|:---:|:---:|:---:|
|[93, 30, 55]|[1, 30, 5]|[2, 1]|
|[95, 90, 99, 99, 80, 99]|[1, 1, 1, 1, 1, 1]	|[1, 3, 2]|

## 걸린시간
35분
## 나의 풀이
```python
def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        count = 0
        while (progress < 100) :
            progress += speed
            count += 1
        days.append(count)

    answer = []
    count = 0
    for i in days:
        if i > count:
            answer.append(1)
            count = i
        else:
            answer[-1] += 1

    return answer
```
---
## 다른 사람의 풀이
```python
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0] <- ((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
```

## ISSUE
```python 
for i in days:
    if i > count:
        answer.append(1)
        count = i
    else:
        answer[-1] += 1

return answer
```
- 해당 알고리즘 생각하는데 대부분의 시간씀
  - 변수 할당
# 두 개 뽑아서 더하기
## 문제
- 로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다.
- 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.
- 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
- 알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
- 알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
- 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
## 입출력 예 (페이지 참고)

## 걸린시간
25분
## 나의 풀이
```python
def solution(lottos, win_nums):
    best_rank = 0
    worst_rank = 0
    rank_dict = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5}
    lottos.reverse()
    
    for idx in range(len(lottos)):
        if lottos[idx] in win_nums:
            win_nums.pop(win_nums.index(lottos[idx]))
            best_rank += 1
            worst_rank += 1
        elif lottos[idx] == 0:
            if len(lottos) >= 1:
                best_rank += 1

    if best_rank < 2:
        best_score = 6
        worst_score = 6
    elif worst_rank < 2:
        best_score = rank_dict[best_rank]
        worst_score = 6
    else:
        best_score = rank_dict[best_rank]
        worst_score = rank_dict[worst_rank]
    
    return [best_score, worst_score]
```
---
## 다른 사람의 풀이 (count 사용 : 리스트의 특정 값 개수 반환)
```python
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
```
- 카운트를 통해 0의 개수를 센다
- 하나씩 돌면서 당첨번호에 번호가 있으면 카운트를 1증가 시킴
- 최고 순위일 땐 0의 개수만큼 플러스, 아닐 땐 그대로 카운트
- 랭크에 있는 인덱스를 반환
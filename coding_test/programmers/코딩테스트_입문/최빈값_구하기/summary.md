# 최빈값 구하기
## 문제
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

재한사항
- 0 < array의 길이 < 100
- 0 ≤ array의 원소 < 1000


|array|result|
|:---:|:---:|
|[1, 2, 3, 3, 3, 4]		| 3	 |
|[1, 1, 2, 2]|-1|
|[1|1|

## 걸린시간
16분
## 나의 풀이
```python
from collections import Counter

def solution(array):
    count_dict = Counter(array)

    max_num = max(count_dict.values())
    
    count = 0
    r_key = None
    
    for key in count_dict:
        if count_dict[key] == max_num:
            count += 1
            r_key = key
    if count == 1:
        return r_key
    else:
        return -1
```

## 다른 풀이

```python 
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
```
> while문과 set을 통해 array의 item들을 없애다가 for문이 끝났을 때 하나만 남아있으면 i가 0이기 때문에 해당 값을 출력, 만약 같은 개수의 아이템이 있으며면 while문에서 리스트 아이템들이 다 사라지기 때문에 바로 -1을 return
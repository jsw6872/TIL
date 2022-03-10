# 신규 아이디 추천
## 규칙
아이디의 길이는 3자 이상 15자 이하여야 합니다.  
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.  
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
## 문제
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.  
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.  
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.  
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.  
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.  
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.  
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.  
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.  
## 나의 풀이
```python
def solution(new_id):
    allow_list = ['-', '_', '.']
    answer = ''
    # 1단계
    new_id = new_id.lower()
    # 2
    for char in new_id:
        if char.isalpha() or char.isalnum() or char in allow_list:
            answer += char
    # 3
    while '..' in answer:
        answer = answer.replace('..','.')
    #4 빈 문자열일 때 슬라이싱이 안 된다
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if answer == '':
        answer = answer.replace('','a')
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    # 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer
```
## 풀면서 생긴 ISSUE
* `.lower()` : 전체 문자를 map 형태로 소문자 변경이 가능(한 글자씩 접근할 필요 X)
* `.isalpha()` , `.isalnum()` : 해당 문자가 알파벳이거나 숫자이면 `True` 반환
* 연속된 문자의 치환 : ex) `.....` 이 반복 시에 `..`을 `.`을 통해 치환 가능
```python
while '..' in answer:
    answer = answer.replace('..','.')
```
---
## 다른 사람의 풀이(정규식?)
```python
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
```
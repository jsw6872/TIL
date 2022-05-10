# 핸드폰 번호 가리기
## 문제
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
## example

|phone_number|return|
|:---:|:---:|
|"01033334444"|"*******4444"|
|"027778888"|"*****8888"|

		
## 걸린시간
5분
## 나의 풀이
```python
def solution(phone_number):
    answer = ''
    for idx, i in enumerate(phone_number):
        if idx > (len(phone_number)-5):
            answer += i
        else :
            answer += '*'
    return answer
```
---
## 다른 사람의 풀이 (문자열 슬라이싱 및 연산)
```python
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
```

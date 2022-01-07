# 파이썬입문과 크롤링기초 부트캠프
## 크롤링 코드 패턴으로 익히기
```python
import requests 
from bs4 import BeautifulSoup
res = requests. get('https'://v.media.daum.net/v/~~)  
soup = BeautifulSoup(res.content, 'html.parser')
# 한글이 꺠질 시에 필요한 코드
# BeautifulSoup(res.content.decode('euc-kr', 'replace'), 'html.parser')
mydata = soup.find('h3')
mydata.get_text()
```
### 필요 라이브러리 호출
* requests : 해당 url에 요청을 보내는 모듈
* bs4(BeautifulSoup) : 웹페이지 분석(크롤링) 라이브러리
```python
import requests 
from bs4 import BeautifulSoup
``` 

### 웹 페이지 가져오기
* `requests.get(URL)` : 크롤링 할 페이지 url주소의 내용 가져오기
> `res = requests. get('https'://v.media.daum.net/v/~~)`
> > `res.content` : res의 내용을 보여준다

### 웹페이지 파싱
* 파싱이란 : 문자열의 의미 분석
> `soup = BeautifulSoup(res.content, 'html.parser')`  
> html.parser울 아용한 클래스

### 필요한 데이터 추출하기
`mydata = soup.find('h3')` : 원하는 소스코드 앞 부분을 넣으면 그 줄이 나온다.(필요한 데이터 추출하는 코드 넣는 곳)  
`mydata.get_text()`  

---

## 웹 구조와 HTML 이해
### HTML
* 마크업 언어(xml 등)
  > 문서나 데이터 구조를 표현하는 언어
* 웹페이지를 만드는 언어    
```html
구조 예:
<!DOCTYPE html>  
<html>
  <head>
    <title>HTML test</title>
      <meta charset="utf-8">
  </head>
    <body>
      <b>Hello html!</b>
    </body>
</html>
```
  > head부분은 웹 상단 타이틀, body 부분은 내용
* 태그에는 속성을 넣을 수 있다(속성과 속성 사이에는 한칸 띄운다)  
   > `<img src="이미지파일이름.png" width="100" height="100">`
* `<br>` : 엔터 역할을 한다
* `id="id_name"` : 특정 태그에 이름을 붙일 때 사용
  > `<img src="이미지파일이름.png" width="100" height="100" id="id_name">`
* meta 태깅은 화면에서 표시되지 않고 검색과 같은 기능을 돕는 역할
* 필요한 태깅 및 기능은 필요할 때 찾기

---
## HTML 이해를 바탕으로 크롤링하기
### 같은 태깅을 가지고 있을 때 하나만 가지고 오는 방법
```python
import requests 
from bs4 import BeautifulSoup
res = requests.get('https://v.media.daum.net/v/~~')
soup = BeautifulSoup(res.content, 'html.parser')  
mydata = soup.find('h3') # 수정 필요
mydata.get_text()
```
  > > 1. `mydata = soup.find('h3', class_ = cssstyle)` : 속성이 class이고 속성값이 cssstyle인 h3태깅을 가져온다.
  > > 2. `mydata = soup.find('h3', attrs = {'align' : 'center'})` : 속성이 align이고 속성값이 center인 h3태깅을 가져온다
  > > 3. `mydata = soup.find(id = 'body')` : 속성이 단 하나일 때 해당 문법도 가능

### 조건을 만족하는 데이터 다 가져오기(find_all)
`data = soup.find_all('p')` : 태깅이 p인 데이터를 모두 가져와서 리스트 형태로 저장  

 ---
## CSS
### CSS 언어 적용
1. style 속성으로 태그 넣기  
```css
<td style="text-align:center;color:blue">
``` 
  > 각 속성 안에 프로퍼티와 적용하고 싶은 값을 넣어 설정, 붙여써도 상관없음

2. `<head>` 안에 `<style>` 태그로 넣기
    > ex)td에 해당하는 모든 태그는 밑에 양식을 따르게 된다

  ```css
  <style type="text/css">
  td {font-size: 2em;font-family:Gulim;text-align: center;}
  </style>
  ```
3. CSS 파일을 통해
   >태그 옆 class는 그룹으로 묶어서 중복으로 사용 가능, 스타일을 지정할 때 쓰는 이름으로 속성에 css파일 형태로 스타일을 저장해 이름을 설정하고 속성값에 넣음으로써 css스타일을 적용 가능, id는 태그 내에선 하나만 사용 가능
---

## 크롤링 팁
1. 크롬 브라우저를 통해 개발자 모드로 찾을 내용을 쉽게 찾을 수 있다(Command + Alt + i)
2. 추출한 것에서 또 추출하기
   > 1. find()로 크게 감싸는 HTML 태그로 추출 후
   > 2. 다시 추출된 데이터에서 find_all()로 원하는 부분을 추출  
```python
res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content,'html.parser')  
section = soup.find('ul', id='hobby_course_list')
titles = section.find_all('li','course')
for title in titles:
  print(title.get_text())
```
---
## CSS Selector 사용법
### .select()
* `find_all()`와 동일한 기능을 한다
* 결과값은 리스트 형태로 반환된다
  1. 하위 태그 이용
```python
res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('ul li') #하위 태그관계를 통해서도 가능(띄워쓰기로 구분), `>`는 가장 근접한 태그를 가져온다
```
  2. CSS class 이름으로 검색
```python
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('.course')
```
3. id 이름으로 검색
```python
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select('#start')
```
### .select_one()
* 리턴값 리스트 X
```python
res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css.html')
soup = BeautifulSoup(res.content,'html.parser')
items = soup.select_one('#start')
```
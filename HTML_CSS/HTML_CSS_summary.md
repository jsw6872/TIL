# HTML
## 웹사이트에 들어갈 내용 담당
---
### HTML 태깅 종류
* `<title>  </title>` : 웹 사이트 제목
* `<h1> </h1>` ~ `<h6> </h6>` : 머리말 크기 순 6이 젤 작음 (heading)
* `<p>  </p>` : 문단
* `<b>  </b>` : 글자 굵게
* `<strong> </strong>` : b와 같으나 스크린리더등과 같은 것에서 강조 된다
* `<i> </i> `: 기울임
* `<em> </em>` : i와 같으나 강조가 목적(emphasized)
* `<meta charset="utf-8">` : 한글 디코딩(닫는 태깅 필요없음), `<h>` 내에 쓰는 것을 권장
* `<body> </body>` : 웹페이지에 실제로 노출되는 내용을 감싸준다(꼭 쓸 필요X)
* `<head> </head>` : body 외의 내용(꼭 쓸 필요X)(css style, link 등)
* `<html> </html>` : 사이에 모든 내용은 html(꼭 쓸 필요X)
* `<a href="~~~">하이퍼링크</a>` : 해당 링크로 이동하는 내용 추가(내부 디렉토리 파일도 가능)
* `<img src="~~~" width="300" heigt="200">` 이미지링크를 통해 가져옴, 가로 세로 조정 가능(%도 가능)
* `<p class='color size'>`  : 클래스 2개 가능
* `<input type="text" id="myInput" placeholder="type anything">` : placeholder의 내용을 갖고 있다

# CSS
## 웹사이트의 스타일 담당
* `font-size: 100` : 폰트사이즈
* `font-weight: 100` : 폰트 굵기
* `font-family: "Times New Roman", Times, serif` : 폰트 설정
* `text-align : left, right, center` : 글자 정렬
* `color : 색` : 글자 색
* `margin-bottom,left,...: 20px` : 여백(padding : 4방향)
* `text-decoration: underline, overline, linethrough, none` : 글자 줄 설정
* `display: block, inline, inline-block` : 한줄, 딱 맞게, 길이 설정 가능
* `cursor: pointer...` : 

### ex)  
* 동일 태깅의 같은 스타일을 줄 때(h1)
```css
<style>
    h1 {
        font-size: 64px;
    }
    .class_name .poster{ /*클래스 중첩 가능*/
        background-color : 'red'
        display: block;
        text-align: center;
    }
</style>
```
* 태그 안에 직접 설정
```html
<h1 style="color: red font-size: 72px;">가나다</h1> <!-- css내용을 바로 확인학고자할 때-->
```
* 태그에 태그 설정을 통해(h1 > i)
```css
<style>
    h1 i{
        font-size: 64px;
    }
</style>
```
* 클래스를 각각 지정해 스타일을 저장해놓고 필요할 때 사용
```css
<style>
    .larget-text {
        font-size: 64px;
    }
    .medium-text {
        margin-left: auto;
    }
</style>
```  
```html
<p> 이 <i class="large-text">글자</i>는 글씨 크기가 64px이지만, 이 <i class="medium">글자</i>sms 글씨 크기가 32px이다</p>
```
* id를 이용 (한 페이지의 중복 불가)

```css
<style>
    #larget-text {
        font-size: 64px;
    }
    #medium-text {
        font-size: 32px;
    }
</style>
```  
#### * `<div> </div>` : 요소 묶는 기능(별 다른 기능은 없음) class부여해서 일관성 가지게(줄이 바뀐다)
#### * `<span> </span>` : 줄 바꿈이 없음

### CSS style 파일 따로 만들어서 적용
* 파일에 css style 구문 작성(head칸에 적는것 권장)
  ex)
```css
<link href="파일경로.css" rel="stylesheet">
```

# JavaScript
## 웹사이트의 인터렉션 담당(동적기능)

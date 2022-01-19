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
* `<a href="~~~">링크이름</a>` : 해당 링크로 이동하는 내용 추가(내부 디렉토리 파일도 가능)
* `<img src="~~~" width="300" heigt="200">` 이미지링크를 통해 가져옴, 가로 세로 조정 가능(%도 가능)
* `<p class='color size'>`  : 클래스 2개 가능
* `<input type="text" id="myInput" placeholder="type anything">` : placeholder의 내용을 갖고 있다
* `<ul></ul>` : 순서가 없는 목록 태그

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

# HTML/css 토픽 2
## Box Model
* margin : 이 요소와 다른 요소 사이의 공간(border와 화면 사이의 거리)
* border : 테두리
* padding : 내용과 테두리(border) 사이 여유공간
* width : 가로를 해당 길이만큼
* min-width : 가로길이가 최소 해당길이 이상을 가진다(해당 길이보다 작아지면 더 이상 줄지 않아서 잘린다)
* max-width : 가로길이가 최대 해당길이까지만 가진다(해당 길이보다 커지면 더 이상 늘지 않는다)
* heightr : 세로
* `box-sizing : border-box` : 패딩과 테두리가 가로 길이, 세로 길이에 포함
* 모든 곳에 적용 `*{box-sizing : border-box};`
* `background-image: url("~~~")` : 배경에 이미지 넣기
* `bakcground-size: cover`: 배경 이미지의 사이즈를 비율에 맞춰서 창에 크기에 따라 달라진다
*  `background-position: ~~` : 짤릴 위치 설정(가로 세로로 늘렸을  때)

## overflow(넘치는 부분) : 화면이 짤렸을 때 해결방법
- `overflow : hidden` : 짤린 부분을 숨긴다
- `overflow : scroll` : 스크롤 나타난다
- `overflow : auto` : 내용이 많을 때 스크롤바

## 마우스 오버(마우스가 올라갔을 때 변화)
ex)
```css
h1:hover {
  color: green;
}
```

## display
* 주로 inline 아니면 block을 가짐(inline은 필요한 길이만큼 한 줄에 같이 있으려는 성질, block은 반대)
* `display: inline,, block` : 디스플레이의 성질 설정
* `display: inline-block` : inline은 크기가 기본 auto이지만 block처럼 길이를 설정할 수 있는 태그

## 다양한 링크
* 택스트와 이미지를 한 블록에 넣고 링크 링크 만들기
```html
<a href='~~~~~' class='link'>
    <img src='./image_link.png'>
    <p>링크로 가는 글</p>
</a>
```
```css
.link {
    display: block; 
    /* 링크를 나타내는 a태그는 inline 속성으로 하나로 못 묶기 때문에 block설정을 통해 한의 요소로 합쳐준다 */
}
```
## baseline
* img의 baseline은 사진 가장 밑이고 텍스트는 글자 바로 밑
* 마지막 요소가 div의 baseline (아무 것도 없을 땐 box의 끝이 baseline)

## float
### 목적 : 뉴스와 같은 레이아웃을 만들기 위해(사진 옆에 글 시작)

## clear
### float된 요소를 치워서 다음 영역으로 옮긴다

## 반응형 웹 그리드
### 크기에 따라 달라지는 그리드
```css
@media (min-width: 768px){
    h1{
        fontsize: 36px;
        /* 가로가 768이 넘어가면 폰트 사이즈가 36이 된다. */
    }
}
```
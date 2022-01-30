# 원드라이브 클론 코딩에서의 이슈
## HTML
- flex 를 이용한 화면 레이아웃 구성
- 화면을 꽉 차게 하기 위한 설정 및 오른쪽 스크롤바가 생기는 이유
--- 
## CSS
### 화면 구성에 있어 vh, vw, % 의 차이
#### vh, vw
* parent 값에 의존하지 않아서 어디든 사용 가능
* 열려있는 화면 전체의 상대길이로 스크롤바 포함한 길이 반환
#### %
* 부모값에 의존하므로 부모에 길이 설정이 있어야 적용 가능
* 스크롤 바를 포함하지 않은 현재 화면 길이만 반환  
[reference](https://edu.goorm.io/qna/11497)
### box-sizing : border-box
### justify-content
### vertical-align
---
## JS
### 체크박스 삭제 each-function
### 하나씩 체크 시에 새로 생성된 파일은 css가 적용 안됨
### 전체 체크 기능에 map 기능 및 활용

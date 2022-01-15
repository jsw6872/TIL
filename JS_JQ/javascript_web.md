# javascript 
## id로 태그 선택
```javascript
const myTag = document.getElementById('id_name'); // id속성을 통해 요소를 가져온다.(const : 상수 선언, 한 번 선언 후 값 변경 불가, let은 가능)
```
## class로 태그 선택
```javascript
const myTags = document.getElement(s)ByClass('class_name'); // class속성을 통해 해당하는 모든 요소를 가져온다.
```
## Tag이름으로 Tag선택
```javascript
const btns = document.getElemen(s)tByTagName('tag_name'); // tag이름을 통해 요소를 가져온다.
```

## css 선택자로 태그 선택
```javascript
document.querySelector('#myNumber')
document.getElementById('myNumber') // 위와 동일한 결과
document.querySelector('.myNumber') // 가장 첫번째만
document.querySelectorAll('.myNumber') // 모두 다
document.getElemntsByClassName('.myNumber') // 위와 동일
```
## 이벤트와 버튼 클릭
```javascript
const btn = document.querySelector('#myBtn');
btn.onclick = function () {
    console.log('Hello !'); // 버튼 누르면 Hello ! 출력
};
```
## inner/outer HTML, textContext
```javascript
const myTag = document.querySelector('#list-1');
console.log(myTag.outerHTML); // list-1 태그를 포함한 HTML 출력
myTag.outerHTML = '<ul id="new-list"><li>change sentence</li></ul>'; // 내용이 바뀐다
console.log(myTag.innerHTML); // list-1 태그 뺴고 HTML 출력
myTag.innerHTML = '<li>change sentence</li>'; // 내용이 바뀐다
console.log(myTag.textContent); // HTML 내용 출력
myTag.textContent = 'change sentence' // 내용이 바뀐다
```
## 요소 추가
```javascript
// 1. 요소 노드 만들기: document.createElement('태그이름')
const first = document.createElement('li');
// 2. 요소 노드 꾸미기: textContent, innerHTML, ...
first.textContent = '처음';
// 3. 요소 노드 추가하기: NODE.prepend, append(마지막), after, before
tomorrow.prepend(first); 
```
## 삭제 및 이동
```javascript
// 노드 삭제와 이동
const today = document.querySelector('#today');
const tomorrow = document.querySelector('#tomorrow');
tomorrow.remove();

// 노드 이동하기: prepend, append, before, after
today.append(tomorrow.children[1]);
```
## 이벤트핸들러
```javascript
let btn = document.querySelector('#myBtn');
function event1() {
	console.log('Hi Codeit!');
}
// elem.addEventListener(event, handler)
btn.addEventListener('click', event1);
//onclick과 달리 중복 가능
```
```javascript
function updateToDo(event) {
  event.target.classList.toggle('done');
} // event가 발생한 대상에 대해 done클래스 부여
```

## 이벤트 버블링 제거(자식 -> 부모로 가는 이벤트)

## 이밴트 버블링을 이용한 이벤트 위임(새로운 요소가 생겼을 때 이벤트 자동 위임)
```javascript
const list = document.querySelector('#list');
list.addEventListener('click', function(e) {
	// if (e.target.tagName === 'LI') (item 영역 외엔 이벤트가 안 생기게)
	if (e.target.classList.contains('item')) {
		e.target.classList.toggle('done');
	}
});
```


# Jquery
* script 태그 앞에 붙여넣기
```javascript
$('#photo').attr('src', 'images/seoul.png');
//document.getElementById('photo').src = 'images/home.png';와 동일

$('#seoul').css('font-weight','bold')
////document.getElementById('seoul').style.fontweight = 'bold'와 동일

<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
```
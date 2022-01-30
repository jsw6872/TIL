# reactivity & 라이브러리화
```javascript
function init(){
    Object.defineProperty(viewModel, 'str', {
        // 속성에 접근했을 때의 동작을 정의
        get : function(){
            console.log('접근');
        }
        // 속성에 값을 할당했을 때의 동작을 정의
        set: function(newValue){
            render(newValue);
        }
    });
}

function render(value){
    div.innerHTML = value;
}

init();
```
```javascript
viewModel.str = 'change contents'; // div.innerHTML 내용 변경
```

# 뷰 인스턴스
* 뷰 개발 시 필수로 생성해야 하는 코드
```javascript
var vm = new Vue({
    element : '#id_name', // id_name을 가진 id 태그에 
    data : {
        message : 'hi' // hi출력
    }
})
```

# 생성자 함수
```javascript
// class 개념
function Person(){
    // class 내의 함수 개념
    this.personInfo = function(name, job){
        this.name = name;
        this.job = job;
    }
}
```
```javascript
var person = new Person();
var a = new p.personInfo('name', 'job');
```
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
```html
<div id="app">
    {{ message }}
</div> 
```
```javascript
var vm = new Vue({
    el : '#id_name', // id_name을 가진 태그에 
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

# 뷰 컴포넌트
* 컴포넌트 : 화면의 영역을 구분하여 개발할 수 있는 뷰의 기능
* 인스턴스를 생성하면 기본적으로 root컴포넌트가 된다
```javascript
new Vue({
    el: '#id_name'
});

// 뷰컴포넌트 이용해 태그 만들기(app-header라는 태그 찾아서 그 안에 template 내용 넣음)
Vue.component('app-header', {
    template: '<h1>Header</h1>
});
```
## 지역 컴포넌트
```javascript
new Vue({
    el: '#app', // app id를 가진 태그 안에
    components:{
        'app-footer':{ // app-footer 태그를 찾아서
            template : '<footer>footer</footer>' // 내용 삽입
        }
    }
});
```
# props 속성
```html
<div id="app">
    <!-- <app-header v-bind:props속성이름='상위컴포넌트 데이터 이름'></app-header>  -->
    <app-header v-bind:propsdata='message'></app-header>
    <app-content v-bind:propsdata='num'></app-content>
</div>
```
```javascript
var appHeader = {
    template: '<h1>{{propsdata}}</h1>', 
    props : ['propsdata']
}
var appContent = {
    template: '<div>{{propsdata}}</div>'
    props : ['propsdata']
}

new Vue({
    el: '#app',
    components: {
        'app-header': appHeader
        'app-content': appContent
    },
    data: {
        message : 'hi !'
        num: 10
    }
})
```
# event emit
```html
<div id="app">
    <app-button></app-button>
</div>
```
```javascript
var appButton = {
        // 클릭을 했을 때 passEvent가 실행된다
        template: '<button v-on:click="passEvent">click</button>',
        methods: {
            passEvent: function(){
                this.$emit('pass');
            }
        }
    }
new Vue({
        el: '#app',
        components: {
            'app-button':appButton
        }
    });
```
## eventemit으로 콘솔 출력하기
```html
<div id="app">
    <app-button></app-button>
</div>
```
```javascript
var appButton = {
        // <button v-on:하위컴포넌트에서 발생한 이름="상위 컴포넌트의 매소드 이름">click</button>
        template: '<button v-on:pass="logText">click</button>',
        methods: {
            //pass 이름을 가진 event
            passEvent: function(){
                this.$emit('pass');
            }
        }
    }
new Vue({
        el: '#app',
        components: {
            'app-button':appButton
        },
        methods:{
            logText: function(){
                console.log('hi');
            }
        }
    });
```
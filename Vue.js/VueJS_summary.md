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
## event emit 을 통한 함수 실행하기
```html
<div id="app">
    <app-content v-bind:propsdata='num'></app-content>
        <!-- increase가 emit 되면 increaseNumber 실행 -->
    <app-button v-on:increase="increaseNumber"></app-button>
</div>
```
```javascript
var appContent = {
    template: '<div>{{ propsdata }}</div>',
    props: ['propsdata']
}
var appButton = { // event emit 발생 시키기
        // add라는 버튼을 누르면 addNumber 이벤트가 발생되고 increase가 emit된다.
    template: '<button v-on:click="addNumber">add</button>',
    methods: {
        addNumber: function(){
            this.$emit('increase');
        }
    }
}

new Vue({
    el: '#app',
    components: {
        'app-content':appContent,
        'app-button':appButton
    },
    methods: {
        increaseNumber: function(){ // event 발생 시 실행할 함수 생성
            this.num= this.num+1;
        }
    },
    data: {
        num : 10
    }
});
```
## 같은 컴포넌트 레벨 간의 통신 방법
* root로 데이터를 event emit으로 주고 root에서 넘겨 주려는 컴포넌트에 props로 준다
```html
<div id="app">
    <app-header v-bind:propsdata="num"></app-header>
    <app-content v-on:pass="deliverNum"></app-content>
</div>
```
```javascript
var appHeader = {
    template: '<div>header</div>',
    props: ['propsdata'] // root의 데이터값을 받는다
}
var appContent = {
    template : '<div>content<button v-on:click="passNum">pass</button></div>',
    methods: {
        passNum : function () {
            this.$emit('pass', 10);
        }
    }
}
new Vue({
    el: '#app',
    components:{
        'app-header': appHeader,
        'app-content' : appContent
    },
    data: {
        num:0 // root의 초기 데이터
    },
    methods:{
        deliverNum: function(value){
            this.num = value; // vue(root)의 Num이 0에서 10으로 변한다
        }
    }
})
```

## 뷰라우터
```html
<div id="app">
    <!-- 해당 url이 routes에 있는 path로 바뀌면 해당 component가 실행   -->
    <!-- 태그가 template으로 있는 것으로 변경 -->
    <router-view></router-view> 
</div>
```
```javascript
var LoginComponent = {
    template: '<div>login</div>'
}

var MainComponent = {
    template: '<div>main</div>'
}

var router = new VueRouter({
    // 페이지의 라우팅 정보(url 이동 시 어떤 페이지를 뿌릴지에 대한 정보) 배열로 표현
    routes : [
        // 로그인 페이지 정보
        {
            // 페이지 url
            path: '/login',
            // 해당 url에 표시될 컴포넌트
            component: LoginComponent
        },
        // 메인페이지 정보
        {
            path: '/main',
            component: MainComponent
        }
    ]
});

new Vue({
    el:'#app',
    router: router
});
```
## 변수 선언
```javascript
let a;
a = 1000;
let b = 2000;
console.log(a) //print(a)랑 동일
```
## 함수 선언
```javascript
function 함수이름(){
    명령1;
    명령2;
    명령3;
    retrun value;
}
함수이름(); //함수호출
```
## 논리연산자
* ` ===` : ==  
* ` !==` : !=
* `&&` : and
* `||` : or

## 타입확인(결과값 문자열로 반환)
```javascript
typeof 100 // type(100)
```

## 문자열 따옴표 처리
```javascript
console.log("\"Hello, I\"m groot\"") 
console.log(`"Hello, I"m groot"`) 
// "Hello, I"m groot"
```
## 형변환
```javascript
String()
Number()
Boolean() //true = 1, false = 0
```
## 템플릿 문자열
```javascript
let a = 100
console.log('a is ${a}.') // a is 100.
```

## if문
```javascript
if (조건문){
    동작
} else if (조건문2) {
    동작2
} else {
    동작3 ;
}
```

## 반복문
* for문
```javascript
for (let i = 1; i<= 10; i++) {
    console.log(i);
} // i = 1부터 조건을 만족할 때까지 1씩 더해가며 반복
// 추가동작부분(i++는 동작부분에 넣어도 됨)
```
* while문
```javascript
let i = 1;
while (조건) {
    console.log(i)
    i++;
} // i = 1부터 조건을 만족할 때까지 1씩 더해가며 반복
// 추가동작부분(i++는 동작부분에 넣어도 됨)
```
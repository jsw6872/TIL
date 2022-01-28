# 모듈의 개념
```javascript
const m = require('/math-tools.js'); // 모듈을 로드해서 객체 하나를 리턴할 수 있음
console.log(m.add(1,2));
```
* 모듈 사용을 위한 외부 공개
```javascript
function add(a,b){
    return a+b;
}
exports.add = add;
// add라는 함수를 add라는 이름으로 외부로 공개
// 사용할 때 add로 사용해야 힘

module.exports = add; // 파일 내에 있는 모든 모듈 export
```

# 동기적 실행 / 비동기 실헹
## 동기적 실행
* 한줄씩 실행, 다음 작업은 현 작업이 끝나야 실행된다  
  ex) readFileSync(), 점원이 주문을 받고 음식을 주고 다음 주문 받음
## 비동기적 실행
* 특정 작업이 완료됐을 때 실행할 콜백을 등록해두고 바로 다음 코드로 실행을 넘기는 것  
    ex) readFile(), 점원이 계속해서 주문을 받고 음식이 나올 때에 나눠줌
> Node.js 는 비동기를 추천

# 프로세스 / 스레드
## 프로세스 : 하나의 프로그램
## 스레드 : 프로그램 내에서 작업 실행 단위
### Node.js의 메인스레드 역할 : 
- CPU로 하는 수치 계산 작업
- 네트워크로 들어오는 클라이언트의 요청을 받아들이고 응답하는 작업
>  Node.js는 CPU-intensive job(고화질 이미지 처리, 복잡한 시뮬레이션 계산, 딥러닝 작업 등)에는 적절하지 않음
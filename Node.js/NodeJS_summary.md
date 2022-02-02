# 코드잇 Node.js
## 모듈의 개념
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

## 동기적 실행 / 비동기 실헹
### 동기적 실행
* 한줄씩 실행, 다음 작업은 현 작업이 끝나야 실행된다  
  ex) readFileSync(), 점원이 주문을 받고 음식을 주고 다음 주문 받음
## 비동기적 실행
* 특정 작업이 완료됐을 때 실행할 콜백을 등록해두고 바로 다음 코드로 실행을 넘기는 것  
    ex) readFile(), 점원이 계속해서 주문을 받고 음식이 나올 때에 나눠줌
> Node.js 는 비동기를 추천

## 프로세스 / 스레드
### 프로세스 : 하나의 프로그램
### 스레드 : 프로그램 내에서 작업 실행 단위
#### Node.js의 메인스레드 역할 : 
- CPU로 하는 수치 계산 작업
- 네트워크로 들어오는 클라이언트의 요청을 받아들이고 응답하는 작업
>  Node.js는 CPU-intensive job(고화질 이미지 처리, 복잡한 시뮬레이션 계산, 딥러닝 작업 등)에는 적절하지 않음

## 웹 서버
```javascript
const http = require('http'); //http 모듈 불러오기
const server = http.createServer(function (request, response) {
  response.end('<h1>Hello World<h1>'); //응답할 때마다 해당 내용
});

server.listen(3000); //3000번 포트로 연결
```

# web-2 Node.js
## 파일 내용 읽기 및 directory 위치 불러오기
```javascript
var fs = require('fs');

// file 읽기
fs.readFile('sample.txt', 'utf-8', function(err,data){
    console.log(data);
});

// directory 목록 읽기(list로 출력)
var testFolder = './';
var fs = require('fs');

fs.readdir(testFolder, function(error, filelist){
    console.log(filelist);
})
```

## URL을 통해 입력된 값 사용하기, 내용 불러오기
```javascript
// http 모듈을 사용해 값 가져와서 http에 할당
var http = require('http'); 
// fs 모듈을 사용해 값 가져와서 fs에 할당
var fs = require('fs'); 
// url 모듈을 사용해 값 가져와서 url에 할당
var url = require('url'); 

function templateHTML(title, list, body){
  return `
  <!doctype html>
  <html>
  <head>
    <title>WEB1 - ${title}</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1><a href="/">WEB</a></h1>
    ${list}
    ${body}
  </body>
  </html>
  `;
}
function templateList(filelist){
  var list = `<ul>`;
  var i = 0;
  while(i<filelist.length){
    list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
    i++;
  }
  list = list + `</ul>`;
  return list;
}

var app = http.createServer(function(request, response){
    var _url = request.url; //????????
    var queryData = url.parse(_url, true).query; // 해당 _url에 query 정보 
    var pathname = url.parse(_url,true).pathname; 
    console.log(url.parse(_url, true));

    if(pathname === '/'){ // 정상적인 루트
      if(queryData.id === undefined){ // id 부분이 /라서 아무 것도 없는 web을 눌렀을 때
        fs.readdir('./', function(err, filelist){ // web부분을 눌렀을 때 출력 부분
        console.log(filelist);
        var title = 'Home';
        var description = 'Hello, world !';
        var list = templateHTML(filelist);
        var template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);
      
        response.writeHead(200);
        response.end(template); //해당 내용을 웹에서 실행
        })
    } else { // 다른 부분을 눌렀을 때
        fs.readdir('./', function(err, filelist){
          console.log(filelist);
          // queryData.id에 해당하는 파일 내용을 읽는다(/?id='~') ~에 해당하는 부분
          fs.readFile(`./${queryData.id}`,"utf-8", function(err,description){
            var title = queryData.id;
            var list = templateList(filelist);
            var template = templateHTML(title, list, `<h2>${title}</h2><p>${description}</p>`);
            response.writeHead(200);
            response.end(template);
            });
        });
      }
    } else { // 비정상적인 루트
      response.writeHead(404);
      response.end('Not found');
    }
});
app.listen(3000);
```

## 동기 & 비동기적 실행
* 동기는 코드 순서대로 실행
* 비동기 코드
```javascript
var fs = require('fs');
console.log(1);
fs.readFile('./2.txt', 'utf-8', function(err,result){
  //err은 파일 에러날 때, result는 파일의 내용
  console.log(result);
});
console.log(3);
```
> 1,3,2

## callback
```javascript
var a = function(){
  console.log('a');
}
function slowfunc(callback){
  callback();
}

slowfunc(a);
```

## form 태그
```html
<!-- action 주소에 각 input의 name과 값으로 querystring을 생성  -->
<!-- post로 할 시 url상에 정보가 숨겨잔다(서버 데이터를 수정이나 삭제할 때 사용) -->
<form action="http://~~" method="post">
  <p><input type="text" name="title"></p>
  <p><textarea name="description"></textarea></p>
  <p><input type="submit"></p>
</form>
```

## post로 전송된 데이터 가져오기
```javascript
if(pathname==='/create_process'){ // submit 한 url이 조건일 때
        var body =``;
        request.on('data', function(data){// post방식으로 많은 데이터를 전달할 때 data라는 인자로부터 콜백 함수 호출
            body += data;
        });
        request.on('end', function(){ // 정보 수신이 끝났을 때
            var post = qs.parse(body); //post에는 post로 전송한 name,데이터가 array로 담겨있다
            var title = post.title; 
            var description = post.description;
        });
    response.writeHead(200);
    response.end('success');
    }
```
## create를 통한 파일 생성, update를 통한 파일 수정, delete(form)을 이용한 파일 삭제
## 입출력정보에 관련된 보안
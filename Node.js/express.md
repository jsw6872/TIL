# express
## 기본 세팅 (기존 node.js 어떻게 다른지 비교)
- 터미널에서 `npm init`
- `npm install express`
```javascript
const express = require('express')
var fs = require('fs')
const app = express()
const port = 3000
var template = require(`./lib/template.js`)


// app.get('url주소', function(req, res)
app.get('/', function(req, res){
    fs.readdir('./data', function(error, filelist){
          var title = 'Welcome';
          var description = 'Hello, Node.js';
          var list = template.list(filelist);
          var html = template.HTML(title, list,
            `<h2>${title}</h2>${description}`,
            `<a href="/create">create</a>`
          );
          response.send(html);
    });   // 페이지 표시
})
// app.listen(3000) 과 동일한 코드
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
```

## route parameters
### ex)
```
Route path: /users/:userId/books/:bookId
Request URL: http://localhost:3000/users/34/books/8989
req.params: { "userId": "34", "bookId": "8989" }
```
```javascript
app.get('/page/:pageId', function(request, response){
    response.send(request.params);
});
```
## 기본 사용
- `npm install mysql --save` 을 통해 sql 모듈 설치
config.js
```
require("dotenv").config();

var config = {
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  connectionLimit: 10,
};

module.exports = config;
```
index.js
```
var mysql = require("mysql");
var config = require("./config");

var pool = mysql.createPool(config);

function getConnection(callback) {
  pool.getConnection(function (error, connection) {
    if (!error) {
      callback(connection);
    }
  });
}

module.exports = getConnection;
```
- routes/users.js에 쿼리문을 통해 뽑아올 데이터 작성
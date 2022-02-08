## 기본 사용
- `npm install mysql --save` 을 통해 sql 모듈 설치
config.js
```javascript
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
```javascript
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
## routes/users.js에 쿼리문을 통해 뽑아올 데이터 작성
ex)
```javascript
var express = require("express");
var router = express.Router();

var getConnection = require("../db/index");

/* GET api/users listing. */
router.get("/", function (req, res) {
  getConnection(function (connection) {
    connection.query("SELECT * FROM users", function (error, results) {
      if (error) throw error;
      console.log(results);
      res.send(results);
    });
    connection.release();
  });
});
router.get("/:id", function (req, res) {
  var userId = req.params.id;
  getConnection(function (connection) {
    connection.query(
      `SELECT * FROM users WHERE id = ${userId}`,
      function (error, results) {
        if (error) throw error;

        console.log(results[0]);

        res.send(results[0]);
      }
    );
    connection.release();
  });
});
module.exports = router;
```
# Node.js Mysql & Sequelize
## Squelize
### 설치 및 초기화
`npm install`  
`npm install mysql2`  
`npm install sequelize`  
`npm install sequelize-cli`  
`sequelize init`  
### ORM 
- 객체 및 관계형 데이터베이스의 데이터를 자동으로 매핑해주는 것
- 자바스크립트 구문을 SQL문으로 변경해줌
### sequelize 문법
- databaase 만들기
### `config.js`
```javascript
{
  "development": {
    "username": "root", 
    "password": null, // mysql password
    "database": "nodejs", // 생성하고자하는 database명 적어주기
    "host": "127.0.0.1", 
    "dialect": "mysql" 
  }
}
```
`$ sequelize db:create` : nodejs라는 데이터베이스 생성
- table 만들기
### `models/user.js`
```javascript
const Sequelize = require('sequelize');

module.exports = ((sequelize,DataTypes)=>{
    return sequelize.define('user',{
        email:{
            type: Sequelize.STRING(40),
            allowNull: true,
            unique: true,
        },
        nick:{
            type: Sequelize.STRING(15),
            allowNull: false,
        },
        password:{
            type: Sequelize.STRING(100),
            allowNull: true, // 카카오 로그인은 비번 필요없으니,,
        },
        prvider :{ // 뭐로 로그인 했는지 : 카카오, 로컬,,
            type: Sequelize.STRING(10),
            allowNull: false,
            defaultValue: 'local',
        },
        snsId:{
            type: Sequelize.STRING(30),
            allowNull: true,
        },

    },{
        timestamps:true,
        paranoid : true, // 삭제일 (복구용)
    })
})
```
### `models/comment.js`
```javascript
module.exports = (Sequelize, DataTypes) => {
  return Sequelize.define('comment', {
    comment: {
      type: DataTypes.STRING(100),
      allowNull: false
    },
    created_at: {
      type: DataTypes.DATE,
      allowNull: false,
      defaultValue: Sequelize.literal('now()')
    },
  }, {
    timestamps: false,  // 생성일을 Sequelize가 자동으로 생성하지 말라는 옵션 
    underscored: true,   // Snake Case를 권장한다는 옵션
  });
}
```
### `models/index.js`
- 모듈화 시킴
- 관계 만들기 ( user - 1 : N - comment )
```javascript
db.User = require('./user')(sequelize, Sequelize);
db.Comment = require('./comment')(sequelize, Sequelize);

db.User.hasMany(db.Comment, { foreignKey: 'commenter', sourceKey: 'id'});   // 사용자는 여러개의 댓글을 가질 수 있음
db.Comment.belongsTo(db.User, { foreignKey: 'commenter', targetKey: 'id' }); // 작성자가 한명임  
```
### `app.js`
```javascript
"""
"""
var { sequelize } = require('./models') // 추가

"""
"""
```
`$ npm start`
### CRUD 이용
`index.js`
#### Create (insert values)
```javascript
models.User.create({
  user_name: "John"
}).then(_ => console.log("Data is created!"));
```
#### Read (select)
```javascript
models.User.findAll().then(console.log);
```

#### Update ( update )
```javascript
models.User.findOne({ where: { user_name: "John" }})
.then(user => {
  if (user) {
    user.update({ user_name: "Bob" })
    .then(r => console.log("Data is updated!"));
  }
});
```
#### Delete ( drop )
```javascript
models.User.destroy({ where: { user_name: "Bob" }})
.then(_ => console.log("Data was deleted!"));
```
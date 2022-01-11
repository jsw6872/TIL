# 여러 커밋을 하나로 합치기 (rebase)
## rebase
`git rebase HEAD~2` : 최근 2개의 커밋을 합친다
## rebase의 옵션
* s
* p
* ..

# branch & merge

## branch
* branch를 통해 분할된 작업 수행
* 따로 branch를 하지 않을 땐 하나의 branch 유지
## branch를 하는 시점은 언제인가
* 원래 소스코드를 유지하면서 다른 버전의 파일을 만들고 싶은 경우
* 여러 시나리오를 시도할 때

## brnach 관련 명령어
`git branch` : 현재 생성된 branch가 무엇이 있는지 확인 가능  
`git branch branch_name` : 해당 이름의 branch 생성  
`git checkout branch_name` : 해당 branch로 변경
* `git log`를 통해 해당 branch의 버전 확인 가능 
* `git log --branches` 를 통해 모든 branch의 로그를 확인 가능하나 가독성이 떨어질 수 있다
* * `git log --branches --decorate` : HEAD 돼있는 branch가 현재 branch이며 가장 최신 버전의 다른 branch파일도 확인 가능
* * `git log --branches --decorate -graph` : branch log의 정보를 가시적으로 확인 가능
* `git log exp..master` : exp엔 없고 master에는 있는 것을 보여준다
* `git log -p exp..master` : master에는 있는 version과 코드의 차이를 보여준다

`git diff master..exp` : 각각의 branch 현재상태 비교

## merge
* 현재 설정된 branch로 merge가 된다  
`git merge exp` : exp의 파일이 합병된다(현재 branch와 exp 두 개의 보모를 가진 현재 branch가 된다)

`git branch -d exp` : exp 브랜치 삭제

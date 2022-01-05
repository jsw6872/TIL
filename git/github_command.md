## repository 생성  
1. 원격저장소가 이미 존재하는 경우(gith)
> 1. github에 새로운 repository 생성
> 2. 원하는 작업 디렉토리 생성 후 해당 디렉토리에서 `or create a new~ `코드 복사 후 실행
2. 로컬저장소에서 이미 만든 작업을 새로운 원격저장소에 올리는 경우
> 1. `git init` 을 통해 작업 디렉토리에 Git 저장소 생성
> 2. `gid add` 와 `git commit`을 통해 작업한 파일 commit
> 3. github에 원격저장소 생성하고 `git remote`를 통해 로컬저장소와 연결
> 4. `git push` 를 통해 업로드

## remote
`git remote add origin http~ ` : 해당 주소를 origin으로 설정  
`git remote ` : 설정된 주소의 alias를 모두 보여준다  
`git remote -v` : 설정된 주소의 alias 및 주소를 모두 보여준다  

## push
`git push origin master ` : origin 주소에 master 브래닟로 commit된 파일 보낸다

## clone
`git clone 주소` : 원격 저장소에 있는 걸 내 컴퓨터로 동기화  
`git clone 주소 git_home` : git_home 디렉토리를 만들고 그 파일을 clone 한다  
`git clone -b <branch명> <remote_repo 주소>` : 특정 브랜치의 내용을 클론하고 싶을 때

## pull
`git pull` : 원격 저장소에 있는 걸 내 컴퓨터로 동기화  

## git clone VS git pull
| clone | pull |
|:---:|:---:|
|clone은 로컬저장소와 원격저장소가 완전 일치(복제)되는 것으로 기존 작업 내용이 있다면 바뀐다 그래서 보통 프로젝트의 처음에 사용|pull은 원격 저장소의 내용을 로컬저장소로 가져와 merge를 해주는 것으로 기존의 작업 내용이 유지된다|  

## commit 작업을 되돌릴 때 (revert, remote)  

## 브랜치 삭제
1. 로컬 브랜드 삭제 : `git branch -d 브랜치명`
2. 로컬 브랜드 삭제 push : `git push -d origin 삭제한 브랜치명`
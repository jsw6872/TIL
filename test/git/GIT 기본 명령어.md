# GIT 기본 명령어
### 기본 터미널
pwd :  현재 디렉토리의 위치 알려줌
ls -al : 현재 디렉토리의 파일을 알려줌
### init & vim 사용법 & cat & status & add
git init : 현재 디렉토리에서 작업을 시작 

vim  파일명.확장자명 : vim 에디터를 이용해서 파일을 생성 및 편집
— i : 편집 가능, esc : 나가는 것, : wq : 저장 후 quit
cat 파일명: 파일 내용 확인

git status : 파일의 상태를 알려준다

git add 파일명 : 파일을 git 관리를 위해 설정
- 초기의 git 버전관리 할당 시에도 사용하고 파일이 수정된 후 버전을 새로 만들어주기 전에도 add를 통해 할당시켜줘야 함
- add를 통해 stage에 commit 대기상태인 파일들이 있고 commit으로 버전 할당해주면 repository 에 올라가게 된다.

git config --global user.name 이름: 버전 이름을 설정해준다
git config --global user.email 이메일 : 버전 메일을 설정해준다

git commit : vim이 실행되며 git 버전정보의 내용을 보여주며 작성 가능
* git commit -a : add 없이 수정된 파일 전부 commit
* git commit -am “적을 버전” : vim 실행 없이 바로 가능 

Git log : git 버전정보 알려준다

cp f1.txt f2.txt :  f1 파일 내용을 카피해서 f2 파일을 만든다

git log -p : 버전마다의 차이를 보여준다 
: 앞 버전의 파일
 +++ : 현재 버전의 파일

Commit 옆이 각 버전의 id

git diff : 파일이 수정되고 명령어 실행시 차이점 보여준다(commit 하기 전)
* git diff id..id2 :  id id2의 차이점 보여준다

git reset id --hard : 버전의 head가 해당 id를 가진 버전이 되지만 실제로 그 상위 버전들이 삭제가 되는 것은 아니다. 공유한 git은 리셋하면 안 됨


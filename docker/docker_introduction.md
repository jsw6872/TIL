## Docker 클라이언트

Docker 클라이언트 (docker)는 많은 Docker 사용자가 Docker와 상호 작용하는 기본 방법입니다.  

docker run와 같은 명령을 사용하면 클라이언트가이 명령을 dockerd에 전송하여 실행합니다.  

이 docker명령은 Docker API를 사용합니다.  

Docker 클라이언트는 둘 이상의 데몬과 통신 할 수 있습니다.  
---
## Docker 클라이언트

Docker 레지스트리 는 Docker 이미지를 저장합니다. Docker Hub는 누구나 사용할 수있는 공용 레지스트리이며 Docker는 기본적으로 Docker Hub에서 이미지를 찾도록 구성됩니다.  
자신의 개인 레지스트리를 실행할 수도 있습니다.  

docker pull또는 docker run명령 을 사용하면 구성된 레지스트리에서 필수 이미지를 가져옵니다. docker push명령 을 사용하면 이미지가 구성된 레지스트리로 푸시됩니다.  

---
## Docker의 특징
- LXC - jail, LXD등
- Kernal의 공유 -> No Booting -> memory 적재(내부 application 별 run은 별도
- cgroup -> Control group, Process 격리 방식
- Hub docker
- aufs -> 적층형 이미지 - 효율적 저장소 관리/네트워크 코스트 절감
  - 기존에 있는 이미지는 빼고 추가로 위에 쌓는 방식
- Device-mapper -> Ubuntu에 특화되어있음
- Version 표기 방식 -> [연도.월] -> 18.03/06/09/12(stable)
---


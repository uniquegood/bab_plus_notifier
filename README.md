# bab_plus_notifier

밥플러스 성수역V1타워점(1호점) 메뉴 안내 슬랫봇 프로그램

### EC2 생성 후 처음 해야 할 일

1. 아래 명령어 실행

```sh
git config --global user.email "{GitHub에 이메일}"
git config --global user.name "{GitHub 이름}"
```

2. 방화벽 확인

```sh
sudo systemctl status ufw
```

3. github repo clone

```sh
git clone https://github.com/KOREAparksh/bab_plus_notifier.git
```

4. 권한 설정 및 init.sh 실행

```sh
chmod 755 init.sh init2.sh init_swap_memory.sh init_node.sh
./init.sh
```

5. `exit` 명령어로 zsh 나온 후 init2.sh 실행

```sh
exit
./init2.sh
```

6. ssh 접속 종료 후 재 접속

7. swap memory 설정 및 확인 `메모리 용량 설정은 스크립트 내에서 직접 설정할 것, 기본 2GB로 설정함`

```sh
./init_swap_memory.sh

free
```

8. init_node.sh 실행. (뭔가 창이 뜨면 `q`를 눌러 나가기).

```sh
./init_node.sh

#nvm --version 으로 설치 확인
#npm --v 으로 설치 확인
#node -v 으로 설치 확인
#yarn -v 으로 설치 확인
```

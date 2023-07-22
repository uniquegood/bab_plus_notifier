# bab_plus_notifier

밥플러스 성수역V1타워점(1호점) 메뉴 안내 슬랫봇 프로그램

### EC2 초기 설정 명령어 및 확인사항

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

4. 권한 설정 및 init.sh 실행 `꼭 sudo로 실행할 것.`

```sh
chmod 755 init.sh
sudo ./init.sh

```

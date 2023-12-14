# bab_plus_notifier

밥플러스 성수역V1타워점(1호점) 메뉴 안내 슬랫봇 프로그램

not yet

### EC2 생성 후 처음 해야 할 일

| 설치 중 다른 창이 뜨면서 선택해야 할 일이 있으면, 그냥 Enter를 누른다.

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
cd bab_plus_notifier
chmod 755 init.sh init2.sh init_swap_memory.sh init_python.sh init_package.sh
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

8. init_python.sh와 init_package.sh를 순서대로 실행

```sh
./init_python.sh
./init_package.sh

# python3 --version 파이썬 실행 확인
# pip3 --version pip3 확인
```

9. `.env-sample`을 복제하여 `.env`파일 생성 및 내용 추가

10. 서버 timezone 세팅

11. 아래 명령어로 프로그램 실행
```sh
# 실제 슬랙으로 날라감
python3 src/main.py 0 $Home # 점심
python3 src/main.py 1 $Home # 저녁
python3 src/main.py 2 $Home # 금요일 저녁
# or
# 테스트 슬랙으로 날라감
python3 src/test.py 0 $Home # 점심
python3 src/test.py 1 $Home # 저녁
python3 src/test.py 2 $Home # 금요일 저녁
```

# man
특정 명령이나 자원들의 메뉴얼을 출력하는 명령어
오프라인 환경 등 검색이 불가능한 상황에서 사용하기 좋다.

```sh
$ man man
$ man -k 키워드     # 키워드가 포함된 모든 메뉴얼 출력
$ mak -f 키워드     # 키워드가 일치하는 메뉴얼 목록
$ man -w 키워드     # 키워드와 일치하는 메뉴얼 페이지의 위치

$ man 2 키워드      # 시스템 콜 영역의 메뉴얼 페이지
$ man 3 키워드      # 라이브러리 함수 영역의 메뉴얼 페이지
```
```sh
$ ll /usr/share/man			# man page는 9개의 영역으로 구성되어 있다.
total 3508
drwxr-xr-x  2 root  wheel    13K Apr  9  2021 man1   	# General Commands
drwxr-xr-x  2 root  wheel   9.0K Apr  9  2021 man2   	# System Call
drwxr-xr-x  2 root  wheel   181K Apr  9  2021 man3   	# Library Functions
drwxr-xr-x  2 root  wheel   512B Apr  9  2021 man3lua
drwxr-xr-x  7 root  wheel    19K Apr  9  2021 man4   	# Kernel Interface
drwxr-xr-x  2 root  wheel   5.0K Apr  9  2021 man5   	# File Format
drwxr-xr-x  2 root  wheel   512B Apr  9  2021 man6   	# Games
drwxr-xr-x  2 root  wheel   1.5K Apr  9  2021 man7   	# Miscellaneous Information
drwxr-xr-x  5 root  wheel    14K Apr  9  2021 man8   	# System Manager
drwxr-xr-x  2 root  wheel    71K Apr  9  2021 man9   	# Kernel Developer
-rw-r--r--  1 root  wheel   3.0M Apr  9  2021 mandoc.db
```
**활용 예시**
```sh
$ ls /usr/include
$ vi /usr/include/stdio.h	# 함수 목록 확인
$ man 3 printf 				# 함수 용법 확인
```

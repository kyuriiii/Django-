
  * 실행환경 : Ubuntu 18.04
              Python 3.6.9
  * 실행위치 : /

  1) Python 및 Django 설치
  
    apt-get upgrade
    apt-get update
    apt-get install python3.6.9
    apt-get install python3-pip
    apt-get install python3-dev
    pip3 install Django
  
  2) 장고 프로젝트 폴더 생성
    
    mkdir /Django
    
  3) 프로젝트 만들기
  
    django-admin startproject 프로젝트명
    
  4) 실행 세팅 변경하기
    
    프로젝트명/settings.py 의 ALLOWED_HOSTS를 아래와 같이 변경.
    ALLOWED_HOSTS = ['IP주소']
    
    

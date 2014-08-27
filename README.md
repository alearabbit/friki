## 멋쟁이 사자처럼 2기 학생들을 위한 Python Flask Skeleton for Google App Engine

Google App Engine에서 [Flask micro framework](http://flask.pocoo.org)를 이용한 Python 애플리케이션을 구축하기 위한 뼈대 입니다.

[원본 뼈대](https://github.com/GoogleCloudPlatform/appengine-python-flask-skeleton)에서 app 폴더를 추가한 정도입니다.

## Quick start

0. 해당 프로젝트를 SourceTree를 통해 Clone합니다.

   ```
   https://github.com/rishubil/appengine-python-flask-skeleton-for-likelion.git
   ```
1. 의존 모듈을 해당 프로젝트의 lib 폴더에 설치합니다.

   Note: App Engine은 프로젝트 내부에 직접 포함된 라이브러리만 import 할 수 있습니다.

   ```
   cd appengine-python-flask-skeleton-for-likelion
   pip install -r requirements.txt -t lib
   ```
2. [app.yaml](app.yaml) 파일의 9번째 줄의 'your-application-id-here'를 해당 프로젝트의 application-id로 변경합니다.

   ```
   [app.yaml]
   ...
   # using cloud.google.com/console use the "project id" for your application
   # id.
   application: your-application-id-here
   version: 1
   runtime: python27
   ...
   ```
3. 프로젝트를 로컬에서 실행해 봅니다.

## Licensing
See [LICENSE](LICENSE)

## Author
원 프로젝트: Logan Henriquez and Johan Euphrosine

해당 프로젝트: Nesswit(Heewon Lee)

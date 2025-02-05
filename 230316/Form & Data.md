##### Form & Data

: 데이터를 보내고 가져오기

**HTML form's attributes**

1. action
   
   - 입력 데이터가 전송될 url을 지정
   
   - 데이터를 어디로 보낼 것인지를 지정하는 것이며 이 값은 반드시 유효한 url이어야 함
   
   - 만약 이 속성을 지정하지 않으면 데이터는 현재 form 이 있는 페이지의 url로 보내짐

2. method
   
   - 데이터를 어떻게 보낼 것인지 정의
   
   - 입력 데이터의 http request methods를 지정
   
   - html form데이터는 오직 2가지 방법으로만 전송할 수 있는데 바로 GET방식과 POST방식

**HTML \<input> element**

- type 속성에 따라 동작 방식이 달라진다

- 핵심 속성 : name > name을 키로 하는 키와 값의 형태로 서버로 보내짐

**HTTP request methods**

- HTTP
  
  HTML문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)

- 웹에서 이루어지는 모든 데이터 교환의 기초

- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의

- 자원에 대한 행위(수행하고자 하는 동작)를 정의

- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄

- HTTP Method 예시
  
  GET, POST, PUT, DELETE

**GET**

- 서버로부터 정보를 조회하는데 사용
  
  : 서버에게 리소스를 요청하기 위해 사용

- 데이터를 가져올 때만 사용해야 함

- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송 : 데이터는 URL에 포함되어 서버로 보내짐

**Query String Parameters**

- 사용자가 입력 데이터를 전달하는 방법 중 하나로 url주소에 데이터를 파라미터를 통해 넘기는 것

- 이러한 문자열은 엠퍼샌드(&)fh dusrufehls key=value쌍으로 구성되며 기본 url과 물음표로 구분됨

- Query String이라고도 함

- 정해진 주소 이후에 물음표를 쓰는 것으로 쿼리스트링이 시작함을 알림

- =로 key와 value가 구분됨

- 파라미터가 여러개일 경우 &을 붙여 여러개의 파라미터를 넘길 수 있음

##### Retrieving the data(server)

- 데이터 가져오기(검색하기)
  
  - 모든 요청 데이터는 view함수의 첫번째 인자 request에 들어있다

#### Model

- 개요
  
  - 모델의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해
  
  - django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

---

**Database**

- 체계화된 데이터의 모임

- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템

- Database의 가장 기초적인 키워드에 대해 알아보고 자세한 내용은 추후 Database시간에 다룰 예정

**Database 기본 구조**

- 스키마 schema

- 테이블 table

**Schema**

- 뼈대

- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

**Table**

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합

- 관계라고도 부름

- 필드
  
  : 속성 또는 컬럼
  
     각 필드에는 고유한 데이터 형식이 지정됨(int, text 등)

- 레코드
  
  : 튜플 또는 행
  
     테이블의 데이터는 레코드에 저장됨

- PK(Primary Key)
  
  - 기본 키
  
  - 각 레코드의 고유한 값(식별자로 사용)
  
  - 기술적으로 다른 항목과 절대로 중복될 수 있는 단일 값(unique)
  
  - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

- 쿼리
  
  - 데이터를 조회하기 위한 명령어
  
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)
  
  - Query를 날린다 > 데이터를 조작한다

---

**모델 이어서..**

- django는 모델을 통해 데이터에 접근하고 조작

- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함

- 저장된 데이터베이스의 구조(layout)

- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑

*models.py 작성*

- 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것

##### Migrations

- django가 모델에 생긴 변화(필드 추가 수정 등)를 실제 DB에 반영하는 방법

- 주요 명령어
  
  makemigrations(지금 모델 상태를 데이터베이스에 반영 가능한 마이그레이션 파일로 만들어주는것)
  
  : 모델의 변경사항에 대한 새로운 migration을 만들때 사용
  
  migrate(내가 가진 마이그레이션 파일을 실제 데이터베이스에 반영하는 명령어)

**migration 3단계**

1. models.py 에서 변경사항이 발생하면

2. migration 생성
   
   makemigrations

3. DB반영
   
   migrate

**ORM**

- object realational mapping

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유혀으이 시스템 간에 데이터를 변환하는 프로그래밍 기술

- SQL를 사용하지 않고 데이터베이스를 조작할 수 있게 만들어줌

- 장점
  
  - SQL을 잘 알지 못해도 객체지향 언어로 DB조작이 가능
  
  - 객체지향적 접근으로 인한 높은 생산성

- 단점
  
  - orm만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

**Model : 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구**

##### Database API

- 장고가 제공하는 ORM 을 사용해 데이터베이스를 조작하는 방법

- Model을 정의하면 데이터를 만들고 읽고 수정하고 지울 수 있는 API를 제공

**Database API 구문**

Article.objects.all()

\> Model class.Manager.Queryset API

**object manager**

- 모뎅리 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스

- 장고는 기본적으로 모든 장고모델 클래스에 대해 objects라는 manager 객체를 자동으로 추가함

- 이 manager를 통해 특정 데이터를 조작할 수 있음

- DB를 Python class로 조작할 수 있도록 여러 메서드를 제공

**Query**

- 데이터베이스에 특정한 데이터를 보여달라는 요청ㄷ

- 파이썬으로 작성한 코드가 orm에 의해 sql로 변환되어 데이터베이스에 전달되며 데이터베이스의 응답 데이터를 orm이 queryset이라는 자료 형태로 변환하여 우리에게 전달

**Queryset**

- 데이터베이스에서 전달받은 객체 목록(데이터 모음)
  
  \> 순회가 가능한 데이터로서 1개 이상의 데이터를 불러와 사용할 수 있음

- 장고 orm을 통해 만들어진 자료형이며 필터를 걸거나 정렬 등을 수행할 수 있음

- objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체

- 단 데이터베이스가 단일한 객체를 반환할때는 queryset이 아닌 모델의 인스턴스로 반환됨

**데이터 객체를 만드는(생성하는) 3가지 방법**

1. article = Article()
   
   클래스를 통한 인스턴스 생성

2. article.title
   
   클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

3. article.save()
   
   인스턴스로 save 메서드 호출



article : 입력시 정보알수있음

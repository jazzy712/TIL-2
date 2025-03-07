## PJT

- '남들이 만들어 놓은 요청을 보내는 코드를 가져다가 쓴다'

- **라이브러리**

## API

- 클라이언트가 원하는 기능을 수행하기 위해 서버 측에 만들어놓은 프로그램
  
  - 데이터 저장, 조회, 수정, 삭제 ...

- 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 **api**를 미리 만들어둠
  
  - 클라이언트는 서버가 미리 만들어 놓은 주소로 요청을 보냄

- 날씨 정보를 제공해주는 **api**
  
  - 날씨 정보를 가지고 있는 서버
  
  - 해당 서버가 제공하는 **api**(무료)

- 오픈 api
  
  - 외부에서 사용할 수 있도록 무료로 개방(open)된 api
  
  - 사용법은 공식 문서에 명시
  
  - 프로젝트에서 사용되는 api
    
    - openweathermap api : 기상 데이터 및 날씨 정보를 제공하는 오픈 api
    
    - 금융상품통합비교공시 api : 금감원에서 제공하는 금융상품 정보를 제공하는 오픈 api
  
  - 주의사항
    
    - 너무 많은 계정에서 동시에 요청 보내면  서버가 견디지 못함
    
    - **api key**를 활용하여 사용자 확인
    
    - 일부 오픈 api는 사용량이 제한

## JSON

- '자바스크립트 객체 표기법'

- **경량의 텍스트 기반의 데이터 형식**

- 통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 표현 방법
  
  - 데이터는 중괄호({})로 둘러쌓인 키-값 쌍의 집합으로 표현됨
  
  - 키 = 문자열/ 값 = 다양한 데이터 유형
  
  - 값은 쉼표(,)로 구분됨

```python
{
    "name : "김싸피",
    "age" : 28,
    "city" : "서울 캠퍼스",
    "hobbies" : [
        "공부하기",
        "복습하기"
],
"isStudent" : true
}
```

- 파싱(parsing)
  
  - 데이터를 의미 있는 구조로 분석하고 해석하는 과정

- json.loads()
  
  - json 형식의 문자열을 파싱하여 python Dictionary로 변환

## Data Science(시험 x)

- 다양한 데이터로부터 새로운 지식과 정보를 추출하기 위해 과학적 방법론, 프로세스, 알고리즘, 시스템을 동원하는 융합분야
  
  - 다양한 학문의 원리와 기술 활용

- 1. 문제정의 
  
  2. 데이터 수집
  
  3. 데이터 전처리(정제) : 실절적 분석 수행위해 데이터 가공하는 단계
     
     1. 수집한 데이터의 오류 제거(결측치, 이상치), 데이터 형식 변환 등
  
  4. **데이터 분석** : 전처리 완료된 데이터에서 필요한 정보 추출하는 단계
  
  5. 결과 해석 및 공유 : 결과 해석 및 시각화 후 공유

- **Numpy**
  
  - 수학 계산용 패키지, pandas와 matplotlib 을 사용하기 위해 활용되는 패키지
  
  - 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 패키지
  
  - 장점
    
    - numpy 행렬 연산은 데이터가 많을수록 python 반복문에 비해 빠르다
    
    - 다차원 행렬 구조 제공하여 개발하기 편하다
  
  - 특징
    
    - CPython(공식사이트의 Python) 에서만 사용가능

- **Pandas**
  
  - 프로그래밍 버전의 엑셀을 다루듯 고성능의 데이터 구조 작성 가능
  
  - numpy 기반 만들어진 패키지로, 

- **MatPlotLib**
  
  - 다양한 종류의 그래프와 도표 생성, 데이터 시각적 표현

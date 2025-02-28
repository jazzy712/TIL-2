## Error & Exception

- Bug
  
  - 소프트웨어에서 발생하는 오류/결함
  
  - 프로그램의 예상된 동작과 실제 동작 사이의 불일치

- Debugging
  
  - 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
  
  - 프로그램의 오작동 원인 식별하여 수정하는 작업
  
  - 1. print  함수 활용
    
    2. 개발환경(text editor, IDE) 등에서 제공하는 기능 활용
    
    3. Python tutor 활용
    
    4. 뇌 컴파일, 눈 디버깅 

- Error
  
  - 프로그램 실행 중에 발생하는 예외 상황
  
  - Syntax Error
    
    - 프로그램 구문이 올바르지 않은 경우 발생
  
  - Exception
    
    - 프로그램 실행 중에 감지되는 에러

- Exception
  
  - 프로그램 실행 중 감지되는 에러
  
  - 내장 예외(built-in exception)
    
    - 예외 상황을 나타내는 예외 클래스들



- Exception Handling(예외 처리)
  
  - 예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법
  
  -  try
    
    - 예외가 발생할 수 있는 코드 작성
  
  - except
    
    - 예외가 발생했을 때 실행할 코드 작성
  
  - else
    
    - 예외가 발생하지 않았을 때 실행할 코드 작성
  
  - finally
    
    - 예외 발생 여부와 상관없이 항상 실행할 코드 작성



- try-except
  
  - try 블록 안에는 예외가 발생할 수 있는 코드 작성
  
  - except 블록 안에는 예외가 발생했을 때 처리할 코드 작성
  
  - 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
```

```python
try:
    num = int(input('숫자입력 : '))
except ValueError:
    print('숫자가 아닙니다.')
```

- 복수 예외 처리

```python
try:
    num = int(input('숫자입력 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('제대로 좀 입력해')

try:
    num = int(input('100을 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('0으로는 나눌 수 없어')
except:
    print('에러가 발생했습니다.')
```

- else & finally
  
  - else 블록은 예외가 발생하지 않았을 때 추가 작업 진행
  
  - finally 블록은 예외 발생 여부와 상관없이 항상 실행할 코드 작성

```python
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('유효한 숫자가 아닙니다.')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료되었습니다.')
```

- 예외 처리 주의사항

```python
# 가장 구체적인 예외부터 처리하고, 마지막에 범용 예외를 처리하도록 순서를 배치
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
# 1) 구체적인 예외부터
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('숫자를 넣어주세요.')
# 2) 마지막에 광범위한 예외(Exception)
except Exception:
    print('에러가 발생하였습니다.')
```

- 예외 객체 다루기
  
  - as 키워드
    
    - 예외가 발생했을 때 예외에 대한 정보 담고 있는 객체
    
    - except 블록에서 예외 객체받아 상세한 예외 정보 활용 가능
  
  ```python
  my_list = []
  
  try:
      number = my_list[1]
  except IndexError as error:
      # list index out of range가 발생했습니다.
      print(f'{error}가 발생했습니다.')
  ```
  
  - try-except 와 if-else
    
    - try-except와 if-else 함께 사용할 수 있음
  
  ```python
  try:
      x = int(input('숫자를 입력하세요:'))
      if x < 0:
          print('음수는 허용되지 않습니다.')
      else:
          print('입력한 숫자:', x)
  except ValueError:
      print('오류 발생')
  ```

- EAFP & LBYL
  
  - EAFP(Easier to Ask for Forgiveness than Permission)
    
    - 예외처리를 중심으로 코드를 작성하는 접근방식(try-except)
    
    - 코드 실행하고 예외 발생하면 예외처리 수행
    
    - 예외 상황 예측하기 어려운 경우 유용
  
  ```python
  # EAFP (Easier to Ask for Forgiveness than Permission, 허락보다 용서 구하기)
  try:
      result = my_dict['key']
      print(result)
  except KeyError:
      print('Key가 존재하지 않습니다.')
  ```
  
  - LBYL(Look Before You Leap)
    
    - 값 검사를 중심으로 코드 작성하는 접근방식(if-else)
    
    - 코드 실행 전 조건문 등을 사용하여 예외 상황 미리 검사하고, 예외 상황 피하는 방식
    
    - 예외 상황 미리 방지하고 싶을 때 유용
  
  ```python
  # LBYL (Look Before You Leap, 돌다리도 두들겨보고 건너기)
  if 'key' in my_dict:
      result = my_dict['key']
      print(result)
  else:
      print('Key가 존재하지 않습니다.')
  ```

# selenium을 통한 크롤링
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = '/Users/joseong-u/workspace/crawling실습/chromedriver' # Chromedriver 설치 경로

driver = webdriver.Chrome(path)

driver.get('https://python.org') # url 받기
print(driver.title) # 웹의 제목 출력
```

### `.find_element_by_name('q')` 
* 최초 발견한 name="q" 태그 기져옴

### `.find_elements_by_name()`
* 최초 발견한 name 옵션  리스트 형태로 기져옴

### `find_element_by_tag_name()`
* 태그 이름으로 검색

### `find_elements_by_tag_name()`
* 태그 검색한 결과 리스트로 반환

### `find_element_by_id`
* id 옵션을 통해 검색
### `find_element_by_css_selector`
* 
### `find_element_by_class_name`
* class 옵션으로 검색
### `.clear()`
* input 텍스트 초기화
  
### `.send_keys()`
* 해당 인자를 키 이벤트 전송

### `.send_keys(Keys.RETURN)`
* 엔터 입력

### `time.sleep(5)` : 5초 기다리기
* `import time` 모듈 필요
* 명시적으로 일정 시간 기다리기(검색우의 딜레이를 기다리고 크롤링 하기 위해)

### `.title`
* 웹 상단의 제목

### `.current_url`
* 웹의 url 표시

### `.quit()`
* 브라우저 종료

## selenium으로 크롤링 하기
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = '/Users/joseong-u/workspace/crawling실습/chromedriver' # Chromedriver 설치 경로

driver = webdriver.Chrome(path)

driver.get('https://python.org') # url 받기

assert 'python' in driver.title # 웹 상단 타이틀에 Python 이 없으면 실행 중지

searchbar = driver.find_element_by_name('q') # 검색창으로 이동

#키 이벤트 전송
searchbar.send_keys("python") # 검색창에 python 검색
searchbar.send_keys(Keys.RETURN)
#검색하는데 걸리는 로딩 시간을 기다리기 위해 코드를 2초 쉰다
time.sleep(2)

titles = driver.find_elements_by_tag_name('h3')
# 타이틀 리스트들을 하나씩 출력
for title in titles:
    print(title.text())

driver.quit()
```
## headless 옵션(브라우저창을 띄우지 않고 크롤링)
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = '/Users/joseong-u/workspace/crawling실습/chromedriver' # Chromedriver 설치 경로
headless_options = webdriver.ChromeOptions() # 옵션 설정
headless_options.add_argument('headless') # headless 옵션 선택
driver = webdriver.Chrome(path, options = headless_options)

assert 'python' in driver.title # 웹 상단 타이틀에 Python 이 없으면 실행 중지

searchbar = driver.find_element_by_name('q') # 검색창으로 이동

#키 이벤트 전송
searchbar.send_keys("python") # 검색창에 python 검색
searchbar.send_keys(Keys.RETURN)
#검색하는데 걸리는 로딩 시간을 기다리기 위해 코드를 2초 쉰다
time.sleep(2)

titles = driver.find_elements_by_tag_name('h3')
# 타이틀 리스트들을 하나씩 출력
for title in titles:
    print(title.text())
```
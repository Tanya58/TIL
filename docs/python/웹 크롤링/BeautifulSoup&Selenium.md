# 웹 크롤링
동적페이지는 크롤링 할 수 없는 메신저봇의 한계를 해결하기 위해 작성되었습니다. <br> 
~~파이썬 공부는 덤~~ 

- 크롬 개발자 도구 `F12`를 통해 크롤링하려는 사이트의 코드를 확인하며 진행할 것! 


## Python 3.7.4 설치 
- 다운로드 경로 : http://www.python.org/downloads
- 설치 및 강의 참고 : http://wikidocs.net/8

## Requests +  BeautifulSoup을 이용한 정적 페이지 크롤링 

- **Requests** : 사이트에서 HTML 소스를 가져오기 위한 라이브러리
- **BeautifulSoup** :  HTML과 XML 파일로부터 데이터를 가공하기 위한 라이브러리

### 설치 
- 필요한 Python 모듈 설치 
   ```
   pip install requests
   pip install bs4 
   ```

### 샘플 코드 
```py
# Example : 특정 웹페이지 내의 모든 링크 가져오기 
import requests
from bs4 import BeautifulSoup

# requests로 HTML 소스 가져오기 
response = requests.get('http://www.google.com') 
docs = reponse.text

# BeautifulSoup으로 문서 파싱
soup = BeautifulSoup(docs, 'html.parser') 

for link in soup.find_all('a'):
    print(link.get('href')
```
<br>

### Requests 모듈 
> Requests : https://requests.readthedocs.io/en/master/
```py
# Example 1 : GET 데이터 전달 
import requests
response = requests.get('http://www.google.com', params={'param1': 'value1', 'param2': 'value2'}) 
print(response.url) # http://www.google.com/?param1=value1&param2=value2

# Example 2 : POST 데이터 전달 
import requests
response = requests.post('http://www.google.com', data={'param1': 'value1', 'param2': 'value2'})
print(response.url) # http://www.google.com

# Example 3 : POST 복잡한 데이터 전달 
import requests, json
response = requests.post('http://www.google.com', data=json.dumps({'outer': {'inner': 'value'}))
print(response.url) # http://www.google.com

# Example 4 : 헤더 및 쿠키 전달 (GET, POST 동일)
import requests
headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'session_id': 'H2jdQy3EkfMX8t7tK'}
response = requests.get('http://www.google.com', headers=headers, cookies=cookies)
print(response.text)
```
| Requests 명령어                                | 비고                                               |
| ---------------------------------------------- | -------------------------------------------------- |
| `res = requests.get('http://www.google.com')`  | 구글 서버로 GET 요청                               |
| `res = requests.post('http://www.google.com')` | 구글 서버로 POST 요청                              |
|                                                |                                                    |
| `res.url`                                      | URL `ex.  http://www.google.com`                   |
| `res.encoding`                                 | 캐릭터셋 `ex. 'utf-8'`                             |
| `res.status_code`                              | 상태 코드 `ex. 200`                                |
| `res.headers['content-type']`                  | 콘텐츠 정보 `ex. 'application/json; charset=utf8'` |
| `res.text`                                     | 응답 텍스트 `ex. '{"type":"User"...'`              |
| `res.json()`                                   | 응답 데이터 `ex. {'private_gists': 419, ...}`      |
<br>

### BeautifulSoup 모듈 
> BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```html
<!-- HTML 데이터 샘플 -->
<html><head><title>Sample Title</title></head>
<p class="title"><b>Sample title</b></p>

<p class="story">There are  
<a href="http://link.com/el" class="sister" id="link1">El</a>,
<a href="http://link.com/la" class="sister" id="link2">La</a> and
<a href="http://link.com/til" class="sister" id="link3">Til</a>;
. :D</p>

<p class="story">...</p>
```
| BeautifulSoup 명령어                                   | 출력 결과                                                           |
| ------------------------------------------------------ | ------------------------------------------------------------------- |
| `soup = BeautifulSoup(docs,'html.parser')`             | docs 데이터에 대해 BeautifulSoup 객체 생성                          |
|                                                        |                                                                     |
| `soup.get_text()`                                      | 모든 텍스트                                                         |
| `soup.prettify()`                                      | HTML 코드를 보기 쉽게 구조화                                        |
| <font size=2 color="#df1616"> soup.\*</font>           |                                                                     |
| `soup.title`                                           | `<title>Sample Title</title>`                                       |
| `soup.p`                                               | `<p class="title"><b>Sample title</b></p>`                          |
| `soup.a`                                               | `<a class="sister" href="http://link.com/el" id="link1">Els/a>`     |
| <font size=2 color="#df1616"> soup.\*.\* </font>       |                                                                     |
| `soup.title.name`                                      | 태그 이름 `ex. title`                                               |
| `soup.title.parent.name`                               | 부모 태그 이름 `ex. head`                                           |
| `soup.p.contents`                                      | 자식 태그 리스트 `ex. ['There are  ', <a class= ... </a>, '. :D ']` |
| `soup.a['id']`                                         | `link1`                                                             |
| `soup.a.get('href')`                                   | `http://link.com/el`                                                |
| <font size=2 color="#df1616"> .text 와 .string </font> |                                                                     |
| `soup.title.text`                                      | 자식 텍스트 포함 `Sample Title`                                     |
| `soup.title.string`                                    | 자신의 순수 텍스트 `Sample Title`                                   |
| `soup.p.text`                                          | 자식 텍스트 포함 `There are  El, La and Til. :D`                    |
| `soup.p.string`                                        | 자신의 순수 텍스트 `None`                                           |
| <font size=2 color="#df1616"> .find </font>            |
| `soup.find_all('a')`                                   | `<a>` 태그를 모두 가져오기                                          |
| `soup.find('a')`                                       | 태그 이름 `<a>` 으로 찾기                                           |
| `soup.find('a', attrs={'class' : 'sister'})`           | 태그 이름과 클래스 `<a class="sister">` 으로 찾기                   |
| `soup.find(id="link3")`                                | 태그 아이디 `id="link3"` 으로 찾기                                  |
| `soup.find('a').find('b').find('c')`                   | `<a>` 태그 밑의 `<b>` 태그 밑의 `<c>` 태그 가져오기                 |
| <font size=2 color="#df1616"> .select </font>          |                                                                     |
| `soup.select('a')`                                     | `<a>` 태그를 모두 가져오기                                          |
| `soup.select_one('a')`                                 | 태그 이름 `<a>` 으로 찾기                                           |
| `soup.select_one('.sister')`                           | 태그 클래스 `class="sister">` 으로 찾기                             |
| `soup.select_one('#link3')`                            | 태그 아이디 `id="link3"` 으로 찾기                                  |
| `soup.select_one('a.sister#link3'`                     | 태그 이름, 클래스, 아이디 지정하여 찾기                             |
| `soup.select_onde('a > b > c')`                        | `<a>` 태그 밑의 `<b>` 태그 밑의 `<c>` 태그 가져오기                 |
<br>
<br>

## Webdriver + Selenium + BeautifulSoup 을 이용한 동적 페이지 크롤링 
> Selenium을 참고자료 : https://selenium-python.readthedocs.io/index.html

- **Webdriver** : Selenium이 사용할 일종의 웹 브라우저
- **Selenium** :  웹 애플리케이션을 위한 테스팅 프레임워크 (BeautifulSoup의 단점 보완)   

### 설치 
- 사용하는 크롬 브라우저 버전과 일치하는 [Web Driver](http://chromedriver.chromium./downloads) 다운로드 
- 필요한 Python 모듈 설치 
   ```
   pip install selenium 
   pip install bs4
   ```
### 샘플 소스 
```py
from selenium import webdriver
from bs4 import BeautifulSoup

#
# webdriver로 특정 페이지 접속 
#
driver = webdriver.Chrome("C:\Temporary\chromedriver.exe") # 크롬 웹 드라이버 설치 파일 경로 
driver.get("https://www.google.com")

   # ... 웹 페이지 조작 생략 

docs = driver.page_source
driver.quit()

#
# BeautifulSoup으로 문서 파싱
#
soup = BeautifulSoup(docs, 'html.parser') 

for link in soup.find_all('a'):
    print(link.get('href')
```


### WebDriver API
> Selenium 공식 API : https://www.selenium.dev/selenium/docs/api/py/api.html <br>
> Selenium 참고 API : https://selenium-python.readthedocs.io/api.html

 | driver 명령어                                                    | 결과 값                 |
 | ---------------------------------------------------------------- | ----------------------- |
 |                                                                  |                         |
 | `driver = webdriber.Chrome("C:\Temporary\chromedriver.exe")`     | 크롬 웹 브라우저 실행   |
 | `driver.quit()`                                                  | 크롬 웹 브라우저 종료   |
 | `driver.get("https://www.google.com")`                           | 특정 웹 사이트 접속     |
 | `driver.title`                                                   | 웹 페이지 타이틀        |
 | `driver.page_source`                                             | 웹 페이지 소스코드 출력 |
 | `driver.get_screenshot_as_file('result.png')`                    | 웹 페이지 스크린샷 저장 |
 | <font size=2 color="#df1616"> driver.* </font>                   |                         |
 | `driver.implicitly_wait(3)`                                      | 암시적 대기             |
 | `driver.maximize_window()`                                       | 윈도우 최대화           |
 | `element = driver.find_element_by_xpath('//*[@id="log.login"]')` | xpath로 찾기            |
 | `element = driver.find_element_by_css_selector('#hireme')`       | css로 찾기              |
 | `element = driver.find_element_by_name('sister')`                | name으로 찾기           |
 | `element = driver.find_element_by_id('link1')`                   | id로 찾기               |
 | <font size=2 color="#df1616"> element.* </font>                  |                         |
 | `element.send_keys("데이터")`                                    | `데이터` 입력           |
 | `element.click()`                                                | click 실행              |
 | `element.sumit()`                                                | submit 실행             |
 | `element.get_attribute('href')`                                  | `href` 속성 값 가져오기 |

```py
# Example 1 : 구글 검색 <input class="gLFyf gsfi" maxlength="2048" name="q" ... 
from selenium import webdriver

driver = webdriver.Chrome("C:\Temporary\chromedriver.exe") # 크롬 웹 드라이버 설치 파일 경로 
driver.get("https://www.google.com")

search_box = driver.find_element_by_name('q')   # 1. name = 'q'인 속성 찾기 
search_box.send_keys('검색할 데이터')            # 2. 검색할 키워드를 입력
search_box.submit()                             # 3. 제출합니다.
```

```py
# Example 2 : 옵션 설정 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-gpu")
# options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome("C:\Temporary\chromedriver.exe", chrome_options=options)
driver.get("https://www.google.com")
driver.implicitly_wait(3)

driver.find_element_by_name('q').send_keys('검색할 데이터').submit()
```

```py
# Example 3 : 특정 요소가 발견될 때까지 설정한 값만큼 페이지 대기 
# https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\Temporary\chromedriver.exe")
driver.get("https://www.google.com")
try:    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.ID, "아이디값")))
                          # title_is
                          # title_contains
                          # staleness_of
                          # alert_is_present
                          # visibility_of
                          # visibility_of_element_located
                          # invisibility_of_element_located                          
                          # text_to_be_present_in_element
                          # text_to_be_present_in_element_value
                          # presence_of_element_located              ←
                          # presence_of_all_elements_located          
                          # element_to_be_clickable
                          # element_to_be_selected
                          # element_selection_state_to_be
                          # element_located_to_be_selected
                          # element_located_selection_state_to_be
                          # frame_to_be_available_and_switch_to_it                
    elelment.click()
finally:
    driver.quit()
```

```py
# Example 4 : 네이버 로그인 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Temporary\chromedriver.exe")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

assert "네이버 : 로그인" in driver.title # 타이틀이 '네이버 : 로그인'이 아닐 경우, AssertionError 오류 

login = {
    "id" : "<이곳에 ID를 입력하세요>",
    "pw" : "<이곳에 PW를 입력하세요>"
}

driver.find_element_by_name('id').send_keys(login.get("id")) # 아이디 입력 
driver.find_element_by_name('pw').send_keys(login.get("pw")) # 패스워드 입력
driver.find_element_by_name('pw').send_keys(Keys.RETURN)     # 패스워드 칸에서 ENTER 입력

print(driver.page_source)
driver.quit()
```

```py
# Example 5 : 네이버 로그인 (캡챠 우회)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyperclip

def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장
    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(1)

driver = webdriver.Chrome("C:\Temporary\chromedriver.exe")
driver.get("https://www.google.com")

clipboard_input('//*[@id="id"]', "이곳에 ID를 입력하세요")
clipboard_input('//*[@id="pw"]', "이곳에 PW를 입력하세요")
driver.find_element_by_xpath('//*[@id="log.login"]').click()

print(driver.page_source)
driver.quit()        
```

```py
# Example 6 : CSV 파일로 저장 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('C:\Temporary\chromedriver.exe')
driver.get('https://oscar.go.com/winners')
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')

oscars_2020 = []
for item in zip(category, movie, producer):
    oscars_2020.append(
        {
            'category' : item[0].text,
            'movie'    : item[1].text,
            'producer' : item[2].text
        }
    )

data = pd.DataFrame(oscars_2020)
print(data)
data.to_csv('oscars_2020.csv')    
```


## 참고 
- [Beautiful Soup 로 크롤링 하기](https://l0o02.github.io/2018/06/09/python-crawling-1_copy0/)
- [Beautiful Soup 사용법 + 영화 리뷰 크롤링 (3/3)](https://ai-creator.tistory.com/201) 
- [Selenium 크롤러 - 네이버 자동 로그인](https://ai-creator.tistory.com/125)
- [Python Selenium으로 크롤링하기](https://velog.io/@swhybein/Python-Selenium%EC%9C%BC%EB%A1%9C-%ED%81%AC%EB%A1%A4%EB%A7%81%ED%95%98%EA%B8%B0)
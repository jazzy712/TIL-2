import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def crawl_toss_discussion(keyword):
    """
    토스증권에서 사용자가 입력한 종목 키워드로 종목을 검색하고,
    첫 번째 종목의 토론 탭에서 댓글 데이터를 크롤링한 후 파일로 저장합니다.
    """

# 크롬 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 ...")  # 사용자 에이전트 설정
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Toss 증권 접속
    driver.get("https://tossinvest.com/")
    time.sleep(2)
    print("1단계 성공")

    # 🔍 2. 돋보기(검색 버튼) 클릭 → 모달 열기
    # search_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="검색"]'))
    # )

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-section-name="검색"]'))
    )

    search_button.click()
    print("🔍 검색창 열기 성공")

    # 3. 검색 input 접근 및 키워드 입력
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input._1x1gpvi6'))
    )
    search_input.clear()
    search_input.send_keys(keyword)
    print("2단계 성공")
    time.sleep(2)


    # 3. 자동완성 리스트에서 첫 번째 종목 클릭
    first_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._1jnh59q0._1afau9j0[data-selected="true"]'))
    )
    first_result.click()
    print("3단계 성공")

    # 4. 커뮤니티 탭 클릭
    discussion_tab = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '커뮤니티')]"))
    )
    discussion_tab.click()
    time.sleep(3)

    # 5. 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 6. 댓글 크롤링
    comments = soup.select("div.css-1v0mbdj")  # 예시 클래스, 실제 구조 확인 필요
    results = []

    for c in comments:
        content = c.get_text().strip()
        if content:
            print("댓글:", content)
            results.append(content)

    # 7. 저장
    filename = f"{keyword}_discussion.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for i, comment in enumerate(results, 1):
            f.write(f"{i}. {comment}\n")

    print(f"✅ {len(results)}개의 댓글을 {filename}에 저장했습니다.")

except Exception as e:
    print("❌ 오류 발생:", e)

finally:
    driver.quit()
crawl_toss_discussion("삼성전자")
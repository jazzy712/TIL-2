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

        # 2. 돋보기(검색 버튼) 클릭 → 모달 열기

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-section-name="검색"]'))
        )

        search_button.click()
        print("🔍 검색창 열기 성공")

        # 2. 검색 input 접근 및 키워드 입력
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
        community_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='tab' and span[text()='커뮤니티']]"))
        )
        community_tab.click()
        print("4단계 성공 (커뮤니티 탭 클릭 완료)")
        time.sleep(3)

        # 5. 페이지 소스 가져오기
        soup = BeautifulSoup(driver.page_source, "html.parser")

        info_div = soup.select_one("div._1sivumi0 > div:nth-of-type(1)")

        if info_div:
            spans = info_div.find_all("span")
            if len(spans) >= 2:
                company_name = spans[0].get_text(strip=True)
                stock_code = spans[1].get_text(strip=True)
                print("종목명:", company_name)
                print("종목코드:", stock_code)
            else:
                print("❗ span이 부족합니다:", spans)
                company_name, stock_code = "정보 없음", "정보 없음"
        else:
            print("❗ 종목 정보 div를 못 찾았어요.")
            company_name, stock_code = "정보 없음", "정보 없음"

        # 6. 댓글 크롤링
        comments = soup.select("article.comment span[class*='_60z0ev1']") 
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

        print(company_name)
        print(stock_code)

    except Exception as e:
        print("❌ 오류 발생:", e)

    finally:
        driver.quit()

        return company_name, stock_code, results

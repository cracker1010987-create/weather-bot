from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def crawl_info():

    # =========================
    # Selenium 설정
    # =========================
    options = webdriver.ChromeOptions()

    # 브라우저 창 숨김
    options.add_argument("--headless=new")

    # 불필요한 로그 제거
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # =========================
    # 네이버 날씨 접속
    # =========================
    driver.get("https://weather.naver.com/")

    # 페이지 로딩 대기
    time.sleep(3)

    # =========================
    # 내일 오전 강수확률
    # =========================
    morning_rain = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_weather > span:nth-child(1) > strong > span.rainfall"
    ).text

    # =========================
    # 내일 오전 날씨
    # =========================
    morning_weather = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_weather > span:nth-child(1) > i"
    ).get_attribute("data-tooltip")

    # =========================
    # 내일 오후 날씨
    # =========================
    afternoon_weather = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_weather > span:nth-child(2) > i"
    ).get_attribute("data-tooltip")

    # =========================
    # 내일 오후 강수확률
    # =========================
    afternoon_rain = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_weather > span:nth-child(2) > strong > span.rainfall"
    ).text

    # =========================
    # 내일 최저기온
    # =========================
    lowest_temp = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_temperature > strong > span.lowest"
    ).text

    # =========================
    # 내일 최고기온
    # =========================
    highest_temp = driver.find_element(
        By.CSS_SELECTOR,
        "#cardWeekScroll > ul > li:nth-child(2) > div > div > div.cell_temperature > strong > span.highest"
    ).text

    # =========================
    # 문자열 정리
    # =========================
    morning_rain = morning_rain.replace("강수확률", "").strip()
    afternoon_rain = afternoon_rain.replace("강수확률", "").strip()

    lowest_temp = lowest_temp.replace("최저기온", "").strip()
    highest_temp = highest_temp.replace("최고기온", "").strip()

    # =========================
    # 브라우저 종료
    # =========================
    driver.quit()
    return morning_weather, morning_rain, afternoon_rain, afternoon_weather, lowest_temp, highest_temp
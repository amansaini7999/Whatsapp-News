def send_message(text, contact_list):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys

    import time
    from .config import CHROME_PROFILE_PATH

    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)

    driver = webdriver.Chrome("/home/aman/Downloads/chromedriver", options=options)
    driver.get("https://web.whatsapp.com")

    try:
        for contact in contact_list:
            search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
            search_box = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            search_box.clear()
            search_box.send_keys(contact)

            contact_xpath = f'//span[@title="{contact}"]'
            contact_title = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, contact_xpath))
            )
            contact_title.click()

            input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
            input_box = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            input_box.send_keys(text)
            input_box.send_keys(Keys.ENTER)

    finally:
        driver.quit()
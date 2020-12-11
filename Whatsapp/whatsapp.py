def send_message(message, pdf_loc, contact_list):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys

    import time
    import sys, os
    from .config import CHROME_PROFILE_PATH

    options = webdriver.ChromeOptions()
    #options.add_argument('--no-sandbox')
    #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")      #Heroku
    options.add_argument(CHROME_PROFILE_PATH)
    #options.add_argument("--headless")                                 #Heroku
    #options.add_argument("--window-size=1440, 900")
    #options.add_argument("Chrome/85.0.4183.121")
    #options.add_argument("--disable-dev-shm-usage")                    #Heroku

    #For Heroku
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)

    #For Local or EC2
    driver = webdriver.Chrome(options=options)    
    driver.get("https://web.whatsapp.com")
    
    try:
        for contact in contact_list:

            search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
            search_box = WebDriverWait(driver, 500).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )
            search_box.clear()
            search_box.send_keys(contact)

            contact_xpath = f'//span[@title="{contact}"]'
            contact_title = WebDriverWait(driver, 500).until(
                EC.presence_of_element_located((By.XPATH, contact_xpath))
            )
            contact_title.click()

            # Send Text
            input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
            input_box = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.XPATH, input_xpath))
            )
            input_box.send_keys(message)
            input_box.send_keys(Keys.ENTER)

            # Send Attachment
            attachment_xpath = '//span[@data-testid="clip"][@data-icon="clip"]'
            attachment_box = WebDriverWait(driver, 500).until(
                EC.presence_of_element_located((By.XPATH, attachment_xpath))
            )
            attachment_box.click()

            document_box = driver.find_element_by_xpath('//input[@accept="*"]')
            abs_pdf_loc = os.path.abspath('..') + "/" + pdf_loc + "dailyexcelsior.pdf"
            document_box.send_keys(abs_pdf_loc)

            time.sleep(3)
            send_btn = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
            send_btn.click()

            time.sleep(10)

    finally:
        driver.quit()
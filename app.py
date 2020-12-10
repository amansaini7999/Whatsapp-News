def job():
    import os
    import shutil
    from News.news import scrape
    from Whatsapp.whatsapp import send_message

    os.mkdir("News/temp")
    scrape()

    #text = "Hey, this message was sent using Selenium"
    contact_list = ["+91 60057 47938"]#, "Harish Tomar AIT"]
    pdf_loc = "Whatsapp News/News/temp/dailyexcelsior.pdf"
    send_message(pdf_loc, contact_list)
    shutil.rmtree("News/temp/", ignore_errors = False)

def schedule_job():
    import schedule
    import time
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    schedule_job()
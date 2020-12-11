def job():
    import os
    import shutil
    from News.news import scrape
    from Whatsapp.whatsapp import send_message

    os.mkdir("News/temp")
    scrape()
    
    contact_list = ["+91 60057 47938"]#, "Harish Tomar AIT"]
    pdf_loc = "Whatsapp News/News/temp/"
    send_message(pdf_loc, contact_list)
    shutil.rmtree("News/temp/", ignore_errors = False)

def schedule_job():
    import schedule
    import time
    job()
    '''schedule.every().minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(10)'''

if __name__ == "__main__":
    schedule_job()
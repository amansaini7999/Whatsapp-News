# from flask import Flask
# app = Flask(__name__)

def job():
    import os
    from News.news import scrape
    from Whatsapp.whatsapp import send_message

    os.mkdir("News/temp")
    scrape()

    #text = "Hey, this message was sent using Selenium"
    contact_list = ["+91 60057 47938"]#, "Harish Tomar AIT"]
    pdf_loc = "Whatsapp News/News/temp/dailyexcelsior.pdf"
    send_message(pdf_loc, contact_list)
    os.rmdir("News/temp/")

#@app.route('/')
'''def schedule():
    response = {}
    response["response"] = job()
    return response'''

if __name__ == "__main__":
    job()
#    app.run(debug=True)
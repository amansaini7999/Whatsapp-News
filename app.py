from flask import Flask, render_template
app = Flask(__name__)

def job():
    from News.news import scrape
    from Whatsapp.whatsapp import send_message

    text = "Hey, this message was sent using Selenium"
    contact_list = ["+91 60057 47938"]#, "Harish Tomar AIT"]

    scrape()

    send_message(text, contact_list)

    return 1

@app.route('/')
def schedule():
    response = {}
    response["response"] = job()
    return response

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "davidschaer7@gmail.com"
app.config["MAIL_PASSWORD"] = "saociizyyktuctsm"
app.config['MAIL_DEFAULT_SENDER'] = 'davidschaer7@gmail.com'
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True



mail = Mail()
mail.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/mywork')
def mywork():
    return render_template('mywork.html', title='My Work')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Gallery')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        msg = Message("Message from your website", sender=email, recipients=["davidschaer7@gmail.com"])
        msg.body = message
        mail.send(msg)
        return render_template('contact.html', success=1)

    return render_template('contact.html', title='Contact')



if __name__ == '__main__':
    app.run(debug=True)


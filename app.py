from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = "soujatya2003bhunia@gmail.com",
    MAIL_PASSWORD = "qsmfvfpipwafbsyr"
)

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/send_mail', methods=['POST'])
# def send_mail():
#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['details']

#     msg = Message('New Message from Contact Form',
#                   recipients=['recipient@example.com'])
#     msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

#     mail.send(msg)
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

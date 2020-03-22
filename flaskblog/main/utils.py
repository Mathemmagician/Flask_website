from flask_mail import Message
from flaskblog import mail


def send_contact_email(eemail, ttitle, bbody):

    msg = Message(f'RamilUS.com Contact: {ttitle}', recipients=["ramilraleskerov@gmail.com"])
    msg.body = f'From: {eemail}\n--------------------------------\n{bbody}'

    mail.send(msg)
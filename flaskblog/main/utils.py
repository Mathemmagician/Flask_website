from flask_mail import Message
from flaskblog import mail

import requests
from datetime import datetime
import json
from matplotlib.figure import Figure

def send_contact_email(eemail, ttitle, bbody):

    msg = Message(f'RamilUS.com Contact: {ttitle}', recipients=["ramilraleskerov@gmail.com"])
    msg.body = f'From: {eemail}\n--------------------------------\n{bbody}'

    mail.send(msg)


def get_codeforces_rating():
	r = requests.get("https://codeforces.com/api/user.rating?handle=RMILKA")
	parsed_data = json.loads(r.content)  # Skip old data
	if parsed_data['status'] == "OK":
		rating_history = []
		datestamps = []
		for p in parsed_data['result'][2:]:
			secs = p['ratingUpdateTimeSeconds']
			datestamps.append(datetime.fromtimestamp(secs).strftime("%b %d"))
			rating_history.append(p['newRating'])
		return (datestamps, rating_history)
	else:
		return -1


def create_figure(xs, ys):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(xs, ys, '^--', color='#ffa340')
    axis.grid()
    axis.set_title('Codeforces')
    axis.set_ylabel('Rating')
    axis.xaxis.set_tick_params(rotation=30)
    return fig
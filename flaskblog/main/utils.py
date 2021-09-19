from flask_mail import Message
from flaskblog import mail

import json
import requests
from datetime import datetime
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
	return -1


def get_lichess_rating():
	r = requests.get("https://lichess.org/api/user/BootsForCats/rating-history")
	r.raise_for_status()
	data = r.json()
	for chess_type in data:
		if chess_type['name'] == 'Blitz':
			rating_history = [point[-1] for point in chess_type['points']]
			datestamps = [datetime(year=point[0], month=point[1]+1, day=point[2]) for point in chess_type['points']]
			return (datestamps, rating_history)
	return -1


def create_figure(xs, ys, title, **kwargs):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(xs, ys, **kwargs)
    axis.grid()
    axis.set_title(title)
    axis.set_ylabel('Rating')
    axis.xaxis.set_tick_params(rotation=30)
    return fig
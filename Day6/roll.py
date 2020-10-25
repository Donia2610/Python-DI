import flask
import random

app = flask.Flask(__name__)

@app.route("/numbers/<int:num>")
def numbers(num):
	if num > 100 or num < 0:
		return f"{num} is out of range!"
	
	ran = random.randint(1,100)
	if ran == num: 
		return "Congrats! you guessed right!"
	else:
		return f"random number was {ran}, Try again!"
	
@app.route("/")
def index():
	return "Hello"

if __name__ == '__main__':
	app.run(debug=True)

import flask

app = flask.Flask("CV")

@app.route("/cv")
def index():
	return flask.render_template("cv.html")
	
app.run(debug=True)
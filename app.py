from flask import Flask, render_template

app = Flask("webapp")

@app.route("/")
def home():
	return render_template("base.html")


@app.route("/index/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()


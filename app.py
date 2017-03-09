from flask import Flask, render_template

app = Flask("webapp")

@app.route("/")
def home():
	return render_template("index.html")


@app.route("/contact/")
def index():
	return render_template("contact.html")

if __name__ == "__main__":
	app.run()


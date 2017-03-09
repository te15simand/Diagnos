from flask import Flask, render_template, request

app = Flask("webapp")

@app.route("/")
def home():
	return render_template("index.html")


@app.route("/contact/")
def index():
	return render_template("contact.html")

@app.route("/contact/sent/", methods=["GET", "POST"])
def sent():
	if request.method == "POST":
		return "Tack!"
	else:
		return render_template("sent.html")




if __name__ == "__main__":
	app.run(host="0.0.0.0")


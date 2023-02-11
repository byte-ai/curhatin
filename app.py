from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
	return render_template("index.html")	

@app.route("/predict", methods=["GET", "POST"])
def predict():
		# sentence = request.form["sentence"]		
	if request.method == "POST":
		sentence = request.form["sentence"]		
		return render_template("predict.html", data=sentence)	
	return render_template("predict.html")	

if __name__ == "__main__":
	app.run(debug=True)


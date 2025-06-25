from flask import *
app = Flask(__name__)

@app.route("/")
def _hello_world():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        message = request.form.to_dict()
        print(message)
        print(f"Received message: {message}")
        return f"You submitted: {message}"
    else:
        return render_template('login.html')

@app.route("/submit", methods=["POST"])
def submit():
    message = request.form["fname"]
    print(f"Received message: {message}")
    return f"You submitted: {message}"
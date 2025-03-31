from flask import Flask,render_template,request,redirect,url_for,sessions
import key_maker

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/WellTrack/Home")
def home():
    page_title = "Homepage"
    return render_template("home.html", title=page_title)

@app.route("/form", methods=["POST","GET"])
def form():
    if request.method == "POST":
        #process some user data
        return redirect(url_for("dashboard"))
    return render_template("form.html")

@app.route("/dashboard")
def dashboard():
    page_title= "WellTrack Dashboard"
    return render_template("dashboard",title=page_title)

app.secret_key = key_maker.secret_key
if __name__ == "__main__":
    app.run(debug=True)

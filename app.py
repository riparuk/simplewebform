from flask import Flask, redirect, request, render_template

app = Flask(__name__)

ACC = {
    "1":"a",
    "2":"b",
    "3":"c",
    "4":"d"
}

@app.route("/", methods=["POST","GET"])
def home():
    if(request.method == "GET"):
        return render_template("login.html", rm=request.method)
    elif(request.method == "POST"):
        user = request.form.get("user")
        passwd = request.form.get("pass")
        choice = request.form.get("choice")
        if user in ACC:
            if(passwd == ACC[user]):
                return render_template("login.html", user=user, auth=(passwd==(ACC[user])))
            else:
                return render_template("login.html", message="Wrong Password")
        else:
            return render_template("login.html", message="Wrong Username and Password")
from flask import Flask, redirect, request, render_template

app = Flask(__name__)

login={}
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
        if not choice:
            if user in ACC:
                if(passwd == ACC[user]):
                    login["user_id"]=user
                    login["password"]=passwd
                    print(login)
                    return render_template("form.html", user=user)
                else:
                    return render_template("login.html", message="Wrong Password")
            else:
                return render_template("login.html", message="Wrong Username and Password")
        else:
            login["choice"]=choice
            return "Thanks '%s' <br>your choice is %s"% (login["user_id"],login["choice"])
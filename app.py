from flask import Flask, redirect, request, render_template

app = Flask(__name__)

login={}
login["user_id"]=None
login["password"]=None
login["choice"]=None
ACC = {
    "1":"a",
    "2":"b",
    "3":"c",
    "4":"d"
}
Presiden = ("Jokowi", "Prabowo", "Anies", "Ganjar", "Megawati")
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
                login["user_id"]=user
                login["password"]=passwd
                print(login)
                return render_template("form.html", user=user, choices=Presiden)    
            else:
                return render_template("login.html", message="Wrong Password")
        elif (login["user_id"] in ACC) and (choice in Presiden):
            login["choice"]=choice
            return "Thanks id=%s <br>Your choice is %s"%(login["user_id"], login["choice"])
        elif choice not in Presiden:
            return "Something Error!"
        else:
            return render_template("login.html", message="Wrong Username and Password")
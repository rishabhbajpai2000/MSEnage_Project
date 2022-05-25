from flask import Flask, render_template,request
# from Functions import cars
# import pandas as pd
# from flask_mail import Mail

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if (request.method == "POST"):
        #  take the values from the form 
        cost = request.form.get('cost')
        brand = request.form.get('brand')
        milege = request.form.get('milege')
        type = request.form.get('type')
        seating = request.form.get('seating')
        print(cost, brand, milege, type, seating)       
        # issue: it loads whole page and does not goes to specific part of the page
        cars(cost,brand, milege, type, seating)


    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

app.run(debug=True)

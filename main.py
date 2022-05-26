from flask import Flask, render_template,request
from Functions import cars
import pandas as pd


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if (request.method == "POST"):
        #  take the values from the form 
        cost_min = request.form.get('cost_min')
        cost_max = request.form.get('cost_max')
        brand = request.form.get('brand')        
        mileage_min = request.form.get('mileage_min')
        mileage_max = request.form.get('mileage_max')
        type = request.form.get('type')
        seating = request.form.get('Seating_Cap')
        print(cost_max,cost_min, brand, mileage_min, mileage_max, type, seating)       
        # issue: it loads whole page and does not goes to specific part of the page
        # cars(cost,brand, milege, type, seating)
        


    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

if __name__=="__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from Functions import cars, test_data
import pandas as pd


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #  take the values from the form
        cost_min_i = int(request.form.get("cost_min"))
        cost_max_i = int(request.form.get("cost_max"))
        brand_i = request.form.get("brand")
        mileage_min_i = int(request.form.get("mileage_min"))
        mileage_max_i = int(request.form.get("mileage_max"))
        type_i = request.form.get("type")
        seating_i = int(request.form.get("Seating_Cap"))
        print(cost_max_i,cost_min_i, brand_i, mileage_min_i, mileage_max_i, type_i, seating_i)
        # issue: it loads whole page and does not goes to specific part of the page

        # cars_found = test_data
        cars_found = cars(
            cost_min=cost_min_i,
            cost_max=cost_max_i,
            brand=brand_i,
            mileage_min=mileage_min_i,
            mileage_max=mileage_max_i,
            p_d_cng=type_i,
            seating=seating_i,
        )
        
        inp_data = {
            "cost_min": "Price:" + str(cost_min_i),
            "cost_max": "Max:" + str(cost_max_i),
            "brand": brand_i,
            "mileage_min": "Mileage:" + str(mileage_min_i),
            "mileage_max": "Mileage:" + str(mileage_max_i),
            "type": type_i,
            "seating": seating_i,
        }
        print(cars_found)
        # issue: the data is not loading inside the model 
        return render_template("index.html", cars_found=cars_found, inp_data=inp_data)

    # issue: its not taking space in the price_min
    default_inp_data = {
        "cost_min": "Price Min",
        "cost_max": "Max",
        "brand": "Brand",
        "mileage_min": "Mileage_Min",
        "mileage_max": "Max",
        "type": "Petrol/CNG/Diesel",
        "Seating_Cap": "Seating Capacity",
    }
    # issue: change defualt cars data
    default_cars = test_data

    return render_template(
        "index.html", cars_found=default_cars, inp_data=default_inp_data
    )


# @app.route("/findcar/string:<post_slug>", methods= ["GET", "POST"])
# def find_car(post_slug):
#     inp_data= post_slug
#     cars_found = cars(cost_max,cost_min, brand, mileage_min, mileage_max, type, seating)
#     return render_template("findcar.html", cars_found=cars_found, inp_data= inp_data)


@app.route("/blog")
def blog():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run(debug=True)

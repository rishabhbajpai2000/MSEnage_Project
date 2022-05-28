from flask import Flask, render_template, request
from Functions import cars, top_cars

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        #  take the values from the form
        cost_min_i = request.form.get("cost_min")
        cost_max_i = request.form.get("cost_max")
        brand_i = request.form.get("brand")
        mileage_min_i = request.form.get("mileage_min")
        mileage_max_i = request.form.get("mileage_max")
        type_i = request.form.get("type")
        seating_i = request.form.get("Seating_Cap")
        print(
            cost_max_i,
            cost_min_i,
            brand_i,
            mileage_min_i,
            mileage_max_i,
            type_i,
            seating_i,
        )

        cars_searched = cars(
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
        if (cars_searched == "none"):
            cars_line = "We were not able to find a car that meets your expectations, but here are our best cars if you want."
            return render_template("index.html",inp_data= inp_data, cars_line = cars_line, cars_found = top_cars, count = len(cars_searched))

        if (type(cars_searched) == str):
            return render_template("index.html", cars_line = cars_searched, inp_data= inp_data, count = 0 )
        print(cars_searched)
        
        cars_line = "Based on your choices, our car recemmendations are"
        return render_template(
            "index.html", cars_found=cars_searched, inp_data=inp_data, cars_line=cars_line, count = len(cars_searched)
        )

    # issue: its not taking space in the price_min
    default_inp_data = {
        "cost_min": "Min",
        "cost_max": "Max",
        "brand": "Brand",
        "mileage_min": "Min",
        "mileage_max": "Max",
        "type": "Petrol/CNG/Diesel",
        "Seating_Cap": "Seating Capacity",
    }
    # issue: change defualt cars data
    default_cars = top_cars
    cars_line = "Our top 5 models from the collection"

    return render_template(
        "index.html",
        cars_found=default_cars,
        inp_data=default_inp_data,
        cars_line=cars_line,
        count=5
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

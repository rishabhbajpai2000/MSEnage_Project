from flask import Flask, render_template, request
from Functions import cars, top_cars

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    # if statement will be activated when user presses the submit button on form 
    if request.method == "POST":
        #  take the values from the form
        cost_min_i = request.form.get("cost_min")
        cost_max_i = request.form.get("cost_max")
        brand_i = request.form.get("brand")
        mileage_min_i = request.form.get("mileage_min")
        mileage_max_i = request.form.get("mileage_max")
        type_i = request.form.get("type")
        seating_i = request.form.get("Seating_Cap")

        # cars function gives the cars recemmendation 
        cars_searched = cars(
            cost_min=cost_min_i,
            cost_max=cost_max_i,
            brand=brand_i,
            mileage_min=mileage_min_i,
            mileage_max=mileage_max_i,
            p_d_cng=type_i,
            seating=seating_i,
        )
        
        # we have stored the data which was inserted into the previous session with input data
        inp_data = {
            "cost_min": "Price:" + str(cost_min_i),
            "cost_max": "Max:" + str(cost_max_i),
            "brand": brand_i,
            "mileage_min": "Mileage:" + str(mileage_min_i),
            "mileage_max": "Mileage:" + str(mileage_max_i),
            "type": type_i,
            "seating": seating_i,
        }
        # if the data frame returns 1, i.e no car is found in the database
        if (type(cars_searched) == int):
            if (cars_searched == 1):
                cars_line = "We were not able to find a car that meets your expectations, but here are our best cars if you want."
                return render_template("index.html",inp_data= inp_data, cars_line = cars_line, cars_found = top_cars, count = 5)

        # if there is some error in the data entered then function returns a error string 
        if (type(cars_searched) == str):
            return render_template("index.html", cars_line = cars_searched, inp_data= inp_data, count = 0 )
        print(cars_searched)
        
        cars_line = "Based on your choices, our car recemmendations are"
        return render_template(
            "index.html", cars_found=cars_searched, inp_data=inp_data, cars_line=cars_line, count = len(cars_searched)
        )

    # default case is entertained here 
    default_inp_data = {
        "cost_min": "Min",
        "cost_max": "Max",
        "brand": "Brand",
        "mileage_min": "Min",
        "mileage_max": "Max",
        "type": "Petrol/CNG/Diesel",
        "Seating_Cap": "Seating Capacity",
    }
    default_cars = top_cars
    cars_line = "Our top 5 models from the collection"

    return render_template(
        "index.html",
        cars_found=default_cars,
        inp_data=default_inp_data,
        cars_line=cars_line,
        count=5
    )



if __name__ == "__main__":
    app.run(debug=True)

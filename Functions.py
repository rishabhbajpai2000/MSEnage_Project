# find car function
# reading the file
import pandas as pd
main_data = pd.read_csv("Data.csv")

# cleaning the data
# making the values of the as float from intger.  
main_data["ARAI_Certified_Mileage_kmpl"].astype(float)
# removing the duplicates based on the rows
main_data = main_data.drop_duplicates(subset="Model")


test_data = main_data.head()
#writing the main function
def cars(cost_min, cost_max, brand, mileage_min, mileage_max, p_d_cng, seating, data=main_data):
    filter_p = data[data["Ex-Showroom_Price"].isin(range(cost_min,cost_max))]
    filter_b_p = filter_p[filter_p["Make"] == brand]
    filter_b_p_t = filter_b_p[filter_b_p["Fuel_Type"]  == p_d_cng]
    filter_b_m_p_t = filter_b_p_t[filter_b_p_t["ARAI_Certified_Mileage_kmpl"].isin(range(mileage_min, mileage_max))]
    filter_b_m_p_s_t = filter_b_m_p_t[filter_b_m_p_t["Seating_Capacity"] == seating]
    return filter_b_m_p_s_t.sort_values("Ex-Showroom_Price").head() 



# simple comment
# random commit from g cloud

# def car_found_desc(data):
    # this fuction will take the output 5 rows data frame to generate a text description of it
    # input: 5 row pandas dataframw
    # output: an array of len 5, where ith index will contain description of ith car, in around 70 words


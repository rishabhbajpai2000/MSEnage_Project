# # find car function
# # reading the file
# import pandas as pd
# main_data = pd.read_csv("Data.csv")

# # cleaning the data
# # making the values of the as float from intger.  
# main_data["ARAI_Certified_Mileage_kmpl"].astype(float)


# #writing the main function
# def cars(cost, brand, milege, p_d_cng, seating, data=main_data):
#     filter_p = data[data["Ex-Showroom_Price"].isin(range(cost[0],cost[1]))]
#     filter_b_p = filter_p[filter_p["Make"] == brand]
#     filter_b_p_t = filter_b_p[filter_b_p["Fuel_Type"]  == p_d_cng]
#     filter_b_m_p_t = filter_b_p_t[filter_b_p_t["ARAI_Certified_Mileage_kmpl"].isin(range(milege[0], milege[1]))]
#     filter_b_m_p_s_t = filter_b_m_p_t[filter_b_m_p_t["Seating"] == seating]
#     filter_b_m_p_s_t.sort_values("Ex-Showroom_Price").head()
#     return filter_b_m_p_s_t 


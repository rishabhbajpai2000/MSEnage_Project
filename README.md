
# Table of Contents
- [Table of Contents](#table-of-contents)
- [CarNow](#carnow)
- [Time-Line (Three weeks)](#time-line-three-weeks)
  - [1. First Week](#1-first-week)
  - [2. Second Week](#2-second-week)
  - [3. Third week](#3-third-week)
- [Features](#features)
- [How to run the project locally?](#how-to-run-the-project-locally)

# CarNow 
 - It is a car recemmendation system system which recemmends the best cars available in the data when requirements are given.
 - This project was developed in Microsoft Engage program, within a given span of 21 days





# Time-Line (Three weeks)
## 1. First Week
 - Learnt HTML
 - CSS
 - Flask


## 2. Second Week
 - Learnt about Data Analytics with Python with various libraires 
 - Pandas, Numpy, Scikitlearn etc


## 3. Third week 
 - Wrote the front of the website, i.e HTML and CSS
 - Developed the back end recemmendation system
 - Connected the backed function with front end with help of flask 
 - Hosted the website on Google cloud


# Features
 - The project is hosted on [google cloud.](https://flask-app-cars.el.r.appspot.com/)
 - It has a minimalistic landing page
  
 - It shows the list of top five cars available in the collection by defult
 - Once the requirements form is filled the list updates with the cars that meet upto the demands

 -  It is also able to handle the edge cases when the form is filled empty

 -  Or when there are no cars which meets the requirements of the user
 
 - The system also generates a description of each car that comes out of the database. 



# How to run the project locally?

1. Clone this repository in your system with the command below in your terminal.
    `git clone https://github.com/rishabhbajpai2000/MSEnage_Project.git`
2. Move into the folder where the data is
3. In your terminal install virtualenv with 
   `pip install viertualenv`
4. The make an environment with 
   `virtualenv env`
5. activate the environment with going into the environment with 
   `.\env\Scripts\activate.ps1`
6. Now run the command to install the dependencies listed within requirements.txt folder
   `pip install -r requirements.txt`
7. once the dependencies are installed you need to run
   `python main.py`
   to the run code on your local server

   You can also watch this [video demo](https://youtu.be/zQIXy-9lV18)(2x speed can work as well) to see the steps to run the project locally
   

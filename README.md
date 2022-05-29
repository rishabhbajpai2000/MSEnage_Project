
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
 - Project demo [video](https://www.youtube.com/watch?v=E29g5AlZ4nM)





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
 <img width="952" alt="image" src="https://user-images.githubusercontent.com/64163517/170878115-9b180672-d655-4d8e-b516-c3661a889698.png">

  
 - It shows the list of top five cars available in the collection by defult
 <img width="873" alt="image" src="https://user-images.githubusercontent.com/64163517/170878128-c6739876-f7d7-4050-aa8e-294e5b7b35d2.png">

 - Once the requirements form is filled the list updates with the cars that meet upto the demands
 <img width="886" alt="image" src="https://user-images.githubusercontent.com/64163517/170878213-ce106be7-7572-43b9-b38b-26e3295413b9.png">


 -  It is also able to handle the edge cases when the form is filled empty
 <img width="925" alt="image" src="https://user-images.githubusercontent.com/64163517/170878227-6fec4872-1377-49db-863f-ed9a8becb2ed.png">


   -  Or when there are no cars which meets the requirements of the user
   <img width="872" alt="image" src="https://user-images.githubusercontent.com/64163517/170878254-8d704136-0c11-484a-94aa-74934192e440.png">


   - The system also generates a description of each car that comes out of the database. 

<img width="556" alt="image" src="https://user-images.githubusercontent.com/64163517/170878271-54fb31a4-62d0-4927-83e4-dbdf31512b3b.png">



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
   

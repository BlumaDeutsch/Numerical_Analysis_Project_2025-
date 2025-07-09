Numerical Analysis Project 2025


This repository contains implementations of numerical analysis algorithms learned in the Numerical Analysis course.
The project demonstrates interpolation methods, root-finding methods, and graphical representations of each method via a Python Flask/FastAPI server and a React client.


Implemented Methods:

 Interpolation Methods

   Linear Interpolation

   Polynomial Interpolation

   Lagrange Interpolation

   Neville Interpolation

   Cubic Spline Interpolation

 Root Finding Methods

   Bisection Method

   Newton-Raphson Method

   Secant Method

   
Project Structure

analiza_lib/     # Core numerical methods library

server/          # API server built with FastAPI

client/          # Frontend React client (optional GUI)


Installation Instructions:

1. Clone the repository
 git clone https://github.com/sara21379/Numerical_Analysis_Project_2025-.git

2.Navigate to the project directory
 cd Numerical_Analysis_Project_2025-

3.Install Python dependencies
 pip install -r requirements.txt

4.Navigate to the server folder and run the server
 cd server
uvicorn api:app --reload

5.Navigate to the client folder and run the client

 cd ../client

 npm install

 npm start


How to Use:

Open Postman or your browser to test API endpoints (e.g., http://127.0.0.1:8000).

Use each endpoint to send x and y values and receive plotted graphs.

The React client (if run) provides a visual interface to call the APIs.


Project Purpose

This project aims to:

Implement and practice numerical analysis algorithms.

Develop clean, modular Python code for engineering applications.

Practice client-server architecture for computational tools.


Languages & Tools:

Python (FastAPI, Matplotlib, Numpy)

JavaScript (React.js)

Postman for API testing

Git & GitHub for version control


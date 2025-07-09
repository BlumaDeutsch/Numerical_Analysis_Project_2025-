#  Numerical Analysis Project 2025
###  **Project Description**


This project implements numerical analysis methods learned in the course, including:
- **Interpolation:** linear, polynomial, Lagrange, Neville, cubic spline
- **Root Finding:** bisection, Newton-Raphson, secant
- **Graph plotting** for each method

### **Project Structure**
Numerical_Analysis_Project_2025-
├── analiza_lib # Functions library
├── server # Backend API (FastAPI)
├── client # Frontend (React)
└── README.md

###  **Installation & Running Instructions**
####  **Clone the repository**

git clone https://github.com/sara21379/Numerical_Analysis_Project_2025-.git
cd Numerical_Analysis_Project_2025-

Run the server (API)
 Navigate to the server folder:
cd server
 Create a virtual environment (recommended):
python -m venv venv
Activate the environment:
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
Install dependencies:
pip install fastapi uvicorn matplotlib numpy
Run the server:
uvicorn api:app --reload
The server runs at:
http://127.0.0.1:3000
### **How to Use**
Run both the server and client as described above.
Open http://localhost:8000 in your browser.
Select the desired method, enter input values, and view the calculated results with graphs.
###  **Prerequisites:**
Python 3.8+
npm installed
git installed

### **What Did We Implement?**
Full implementation of all listed numerical methods.
Graph generation for each method.
FastAPI server with POST requests for each function.
React client for user-friendly interaction.

### **Project Purpose**
This project aims to:

Implement and practice numerical analysis algorithms.
Develop clean, modular Python code for engineering applications.
Practice client-server architecture for computational tools.


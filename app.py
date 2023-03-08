import db
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.post("/employee_signup")
def employee_signup():
    data = request.get_json()
    # TODO: add check box in frontend to determine if manager or staff
    if (data["employee_type"] == "manager"):
        db.insert_new_manager(data["name"], data["salary"], data["password"], data["startDate"], data["jobTitle"])
        return redirect("/") # placeholder redirect after successful account creation
    elif data["employee_type"] == "staff":
        db.insert_new_staff(data["name"], data["salary"], data["password"], data["startDate"], data["jobTitle"])
        return redirect("/")

    return render_template("employee_signup.html", error="Unable to create new employee.") # place holder

@app.post("/customer_signup")
def customer_signup():
    data = request.get_json()
    db.insert_new_customer(data["name"], data["password"], data["email"], data["phoneNum"], data["street"], data["city"], data["state"], data["zip"])

@app.get("/aboutus")
def get_about_us():
    return render_template("about.html") # place holder

@app.get("/faq")
def get_faq():
    return render_template("faq.html") # place holder

@app.get("/user/employee/<eid>")
def get_employee_page():
    pass

@app.get("/user/customer/<cid>")
def get_customer_page():
    pass

@app.get("/products/")
def get_product_page():
    pass



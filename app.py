from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "ems_secret_key_2026")

# ── Database Connection ──────────────────────────────────────
def get_db():
    return mysql.connector.connect(
        host="mysql.railway.internal",
        user="root",
        password="syKyETjtreedYyzvfkbBtjzchkJdiktv",
        database="railway",
        port=3306
    )
# ── Login Required ───────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# ── LOGIN ────────────────────────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin123":
            session["user"] = username
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password!"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ── HOME ─────────────────────────────────────────────────────
@app.route("/")
@login_required
def home():
    return render_template("index.html")

# ── CUSTOMERS ────────────────────────────────────────────────
@app.route("/customers")
@login_required
def customers():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("customers.html", customers=data)

# ── ADD CUSTOMER ─────────────────────────────────────────────
@app.route("/add-customer", methods=["GET", "POST"])
@login_required
def add_customer():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO customer (FullName, Email, Phone, Address)
            VALUES (%s, %s, %s, %s)
        """, (
            request.form["fullname"],
            request.form["email"],
            request.form["phone"],
            request.form["address"]
        ))
        db.commit()
        cursor.close(); db.close()
        return redirect(url_for("customers"))
    return render_template("add_customer.html")

# ── EDIT CUSTOMER ─────────────────────────────────────────────
@app.route("/edit-customer/<int:id>", methods=["GET", "POST"])
@login_required
def edit_customer(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        cursor.execute("""
            UPDATE customer
            SET FullName=%s, Email=%s, Phone=%s, Address=%s
            WHERE CustomerID=%s
        """, (
            request.form["fullname"],
            request.form["email"],
            request.form["phone"],
            request.form["address"],
            id
        ))
        db.commit()
        cursor.close(); db.close()
        return redirect(url_for("customers"))
    cursor.execute("SELECT * FROM customer WHERE CustomerID=%s", (id,))
    customer = cursor.fetchone()
    cursor.close(); db.close()
    return render_template("edit_customer.html", customer=customer)

# ── DELETE CUSTOMER ───────────────────────────────────────────
@app.route("/delete-customer/<int:id>")
@login_required
def delete_customer(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM customer WHERE CustomerID=%s", (id,))
    db.commit()
    cursor.close(); db.close()
    return redirect(url_for("customers"))

# ── EVENTS ────────────────────────────────────────────────────
@app.route("/events")
@login_required
def events():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM event")
    data = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("events.html", events=data)

# ── BOOKINGS ──────────────────────────────────────────────────
@app.route("/bookings")
@login_required
def bookings():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT b.BookingID, c.FullName, e.EventName,
               b.BookingDate, b.Status, b.TotalAmount
        FROM booking b
        JOIN customer c ON b.CustomerID = c.CustomerID
        JOIN event e ON b.EventID = e.EventID
    """)
    data = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("bookings.html", bookings=data)

# ── PAYMENTS ──────────────────────────────────────────────────
@app.route("/payments")
@login_required
def payments():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.PaymentID, c.FullName, p.Amount,
               p.PaymentDate, p.Method, p.PaymentStatus
        FROM payment p
        JOIN booking b ON p.BookingID = b.BookingID
        JOIN customer c ON b.CustomerID = c.CustomerID
    """)
    data = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("payments.html", payments=data)

# ── SERVICES ──────────────────────────────────────────────────
@app.route("/services")
@login_required
def services():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM service")
    data = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("services.html", services=data)

# ── ADD BOOKING ───────────────────────────────────────────────
@app.route("/add-booking", methods=["GET", "POST"])
@login_required
def add_booking():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        cursor.execute("""
            INSERT INTO booking (CustomerID, EventID, Status, TotalAmount)
            VALUES (%s, %s, 'Pending', %s)
        """, (
            request.form["customer_id"],
            request.form["event_id"],
            request.form["total_amount"]
        ))
        db.commit()
        cursor.close(); db.close()
        return redirect(url_for("bookings"))
    cursor.execute("SELECT CustomerID, FullName FROM customer")
    customers = cursor.fetchall()
    cursor.execute("SELECT EventID, EventName FROM event")
    events = cursor.fetchall()
    cursor.close(); db.close()
    return render_template("add_booking.html",
                           customers=customers, events=events)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)))

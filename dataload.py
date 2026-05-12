import mysql.connector
import csv
import os

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",  # ← Change this to your MySQL password
    database="event_management"
)
cursor = conn.cursor()

# Path to your CSV files
csv_path = "csv/"

# ── 1. LOAD CUSTOMER ────────────────────────────────────────
with open(csv_path + "customer.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO customer
            (CustomerID, FullName, Email, Phone, Address, RegisteredAt)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["CustomerID"], row["FullName"], row["Email"],
            row["Phone"], row["Address"], row["RegisteredAt"]
        ))
conn.commit()
print("✅ customer loaded:", cursor.rowcount, "rows")

# ── 2. LOAD EVENT ────────────────────────────────────────────
with open(csv_path + "event.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO event
            (EventID, EventName, EventType, EventDate,
             Venue, Capacity, Description)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["EventID"], row["EventName"], row["EventType"],
            row["EventDate"], row["Venue"], row["Capacity"],
            row["Description"]
        ))
conn.commit()
print("✅ event loaded:", cursor.rowcount, "rows")

# ── 3. LOAD SERVICE ──────────────────────────────────────────
with open(csv_path + "service.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO service
            (ServiceID, ServiceName, Category, Cost,
             Description, IsAvailable)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["ServiceID"], row["ServiceName"], row["Category"],
            row["Cost"], row["Description"], row["IsAvailable"]
        ))
conn.commit()
print("✅ service loaded:", cursor.rowcount, "rows")

# ── 4. LOAD BOOKING ──────────────────────────────────────────
with open(csv_path + "booking.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO booking
            (BookingID, CustomerID, EventID, BookingDate,
             Status, TotalAmount)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["BookingID"], row["CustomerID"], row["EventID"],
            row["BookingDate"], row["Status"], row["TotalAmount"]
        ))
conn.commit()
print("✅ booking loaded:", cursor.rowcount, "rows")

# ── 5. LOAD PAYMENT ──────────────────────────────────────────
with open(csv_path + "payment.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO payment
            (PaymentID, BookingID, Amount, PaymentDate,
             Method, PaymentStatus)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["PaymentID"], row["BookingID"], row["Amount"],
            row["PaymentDate"], row["Method"], row["PaymentStatus"]
        ))
conn.commit()
print("✅ payment loaded:", cursor.rowcount, "rows")

# ── 6. LOAD EVENT_SERVICE ────────────────────────────────────
with open(csv_path + "event_service.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT IGNORE INTO event_service
            (EventID, ServiceID, Quantity, Notes)
            VALUES (%s, %s, %s, %s)
        """, (
            row["EventID"], row["ServiceID"],
            row["Quantity"], row["Notes"]
        ))
conn.commit()
print("✅ event_service loaded:", cursor.rowcount, "rows")

# ── CLOSE CONNECTION ─────────────────────────────────────────
cursor.close()
conn.close()
print("\n🎉 All data loaded successfully into event_management!")
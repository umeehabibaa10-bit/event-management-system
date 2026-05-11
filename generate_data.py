import csv
import os
import random
from faker import Faker
from datetime import date, timedelta

fake = Faker()

# Create csv folder if it doesn't exist
os.makedirs("csv", exist_ok=True)

# ── 1. CUSTOMER ──────────────────────────────────────────
customers = []
for i in range(1, 101):
    customers.append({
        "CustomerID": i,
        "FullName": fake.name(),
        "Email": fake.unique.email(),
        "Phone": fake.numerify("03#########"),
        "Address": fake.address().replace("\n", ", "),
        "RegisteredAt": fake.date_between(
                            start_date=date(2023, 1, 1),
                            end_date=date(2025, 12, 31))
    })

with open("csv/customer.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=customers[0].keys())
    writer.writeheader()
    writer.writerows(customers)
print("✅ customer.csv created")

# ── 2. EVENT ─────────────────────────────────────────────
event_types = ["Wedding", "Corporate", "Conference",
               "Private Party", "Birthday", "Seminar"]
venues = [
    "Pearl Continental Karachi", "Marriott Hotel Karachi",
    "Mohatta Palace", "Arts Council Karachi",
    "Beach Luxury Hotel", "Avari Towers",
    "Port Grand", "Karachi Expo Centre",
    "PC Hotel Lahore", "Serena Hotel Islamabad"
]

events = []
for i in range(1, 101):
    events.append({
        "EventID": i,
        "EventName": fake.catch_phrase(),
        "EventType": random.choice(event_types),
        "EventDate": fake.date_between(
                        start_date=date(2024, 1, 1),
                        end_date=date(2026, 12, 31)),
        "Venue": random.choice(venues),
        "Capacity": random.randint(50, 500),
        "Description": fake.sentence(nb_words=12)
    })

with open("csv/event.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=events[0].keys())
    writer.writeheader()
    writer.writerows(events)
print("✅ event.csv created")

# ── 3. BOOKING ───────────────────────────────────────────
statuses = ["Pending", "Confirmed", "Cancelled"]

bookings = []
for i in range(1, 101):
    bookings.append({
        "BookingID": i,
        "CustomerID": random.randint(1, 100),
        "EventID": random.randint(1, 100),
        "BookingDate": fake.date_between(
                          start_date=date(2024, 1, 1),
                          end_date=date(2025, 12, 31)),
        "Status": random.choice(statuses),
        "TotalAmount": round(random.uniform(5000, 500000), 2)
    })

with open("csv/booking.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=bookings[0].keys())
    writer.writeheader()
    writer.writerows(bookings)
print("✅ booking.csv created")

# ── 4. PAYMENT ───────────────────────────────────────────
methods = ["Cash", "Card", "Bank Transfer"]
pay_statuses = ["Paid", "Pending", "Refunded"]

payments = []
for i in range(1, 101):
    payments.append({
        "PaymentID": i,
        "BookingID": i,  # 1:1 relationship with booking
        "Amount": round(random.uniform(5000, 500000), 2),
        "PaymentDate": fake.date_between(
                          start_date=date(2024, 1, 1),
                          end_date=date(2025, 12, 31)),
        "Method": random.choice(methods),
        "PaymentStatus": random.choice(pay_statuses)
    })

with open("csv/payment.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=payments[0].keys())
    writer.writeheader()
    writer.writerows(payments)
print("✅ payment.csv created")

# ── 5. SERVICE ───────────────────────────────────────────
service_data = [
    ("Catering Standard",    "Catering",     15000),
    ("Catering Premium",     "Catering",     35000),
    ("Floral Decoration",    "Decor",        20000),
    ("Stage Setup",          "Decor",        45000),
    ("Photography Basic",    "Photography",  25000),
    ("Photography Premium",  "Photography",  60000),
    ("Videography",          "Videography",  50000),
    ("Sound System",         "Audio/Visual", 18000),
    ("Projector & Screen",   "Audio/Visual", 12000),
    ("Lighting Setup",       "Audio/Visual", 22000),
    ("Security Staff",       "Security",     10000),
    ("Valet Parking",        "Logistics",     8000),
    ("Guest Transport",      "Logistics",    30000),
    ("MC / Host",            "Entertainment",20000),
    ("Live Band",            "Entertainment",55000),
    ("DJ Services",          "Entertainment",25000),
    ("Invitation Cards",     "Stationery",    5000),
    ("Cake & Desserts",      "Catering",     12000),
    ("Tent & Furniture",     "Logistics",    40000),
    ("Bridal Makeup",        "Beauty",       18000),
]

services = []
for i, (name, category, cost) in enumerate(service_data, start=1):
    services.append({
        "ServiceID": i,
        "ServiceName": name,
        "Category": category,
        "Cost": cost,
        "Description": fake.sentence(nb_words=10),
        "IsAvailable": random.choice([True, True, True, False])
    })

with open("csv/service.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=services[0].keys())
    writer.writeheader()
    writer.writerows(services)
print("✅ service.csv created")

# ── 6. EVENT_SERVICE ─────────────────────────────────────
event_service_pairs = set()
event_services = []

while len(event_services) < 100:
    eid = random.randint(1, 100)
    sid = random.randint(1, 20)
    if (eid, sid) not in event_service_pairs:
        event_service_pairs.add((eid, sid))
        event_services.append({
            "EventID": eid,
            "ServiceID": sid,
            "Quantity": random.randint(1, 5),
            "Notes": fake.sentence(nb_words=8)
        })

with open("csv/event_service.csv", "w", newline="",
          encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=event_services[0].keys())
    writer.writeheader()
    writer.writerows(event_services)
print("✅ event_service.csv created")

print("\n🎉 All 6 CSV files generated in the csv/ folder!")

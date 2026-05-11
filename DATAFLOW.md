# Dataflow Description
## Event Management System — Database Lab Project
**Prepared by:** Ume Habiba
**Course:** Database Lab | BCS 4th Semester, Group-A
**Instructor:** Mr. Ali Hassan
**Milestone:** M3 — Dataset Preprocessing & Dataflow

---

## 1. What is a Dataflow?
A dataflow describes where data enters the system, how it moves
through the database tables, which tables depend on others, and
what comes out at the end.

---

## 2. Where Data Enters the System

Data enters the Event Management System through three entry points:

**Entry Point 1 — Customer Registration**
A new customer fills in their details (name, email, phone, address).
This creates a new row in the `customer` table.

**Entry Point 2 — Event Creation**
An admin or organizer creates a new event by entering the event
name, type, date, venue, capacity, and description.
This creates a new row in the `event` table.

**Entry Point 3 — Service Setup**
An admin adds available services (catering, decor, photography etc.)
to the system with their cost and availability status.
This creates a new row in the `service` table.

---

## 3. How Data Moves Through the System

The data flows through the system in the following order:

### Step 1 — Customer Registers
- Data enters: `customer` table
- A unique `CustomerID` is assigned automatically

### Step 2 — Customer Browses Events
- Data is read from: `event` table
- No new data is written at this step

### Step 3 — Customer Creates a Booking
- Data enters: `booking` table
- `booking` depends on BOTH `customer` and `event`
- `CustomerID` (FK) links to `customer` table
- `EventID` (FK) links to `event` table
- A unique `BookingID` is assigned automatically
- Booking `Status` is set to **Pending** by default

### Step 4 — Services Are Attached to the Event
- Data enters: `event_service` table (junction table)
- `EventID` (FK) links to `event` table
- `ServiceID` (FK) links to `service` table
- `Quantity` and `Notes` are recorded for each pairing
- This step resolves the Many-to-Many relationship
  between events and services

### Step 5 — Customer Makes a Payment
- Data enters: `payment` table
- `payment` depends on `booking`
- `BookingID` (FK) links to `booking` table
- Payment `Method`, `Amount`, and `PaymentStatus` are recorded
- Once payment is confirmed, `booking.Status` is updated
  from **Pending** to **Confirmed**

---

## 4. Data Dependency Order

The tables must be populated in this exact order due to
foreign key dependencies:
---

## 5. What Comes Out of the System

The system produces the following outputs:

| Output | Tables Used | Description |
|---|---|---|
| Customer booking history | customer + booking | All bookings made by a customer |
| Event attendee list | event + booking + customer | All customers booked for an event |
| Payment report | payment + booking | Total payments collected |
| Event service summary | event + event_service + service | Services attached to each event |
| Pending bookings report | booking + payment | Bookings not yet paid |
| Revenue by event type | event + booking + payment | Total revenue per event category |

---

## 6. Dataflow Diagram (Text Format)
---

## 7. Summary

The EMS database follows a strict sequential dataflow:
Customers and Events are created independently first.
Bookings then link Customers to Events.
Services are attached to Events through the junction table.
Finally, Payments are recorded against each Booking.
This ensures referential integrity is maintained at every
step of the process.
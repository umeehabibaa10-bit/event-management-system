# Normalization Document
## Event Management System — Database Lab Project
**Prepared by:** Ume Habiba
**Course:** Database Lab | BCS 4th Semester, Group-A
**Instructor:** Mr. Ali Hassan
**Milestone:** M2 — ERD Design & Normalization

---

## What is Normalization?
Normalization is the process of organizing a relational database to reduce
redundancy and ensure data integrity. It is applied in sequential stages
called Normal Forms (1NF, 2NF, 3NF). Each stage builds on the previous one.

---

## Table 1 — customer

| Column | Type |
|---|---|
| CustomerID (PK) | INT |
| FullName | VARCHAR(100) |
| Email | VARCHAR(150) |
| Phone | VARCHAR(20) |
| Address | TEXT |
| RegisteredAt | DATE |

### 1NF
Every column in the customer table holds a single, atomic value.
FullName stores one name, Email stores one address, and Phone stores
one number. There are no repeating groups or multi-valued attributes.
**Result: Already in 1NF. No changes needed.**

### 2NF
The primary key is CustomerID, which is a single column (not composite).
Since 2NF only applies when there is a composite primary key, partial
dependency cannot exist here. Every non-key column (FullName, Email,
Phone, Address, RegisteredAt) fully depends on CustomerID alone.
**Result: Already in 2NF. No changes needed.**

### 3NF
No transitive dependencies exist. Email does not determine Phone,
and Phone does not determine Address. Each column describes
the customer directly and independently through CustomerID.
**Result: Already in 3NF. No changes needed.**

---

## Table 2 — event

| Column | Type |
|---|---|
| EventID (PK) | INT |
| EventName | VARCHAR(150) |
| EventType | VARCHAR(80) |
| EventDate | DATE |
| Venue | VARCHAR(200) |
| Capacity | INT |
| Description | TEXT |

### 1NF
All columns contain single atomic values. EventType holds one
category value per row, and EventDate holds one date. No lists
or repeating groups are present.
**Result: Already in 1NF. No changes needed.**

### 2NF
The primary key is EventID, a single column. All non-key columns
fully depend on EventID. There is no partial dependency possible
with a single-column primary key.
**Result: Already in 2NF. No changes needed.**

### 3NF
No column depends on another non-key column. Venue does not
determine Capacity, and EventType does not determine EventDate.
Every column independently describes the event through EventID.
**Result: Already in 3NF. No changes needed.**

---

## Table 3 — booking

| Column | Type |
|---|---|
| BookingID (PK) | INT |
| CustomerID (FK) | INT |
| EventID (FK) | INT |
| BookingDate | DATE |
| Status | ENUM |
| TotalAmount | DECIMAL |

### 1NF
All columns hold single atomic values. Status holds one ENUM
value (Pending, Confirmed, or Cancelled) and TotalAmount holds
one decimal number per row.
**Result: Already in 1NF. No changes needed.**

### 2NF
The primary key is BookingID, a single column. CustomerID and
EventID are foreign keys that reference other tables — they do
not create partial dependencies because the PK is not composite.
All columns fully depend on BookingID.
**Result: Already in 2NF. No changes needed.**

### 3NF
TotalAmount represents the total cost of this specific booking
and depends only on BookingID, not on CustomerID or EventID
independently. No transitive dependencies exist.
**Result: Already in 3NF. No changes needed.**

---

## Table 4 — payment

| Column | Type |
|---|---|
| PaymentID (PK) | INT |
| BookingID (FK) | INT |
| Amount | DECIMAL |
| PaymentDate | DATE |
| Method | ENUM |
| PaymentStatus | ENUM |

### 1NF
All columns are atomic. Method stores one payment method
(Cash, Card, or Bank Transfer) and PaymentStatus stores one
state (Paid, Pending, or Refunded) per row.
**Result: Already in 1NF. No changes needed.**

### 2NF
The primary key is PaymentID, a single column. All non-key
columns fully depend on PaymentID. No partial dependency
is possible.
**Result: Already in 2NF. No changes needed.**

### 3NF
PaymentStatus does not depend on Method. Amount does not
determine PaymentDate. Every column independently describes
the payment record through PaymentID only.
**Result: Already in 3NF. No changes needed.**

---

## Table 5 — service

| Column | Type |
|---|---|
| ServiceID (PK) | INT |
| ServiceName | VARCHAR(120) |
| Category | VARCHAR(80) |
| Cost | DECIMAL |
| Description | TEXT |
| IsAvailable | BOOLEAN |

### 1NF
All columns hold single atomic values. IsAvailable is a single
boolean flag and Cost is a single decimal value per row.
**Result: Already in 1NF. No changes needed.**

### 2NF
The primary key is ServiceID, a single column. All non-key
columns fully depend on ServiceID.
**Result: Already in 2NF. No changes needed.**

### 3NF
Cost does not determine Category, and Category does not
determine ServiceName. Each column independently describes
the service through ServiceID only. No transitive dependency
exists.
**Result: Already in 3NF. No changes needed.**

---

## Table 6 — event_service (Junction Table)

| Column | Type |
|---|---|
| EventID (PK/FK) | INT |
| ServiceID (PK/FK) | INT |
| Quantity | INT |
| Notes | TEXT |

### 1NF
All columns hold single atomic values. Quantity is a single
integer and Notes is a single text value per row.
**Result: Already in 1NF. No changes needed.**

### 2NF
This table has a composite primary key: (EventID, ServiceID).
2NF requires that every non-key column depends on the WHOLE
composite key, not just part of it.
- Quantity = number of service units for THIS specific
  event-service pair → depends on both EventID AND ServiceID.
- Notes = custom instructions for THIS specific pairing →
  depends on both EventID AND ServiceID.
No partial dependency exists.
**Result: Already in 2NF. No changes needed.**

### 3NF
Quantity does not determine Notes, and Notes does not
determine Quantity. Both columns depend only on the composite
primary key (EventID, ServiceID) and not on each other.
**Result: Already in 3NF. No changes needed.**

---

## Final Summary

| Table | 1NF | 2NF | 3NF | Changes Made |
|---|---|---|---|---|
| customer | ✅ | ✅ | ✅ | None |
| event | ✅ | ✅ | ✅ | None |
| booking | ✅ | ✅ | ✅ | None |
| payment | ✅ | ✅ | ✅ | None |
| service | ✅ | ✅ | ✅ | None |
| event_service | ✅ | ✅ | ✅ | None |

The schema was designed correctly from the start and satisfies
Third Normal Form (3NF) across all six tables. No structural
changes were required during the normalization process.
-- ============================================================
--  EVENT MANAGEMENT SYSTEM — DML Script
--  Milestone 5 — Data Population
--  Prepared by: Ume Habiba
--  Course: Database Lab | BCS 4th Semester, Group-A
--  Instructor: Mr. Ali Hassan
-- ============================================================

USE event_management;

-- ============================================================
-- STEP 1: LOAD DATA FROM CSV FILES
-- ============================================================

-- Load customer data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customer.csv'
INTO TABLE customer
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(CustomerID, FullName, Email, Phone, Address, RegisteredAt);

-- Load event data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/event.csv'
INTO TABLE event
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(EventID, EventName, EventType, EventDate, Venue, Capacity, Description);

-- Load service data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/service.csv'
INTO TABLE service
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ServiceID, ServiceName, Category, Cost, Description, IsAvailable);

-- Load booking data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/booking.csv'
INTO TABLE booking
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(BookingID, CustomerID, EventID, BookingDate, Status, TotalAmount);

-- Load payment data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/payment.csv'
INTO TABLE payment
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(PaymentID, BookingID, Amount, PaymentDate, Method, PaymentStatus);

-- Load event_service data
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/event_service.csv'
INTO TABLE event_service
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(EventID, ServiceID, Quantity, Notes);

-- ============================================================
-- STEP 2: UPDATE OPERATION
-- ============================================================

-- Update booking status to Confirmed where payment is Paid
UPDATE booking
SET Status = 'Confirmed'
WHERE BookingID IN (
    SELECT
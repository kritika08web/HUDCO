CREATE DATABASE hotel_management;
USE hotel_management;

-- Table for hotels
CREATE TABLE Hotels (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100),
    country VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100)
);

-- Table for rooms
CREATE TABLE Rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT,
    room_number VARCHAR(10) NOT NULL,
    type VARCHAR(50) NOT NULL, -- e.g., Single, Double, Suite
    price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL, -- e.g., Available, Occupied, Maintenance
    FOREIGN KEY (hotel_id) REFERENCES Hotels(hotel_id)
);

-- Table for customers
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- Table for bookings
CREATE TABLE Bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    customer_id INT,
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL, -- e.g., Confirmed, Checked-In, Cancelled
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Table for payments
CREATE TABLE Payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(50) NOT NULL, -- e.g., Credit Card, Cash, Online
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id)
    );
    show tables;
    
    select * from hotels;
    select * from rooms;
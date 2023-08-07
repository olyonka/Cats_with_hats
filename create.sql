CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    user_type VARCHAR(10)
);

CREATE TABLE Rooms (
    room_id INT PRIMARY KEY,
    host_id INT,
    title VARCHAR(255),
    description TEXT,
    max_residents INT,
    price_perNight DECIMAL(10, 2),
    FOREIGN KEY (host_id) REFERENCES Hosts(host_id)
);

CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    total_cost DECIMAL(10, 2),
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    rating INT,
    comment TEXT,
    date DATE,
    FOREIGN KEY (guest_id) REFERENCES Guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);
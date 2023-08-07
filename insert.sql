-- Inserting Users
INSERT INTO Users (user_id, name, email, phone, user_type)
VALUES (1, 'Alis Sams', '1@example.com', '22333445', 'Host'),
       (2, 'Bob Smith', '2@example.com', '23455677', 'Guest');

-- Inserting Rooms
INSERT INTO Rooms (room_id, host_id, title, description, max_residents, price_per_night)
VALUES (1, 1, 'Apartment1', 'A comfortable apartment in the heart of the city London.', 2, 100.00),
       (2, 1, 'Apartment2', 'A comfortable apartment in the heart of the city Paris.', 3, 200.00);

-- Inserting Reservations
INSERT INTO Reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date, total_cost)
VALUES (1, 1, 1, '2023-08-01', '2023-08-07', 600.00),
       (2, 1, 2, '2023-08-08', '2023-08-10', 400.00);

-- Inserting Reviews
INSERT INTO Reviews (review_id, guest_id, room_id, rating, comment, date)
VALUES (1, 1, 1, 4, 'Had a great stay!', '2023-08-08'),
       (2, 1, 2, 5, 'Amazing location and views.', '2023-08-15');
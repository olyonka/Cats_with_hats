SELECT u.name, u.user_id
FROM Users u
JOIN Reservations r ON u.user_id = r.guest_id
GROUP BY u.name, u.user_id
ORDER BY COUNT(r.reservation_id) DESC
LIMIT 1;
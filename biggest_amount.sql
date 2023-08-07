SELECT u.user_id AS host_id, u.name AS host_name, SUM(r.total_cost) AS earnings
FROM Users u 
JOIN Rooms ro ON u.user_id = ro.host_id
JOIN Reservations r ON ro.room_id = r.room_id
WHERE r.check_in_date >= DATEADD(MONTH, -1, GETDATE())
GROUP BY h.host_id, u.name
ORDER BY earnings DESC
LIMIT 1;
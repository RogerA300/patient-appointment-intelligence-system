-- No-show rate by department
SELECT 
    department,
    COUNT(*) AS total_appointments,
    SUM(CASE WHEN status = 'No Show' THEN 1 ELSE 0 END) AS no_show_count,
    ROUND(
        SUM(CASE WHEN status = 'No Show' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS no_show_rate
FROM appointments
GROUP BY department
ORDER BY no_show_rate DESC;

-- Top 5 patients with most no-shows
SELECT 
    p.name,
    COUNT(*) AS total_no_show
FROM patients p
JOIN appointments a
ON p.patient_id = a.patient_id
WHERE a.status = 'No Show'
GROUP BY p.name
ORDER BY total_no_show DESC
LIMIT 5;

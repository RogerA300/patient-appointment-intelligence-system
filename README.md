# patient-appointment-intelligence-system
SQL and Python analysis of hospital appointment data to identify no-show trends and business insights

# Patient Appointment Intelligence System

## Tools Used
- MySQL
- Python
- Power BI

## Key Insights
- Identified departments with highest no-show rates
- Found repeat no-show patients
- Analyzed trends over time

## SQL Example
```sql
SELECT department, COUNT(*) AS total_appointments
FROM appointments
GROUP BY department;

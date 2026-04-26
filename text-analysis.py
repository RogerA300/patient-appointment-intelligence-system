import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://user:password@localhost/db_name")

query = """
SELECT 
    DATE_FORMAT(appointment_date, '%Y-%m') AS month,
    ROUND(
        SUM(CASE WHEN status = 'No Show' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS no_show_rate
FROM appointments
GROUP BY month
ORDER BY month;
"""

df = pd.read_sql(query, engine)

plt.plot(df['month'], df['no_show_rate'])
plt.title("No-Show Rate Over Time")
plt.xlabel("Month")
plt.ylabel("No-Show Rate (%)")
plt.xticks(rotation=45)
plt.show()

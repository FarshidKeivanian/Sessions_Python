#pip install matplotlib pandas

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Data for the Gantt Chart
tasks = {
    "Market Research": ("2024-07-01", "2024-08-15"),
    "App Design": ("2024-08-01", "2024-09-15"),
    "App Development": ("2024-08-15", "2024-10-30"),
    "Testing & QA": ("2024-10-01", "2024-11-30"),
    "Launch & Marketing": ("2024-11-15", "2024-12-31")
}

# Convert dates to matplotlib date numbers
for key, value in tasks.items():
    start_date, end_date = pd.to_datetime(value[0]), pd.to_datetime(value[1])
    tasks[key] = (mdates.date2num(start_date), mdates.date2num(end_date))

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
for i, (task, dates) in enumerate(tasks.items()):
    start_date, end_date = dates
    ax.barh(task, end_date - start_date, left=start_date, color=plt.cm.Set3(i * 0.1), edgecolor='black')

# Formatting
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_minor_locator(mdates.DayLocator())
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle=':', linewidth='0.5', color='gray')
plt.xlabel("Date")
plt.title("Gantt Chart for New Mobile App Launch")
plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime

# Define the project start date
start_date = datetime.date(2023, 5, 1)

# Define tasks, durations (in weeks), and dependencies (in task indices)
tasks = {
    "Requirement Analysis": (4, None),
    "System Design": (6, 0),
    "Module 1 Development": (8, 1),
    "Module 2 Development": (8, 1),
    "Module 3 Development": (8, 1),
    "Testing Phase 1": (4, [2, 3, 4]),
    "Testing Phase 2": (4, 5),
    "Deployment": (2, 6)
}

# Calculate start and end dates for tasks
task_dates = {}
for i, (task, (duration, deps)) in enumerate(tasks.items()):
    if deps is None:
        start = start_date
    elif isinstance(deps, list):
        start = max(task_dates[list(tasks.keys())[d]][1] for d in deps) + datetime.timedelta(days=1)
    else:
        start = task_dates[list(tasks.keys())[deps]][1] + datetime.timedelta(days=1)
    end = start + datetime.timedelta(weeks=duration)
    task_dates[task] = (start, end)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
for i, (task, (start, end)) in enumerate(task_dates.items()):
    ax.barh(task, end - start, left=start, color=np.random.rand(3,))

# Formatting the plot
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xlabel('Date')
plt.ylabel('Task')
plt.title('Project Gantt Chart')
plt.grid(True)
plt.tight_layout()
plt.show()

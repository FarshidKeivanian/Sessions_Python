import matplotlib.pyplot as plt

# Domains and their key processes
domains = ["Align, Plan and Organize", "Build, Acquire and Implement", "Deliver, Service and Support", "Monitor, Evaluate and Assess"]
processes = [
    ["Manage IT Management Framework", "Manage Strategy", "Manage Enterprise Architecture", "Manage Innovation", "Manage Portfolio", "Manage Budget and Costs"],
    ["Manage Programs and Projects", "Manage Requirements Definition", "Manage Solutions Identification and Build", "Manage Availability and Capacity"],
    ["Manage Operations", "Manage Service Request and Incidents", "Manage Problems", "Manage Continuity"],
    ["Monitor and Evaluate Performance", "Monitor and Evaluate Internal Control", "Ensure Compliance with External Requirements"]
]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = range(len(domains))
process_counts = [len(p) for p in processes]

ax.barh(y_pos, process_counts, color='skyblue')
ax.set_yticks(y_pos)
ax.set_yticklabels(domains)
ax.set_xlabel('Number of Processes')
ax.set_title('COBIT Management Objectives for an IT Service Company')

for i, v in enumerate(process_counts):
    ax.text(v + 0.1, i, str(v), color='blue', va='center')

plt.show()

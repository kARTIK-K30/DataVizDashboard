import matplotlib.pyplot as plt
import statistics

# User input
n = int(input("Enter number of values: "))

labels = []
values = []

for i in range(n):
    labels.append(input(f"Enter label {i+1}: "))
    values.append(float(input(f"Enter value {i+1}: ")))

# ---------- DATA ANALYSIS ----------
mean_val = statistics.mean(values)
median_val = statistics.median(values)
try:
    mode_val = statistics.mode(values)
except statistics.StatisticsError:
    mode_val = "No unique mode"

print("\n--- Data Summary ---")
print(f"Mean   : {mean_val}")
print(f"Median : {median_val}")
print(f"Mode   : {mode_val}")

# ---------- Create dashboard ----------
plt.figure(figsize=(10, 6))

# Bar chart
plt.subplot(1, 3, 1)
for i in range(n):
    plt.bar(labels[i], values[i])
plt.title("Bar Chart")

# Line chart
plt.subplot(1, 3, 2)
plt.plot(labels, values, marker='o')
plt.title("Line Chart")

# Pie chart
plt.subplot(1, 3, 3)
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.suptitle(f"Data Visualization Dashboard\nMean: {mean_val:.2f} | Median: {median_val} | Mode: {mode_val}")
plt.tight_layout()
plt.show()

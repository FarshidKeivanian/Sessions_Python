def read_temperatures(file_path):
    """Reads temperatures from a file and returns a dictionary of cities and their temperature lists."""
    temperatures = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                city = parts[0]
                temps = list(map(lambda x: float(x), parts[1:]))
                temperatures[city] = temps
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return temperatures

def calculate_stats(temperatures):
    """Calculates the min, max, and average temperatures for a list of temperatures."""
    minimum = min(temperatures)
    maximum = max(temperatures)
    average = sum(temperatures) / len(temperatures)
    return minimum, maximum, average

def process_data(temperature_data):
    """Process data and generate reports on temperature thresholds."""
    report = {}
    for city, temps in temperature_data.items():
        min_temp, max_temp, avg_temp = calculate_stats(temps)
        report[city] = {
            "Min Temp": min_temp,
            "Max Temp": max_temp,
            "Average Temp": avg_temp,
            "Status": "Critical" if max_temp > 40 else "Normal"
        }
    return report

def write_report(report, file_path):
    """Writes the temperature report to a file."""
    with open(file_path, 'w') as file:
        for city, stats in report.items():
            file.write(f"{city}:\n")
            for key, value in stats.items():
                file.write(f"\t{key}: {value}\n")
            file.write("\n")

def main():
    file_path = 'D:\synthetic_temperature_data2.csv'
    output_path = 'temperature_report.txt'
    
    # Read temperature data
    temperature_data = read_temperatures(file_path)
    
    # Process the data and generate a report
    report = process_data(temperature_data)
    
    # Write the report to a file
    write_report(report, output_path)

    print(f"Report has been generated and saved to {output_path}")

if __name__ == "__main__":
    main()

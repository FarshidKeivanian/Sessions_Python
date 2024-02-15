from statistics import mean, median, mode, stdev, variance

def calculate_mean(numbers):
    return mean(numbers)

def calculate_median(numbers):
    return median(numbers)

def calculate_mode(numbers):
    try:
        return mode(numbers)
    except:
        return "No unique mode found"

def calculate_standard_deviation(numbers):
    return stdev(numbers)

def calculate_variance(numbers):
    return variance(numbers)

def get_numbers_from_user():
    input_string = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(num) for num in input_string.split()]
    return number_list

def main():
    numbers = get_numbers_from_user()
    print("Choose an operation:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation")
    print("5. Variance")
    operation = input("Enter the number of the operation you want to perform: ")
    
    if operation == "1":
        print("Mean:", calculate_mean(numbers))
    elif operation == "2":
        print("Median:", calculate_median(numbers))
    elif operation == "3":
        print("Mode:", calculate_mode(numbers))
    elif operation == "4":
        print("Standard Deviation:", calculate_standard_deviation(numbers))
    elif operation == "5":
        print("Variance:", calculate_variance(numbers))
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()

find_largest_number <- function(numbers) {
  if(length(numbers) == 0) { # Check if the vector is empty
    return(NA) # Return NA (R's equivalent of None) if the vector is empty
  }
  largest <- numbers[1] # Initialize largest to the first number in the vector
  for(number in numbers[-1]) { # Start loop from the second element
    if(number > largest) {
      largest <- number
    }
  }
  return(largest)
}
# Example usage of the function with a vector of numbers
result <- find_largest_number(c(3, 67, 99, 23, 45))
print(result)
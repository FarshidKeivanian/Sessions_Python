bubble_sort <- function(arr) {
    n <- length(arr)
    for (i in 1:(n-1)) {
        for (j in 1:(n-i)) {
            if (arr[j] > arr[j+1]) {
                temp <- arr[j]
                arr[j] <- arr[j+1]
                arr[j+1] <- temp
            }
        }
    }
    return(arr)
}
# Example usage
numbers <- c(64, 34, 25, 12, 22, 11, 90)
sorted_numbers <- bubble_sort(numbers)
print(paste("Sorted list:", toString(sorted_numbers)))
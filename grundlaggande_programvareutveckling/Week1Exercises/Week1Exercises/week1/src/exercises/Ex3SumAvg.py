# package exercises
#
# Program to calculate sum and average for non-negative integers
#
# See:
# - Loops

def sum_avg_program():
    # Write your code here
    print("Write your own code for calculating sums and averages")
    # -- Input (and bookkeeping)


    # -- Process---
    i = 0
    sum = 0
    starting_int = 0
    
    while starting_int != -1:
        i += 1
        sum += starting_int
        starting_int = int(input("Enter a number\n"))
        
        
    print(sum)
    print(i)
    print(sum/(i-1))
        



    # -- Output ----


# Recommended way to make module executable
if __name__ == "__main__":
    sum_avg_program()

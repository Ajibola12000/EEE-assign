import time
import matplotlib.pyplot as plt

# === Cube Root Function ===
def simple_cube_root(n):
    """
   I Computes the cube root of a number using binary search.
    
    Args:
        n (float): The number for which the cube root is to be calculated.
    
    Returns:
        tuple: (cube_root, steps), where:
            - cube_root (float): The approximate cube root of `n`.
            - steps (int): The number of iterations taken to converge.
    """
    steps = 0  # I Initialize step counter
    is_negative = n < 0  # I Check if the input is negative
    n = abs(n)  # I Work with positive numbers for simplicity
    low = 0  # Lower bound of search range
    high = n  # Upper bound of search range
    precision = 0.0000000001  # Desired precision for the solution

    # Binary search loop
    while low <= high:
        steps += 1  # Increment step counter
        mid = (low + high) / 2  # I Compute midpoint
        cube = mid * mid * mid  # I Calculate cube of midpoint

        # I Check if midpoint's cube is within precision of `n`
        if abs(cube - n) < precision:
            return (-mid if is_negative else mid, steps)  # I Return with correct sign
        elif cube < n:
            low = mid  # I Adjust lower bound if cube is too small
        else:
            high = mid  # I Adjust upper bound if cube is too large

    # Fallback return (should theoretically not be needed due to precision check)
    return (-mid if is_negative else mid, steps)


# === Graph Drawing Function ===
def draw_graphs(digits, step_counts, time_taken):
    """
    Plots two graphs: Steps vs. Digits and Time vs. Digits.
    
    Args:
        digits (list): List of digit lengths tested.
        step_counts (list): Corresponding steps taken for each digit length.
        time_taken (list): Corresponding time taken for each digit length.
    """
    fig, (left, right) = plt.subplots(1, 2, figsize=(12, 5))  # Create a figure with two subplots

    # Left subplot: Steps vs. Digits
    left.plot(digits, step_counts, marker='o', color='blue', label='Steps')
    left.set_title("Steps vs. Number of Digits")
    left.set_xlabel("Digits in Number")
    left.set_ylabel("Steps Taken")
    left.grid(True)  # Add grid for better readability
    left.legend()  # Show legend

    # Right subplot: Time vs. Digits
    right.plot(digits, time_taken, marker='s', color='red', label='Time (s)')
    right.set_title("Time vs. Number of Digits")
    right.set_xlabel("Digits in Number")
    right.set_ylabel("Time (seconds)")
    right.grid(True)
    right.legend()

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()  # Display the plots


# === Collect and Process Data ===
digits_list = []  # I Store the number of digits in each test number
steps_list = []  # I Store steps taken for each test number
times_list = []  # I Store time taken for each test number

# Test numbers with increasing digit lengths (1 to 10 digits)
for num_digits in range(1, 11):
    # Generate test number (e.g., 15, 105, 1005, ..., 1000000005)
    test_number = 10**(num_digits - 1) + 5  

    # Measure time and steps for cube root calculation
    start_time = time.time()
    _, steps = simple_cube_root(test_number)
    end_time = time.time()

    time_taken = end_time - start_time  # Compute elapsed time

    # Store results
    digits_list.append(num_digits)
    steps_list.append(steps)
    times_list.append(time_taken)

    # Print results for current test
    print(f"{test_number}: Steps={steps}, Time={time_taken:.8f} seconds")


# === Draw Graphs ===
draw_graphs(digits_list, steps_list, times_list)  # Visualize the results
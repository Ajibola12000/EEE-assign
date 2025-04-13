def is_prime(n):
    """
    Efficient primality test using 6k±1 optimization.
    
    Args:ss
        n (int): Number to test for primality
        
    Returns:
        bool: True if prime, False otherwise
        
    Explanation:
        - I First check for small primes (<=3)
        - Eliminates even numbers and multiples of 3
        - Then checks divisors of form 6k±1 up to √n
        - This is ~3x faster than checking all numbers up to √n
    """
    if n <= 3:
        return n > 1  # 2 and 3 are prime, numbers <=1 are not
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate even numbers and multiples of 3
    
    # Check divisors of form 6k±1 up to √n
    i = 5  # Starting from 5 (next prime after 3)
    w = 2  # Initial step (will alternate between 2 and 4)
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w  # Alternate between 2 and 4 (for 6k±1 steps)
    
    return True  # If no divisors found, it's prime

def sum_primes_in_range(start, end):
    """
    Calculate sum of primes in a given range [start, end].
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
        
    Returns:
        int: Sum of all prime numbers in the range
        
    Explanation:
        - Uses is_prime() to check each number
        - Generator expression for memory efficiency
        - Includes both start and end in range
    """
    return sum(n for n in range(start, end + 1) if is_prime(n))

# Example usage with comments
if __name__ == "__main__":
    # I Calculate sum of primes between 3 and 1000
    prime_sum = sum_primes_in_range(3, 1000)
    
    # Print results with explanation
    print("Sum of prime numbers between 3 and 1000:")
    print(prime_sum) 
    
    # Breakdown of what the code is doing:
    # 1. For each number n from 3 to 1000:
    #    a. I Check if n is prime using optimized is_prime()
    #    b. If prime, includes in sum
    # 2. I Return the total sum
    # 3. The is_prime() function uses mathematical optimizations:
    #    - No even numbers >2 are prime
    #    - No multiples of 3 >3 are prime
    #    - Only check divisors of form 6k±1
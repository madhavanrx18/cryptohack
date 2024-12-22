def extended_euclidean(a, b):
    """
    Returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage:
a = 26513
b = 32321
gcd, x, y = extended_euclidean(a, b)
print(f"GCD: {gcd}, x: {x}, y: {y}")


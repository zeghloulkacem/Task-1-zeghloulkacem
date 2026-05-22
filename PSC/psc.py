import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Reason: Password must be at least 8 characters long to prevent brute-force risks)"
    
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    has_symbol = any(char in string.punctuation for char in password)

    criteria_met = sum([has_upper, has_digit, has_symbol])

    if criteria_met == 3:
        return "Strong (Passes all defensive criteria)"
    elif criteria_met == 2:
        return "Medium (Missing one security layer: check uppercase, numbers, or symbols)"
    else:
        return "Weak (Missing multiple required character sets)"
    
def main():
    print("=== DecodeLabs Industrial Kit: Project 1 ===")
    print("Initialize: Defensive Phase - Password Strength Checker\n")

    user_password = input("Enter your password to evaluate: ")

    result = check_password_strength(user_password)

    print("-" * 50)
    print(f"Password Evaluated: {user_password}")
    print(f"Risk Classification: {result}")
    print("-" * 50)

if __name__ == "__main__":
    main()


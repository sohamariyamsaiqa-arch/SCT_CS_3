import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Criteria
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Add at least one number.")

    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        remarks.append("Add at least one special character (@, $, !, %, *, ?, &).")

    # Rating
    if strength == 5:
        return "Strong Password ✅", remarks
    elif strength >= 3:
        return "Moderate Password ⚠", remarks
    else:
        return "Weak Password ❌", remarks


if _name_ == "_main_":
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    result, tips = check_password_strength(password)
    print(f"\nResult: {result}")
    if tips:
        print("Suggestions:")
        for tip in tips:
            print("-", tip)

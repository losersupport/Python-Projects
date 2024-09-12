import re

def evaluate_password(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "number": bool(re.search(r'[0-9]', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    score = sum(criteria.values())

    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }[score]

    feedback = {
        "length": "Password should be at least 8 characters long.",
        "uppercase": "Password should include at least one uppercase letter.",
        "lowercase": "Password should include at least one lowercase letter.",
        "number": "Password should include at least one number.",
        "special": "Password should include at least one special character."
    }

    return strength, [feedback[rule] for rule, met in criteria.items() if not met]

def main():
    password = input("Enter your password: ")
    strength, feedback = evaluate_password(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f" - {tip}")

if __name__ == "__main__":
    main()

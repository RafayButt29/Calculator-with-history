def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input! Use format like (8 + 8)")
        return

history_file = "history.txt"

def show_history():
    with open(history_file, "r") as h_file:
        lines = h_file.readlines()
        if not lines:
            print("No history found!")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    open(history_file, "w").close()
    print("History cleared!")

def save_history(equation, result):
    with open(history_file, "a") as h_file:
        h_file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input! Use format like (8 + 8)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot perform division with zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Use only +, -, *, /")
        return


    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input! Use format like (8 + 8)")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "%":
        result = num1 % num2    
    elif op == "/":
        if num2 == 0:
            print("Cannot perform division with zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Use only +, -, *, /")
        return

    # Convert result to int if it's a whole number
    if result == int(result):
        result = int(result)

    print("Result:", result)
    save_history(user_input, result)

def main():
    print("--- Simple Calculator (type history, clear, or exit) ---\n")
    while True:
        user_input = input("Enter calculation (+,-,*,/) or command (history, clear, exit): ")
        command = user_input.strip().lower()
        if command == "exit":
            print("Good Bye!")
            break
        elif command == "history":
            show_history()
        elif command == "clear":
            clear_history()
        else:
            calculate(user_input)

main()

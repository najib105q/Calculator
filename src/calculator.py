class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error of Division by zero!"
        return a / b

class CalculatorApp:

    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        while True:
            print("\n=== Calculator ===")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "5":
                print("Goodbye!")
                break

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice!")
                continue

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = self.calculator.add(a, b)
                elif choice == "2":
                    result = self.calculator.subtract(a, b)
                elif choice == "3":
                    result = self.calculator.multiply(a, b)
                else:
                    result = self.calculator.divide(a, b)

                print(f"Result: {result}")

            except ValueError:
                print("Please enter valid numbers!")


app = CalculatorApp()
app.run()
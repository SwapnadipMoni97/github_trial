class Calculator:
    """A simple calculator class to demonstrate OOP concepts."""

    def __init__(self, value=0):
        """Initialize the calculator with an optional starting value."""
        self.value = value

    def add(self, amount):
        """Add a number to the current value."""
        self.value += amount
        return self.value

    def subtract(self, amount):
        """Subtract a number from the current value."""
        self.value -= amount
        return self.value

    def multiply(self, amount):
        """Multiply the current value by a number."""
        self.value *= amount
        return self.value

    def divide(self, amount):
        """Divide the current value by a number."""
        if amount == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= amount
        return self.value

    def reset(self):
        """Reset the calculator value to zero."""
        self.value = 0
        return self.value


# Practical usage of the Calculator class
if __name__ == "__main__":
    calc = Calculator()  # Create an instance of Calculator

    # Perform some operations
    print("Initial value:", calc.value)
    print("Add 10:", calc.add(10))
    print("Subtract 3:", calc.subtract(3))
    print("Multiply by 4:", calc.multiply(4))
    print("Divide by 2:", calc.divide(2))
    print("Reset value:", calc.reset())
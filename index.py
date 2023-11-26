import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length**2

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        print("\nHexagon Properties:")
        print(f"Area: {self.calcArea()}")
        print(f"Perimeter: {self.calcPeri()}")
        print(f"Sum of Angles: {self.calcAngleSum()}")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length**2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        print("\nSquare Properties:")
        print(f"Area: {self.calcAreaSquare()}")
        print(f"Perimeter: {self.calcPeriSquare()}")

def main_menu():
    cnic = input("Enter the last digit of your CNIC: ")
    hexagon = Hexagon(int(cnic))
    square = Square(int(cnic) + 1)

    while True:
        print("\nMenu:")
        print("1. Display properties of Hexagon")
        print("2. Display properties of Square")
        print("Any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hexagon.display()
        elif choice == '2':
            square.display()
        else:
            print("Exiting. Thank you!")
            break

# Run the program
main_menu()

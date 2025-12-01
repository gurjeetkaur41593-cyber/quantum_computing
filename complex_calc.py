import math
import sys

class ComplexCalculator:
    @staticmethod
    def parse_complex(s: str) -> complex:
        """
        Try to parse a complex number from user string.
        Accepts forms like:
          - '3+4j' or '3-4j' (Python complex literal)
          - '3 4' meaning 3 (real) and 4 (imag)
          - '3' meaning 3+0j
        Raises ValueError on parse failure.
        """
        s = s.strip()
        # try Python literal first
        try:
            c = complex(s)
            return c
        except Exception:
            pass

        # try two numbers separated by whitespace or comma
        separators = [',', ' ']
        for sep in separators:
            if sep in s:
                parts = [p for p in s.replace(',', ' ').split() if p]
                if len(parts) == 1:
                    try:
                        return complex(float(parts[0]), 0.0)
                    except Exception:
                        break
                if len(parts) == 2:
                    try:
                        return complex(float(parts[0]), float(parts[1]))
                    except Exception:
                        break
        raise ValueError(f"Could not parse complex number from '{s}'")

    @staticmethod
    def add(a: complex, b: complex) -> complex:
        return a + b

    @staticmethod
    def subtract(a: complex, b: complex) -> complex:
        return a - b

    @staticmethod
    def multiply(a: complex, b: complex) -> complex:
        return a * b

    @staticmethod
    def divide(a: complex, b: complex) -> complex:
        if abs(b) == 0:
            raise ZeroDivisionError("Cannot divide by zero (the second complex number is 0).")
        return a / b

    @staticmethod
    def modulus(a: complex) -> float:
        return abs(a)

    @staticmethod
    def format_complex(c: complex, places: int = 2) -> str:
        r = round(c.real, places)
        i = round(c.imag, places)
        sign = '+' if i >= 0 else '-'
        return f"{r}{sign}{abs(i)}j"

def main():
    print("Complex Calculator — supports input like '3+4j' or '3 4' (real imag)\n")

    try:
        s1 = input("Enter first complex number (e.g. 3+4j or '3 4'): ").strip()
        a = ComplexCalculator.parse_complex(s1)
    except ValueError as e:
        print("Error parsing first number:", e)
        sys.exit(1)

    try:
        s2 = input("Enter second complex number (e.g. 1-2j or '1  -2'): ").strip()
        b = ComplexCalculator.parse_complex(s2)
    except ValueError as e:
        print("Error parsing second number:", e)
        sys.exit(1)

    menu = (
        "\nChoose operation:\n"
        "  1) Add (a + b)\n"
        "  2) Subtract (a - b)\n"
        "  3) Multiply (a * b)\n"
        "  4) Divide (a / b)\n"
        "  5) Modulus of first number |a|\n"
        "  6) Modulus of second number |b|\n"
        "  0) Exit\n"
    )
    print(menu)
    choice = input("Enter choice (0-6): ").strip()

    try:
        if choice == '1':
            res = ComplexCalculator.add(a, b)
            print(f"\nResult (a + b): {ComplexCalculator.format_complex(res)}")
        elif choice == '2':
            res = ComplexCalculator.subtract(a, b)
            print(f"\nResult (a - b): {ComplexCalculator.format_complex(res)}")
        elif choice == '3':
            res = ComplexCalculator.multiply(a, b)
            print(f"\nResult (a * b): {ComplexCalculator.format_complex(res)}")
        elif choice == '4':
            try:
                res = ComplexCalculator.divide(a, b)
                print(f"\nResult (a / b): {ComplexCalculator.format_complex(res, places=4)}")
            except ZeroDivisionError as zde:
                print("\nError:", zde)
        elif choice == '5':
            mod = ComplexCalculator.modulus(a)
            print(f"\n|a| = {mod:.4f}")
        elif choice == '6':
            mod = ComplexCalculator.modulus(b)
            print(f"\n|b| = {mod:.4f}")
        elif choice == '0':
            print("Goodbye.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

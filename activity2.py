import math

def rectangular_to_polar(a, b):
    r = math.sqrt(a*a + b*b)             # modulus
    theta = math.atan2(b, a)             # angle in radians
    phi = math.degrees(theta)            # angle in degrees
    return r, theta, phi

def polar_to_rectangular(r, theta=None, phi=None):
    # If theta and phi are both given, phi takes priority (degrees)
    if phi is not None:
        theta = math.radians(phi)

    a = r * math.cos(theta)
    b = r * math.sin(theta)
    return a, b

def main():
    print("Complex Vector Interchange Program")
    print("1) Enter a and b → Get theta and phi")
    print("2) Enter r and theta/phi → Get a and b\n")

    choice = input("Choose option (1 or 2): ")

    if choice == "1":
        a = float(input("Enter real part a: "))
        b = float(input("Enter imaginary part b: "))

        r, theta, phi = rectangular_to_polar(a, b)

        print(f"\nModulus r = {r:.4f}")
        print(f"Theta (radians) = {theta:.4f}")
        print(f"Phi (degrees) = {phi:.4f}")

    elif choice == "2":
        r = float(input("Enter modulus r: "))

        mode = input("Enter angle mode (theta for radians / phi for degrees): ").strip().lower()

        if mode == "theta":
            theta = float(input("Enter theta (radians): "))
            a, b = polar_to_rectangular(r, theta=theta)
        elif mode == "phi":
            phi = float(input("Enter phi (degrees): "))
            a, b = polar_to_rectangular(r, phi=phi)
        else:
            print("Invalid angle mode.")
            return

        print(f"\nReal part a = {a:.4f}")
        print(f"Imag part b = {b:.4f}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

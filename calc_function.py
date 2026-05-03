def calculate_distance():
    planet1 = input("Enter the name of the first planet: ").strip()
    planet2 = input("Enter the name of the second planet: ").strip()

    try:
        distance = float(input(f"Enter the distance between {planet1} and {planet2} in million kilometers: "))
    except ValueError:
        print("Invalid distance. Please enter a number.")
        return None

    print(f"The distance between {planet1} and {planet2} is {distance} million kilometers.")
    return distance


if __name__ == "__main__":
    calculate_distance()

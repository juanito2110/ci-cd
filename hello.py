def calculate_year_of_100(age: int, current_year: int = 2023) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        return (current_year - age) + 100

def main():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    year = calculate_year_of_100(age)
    print(f"Hello, {name}! You will turn 100 years old in the year {year}.")

if __name__ == "__main__":
    main()
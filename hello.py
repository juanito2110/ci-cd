def main():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    year = (2023 - age) + 100
    print(f"Hello, {name}! You will turn 100 years old in the year {year}.")

if __name__ == "__main__":
    main()
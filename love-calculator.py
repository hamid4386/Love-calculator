def calculate_love_score(name1, name2):
    # Convert names to lowercase
    name1 = name1.lower()
    name2 = name2.lower()

    # Calculate numeric values for each letter in the names
    value1 = sum(ord(char) - 96 for char in name1)
    value2 = sum(ord(char) - 96 for char in name2)

    # Sum up the values
    total_value = value1 + value2

    # Calculate the love score (range from 0 to 100)
    love_score = total_value % 101

    return love_score

def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    love_score = calculate_love_score(name1, name2)
    print(f"The love score between {name1} and {name2} is: {love_score}%")

if __name__ == "__main__":
    while True:
        main()

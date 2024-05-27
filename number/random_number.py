import random

def generate_random_numbers_with_quotes(num_rows):
    with open("random_numbers.txt", "w") as file:
        for _ in range(num_rows):
            random_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
            file.write(f"'{random_number}\n")

# Prompt the user for the number of rows
num_rows = int(input("Enter the number of rows you want to generate: "))

# Generate random numbers and write them to a text file
generate_random_numbers_with_quotes(num_rows)
print(f"{num_rows} rows of random numbers have been generated and saved to 'random_numbers.txt'.")

import random

# Lists of common first names and last names
first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'James', 'Emma', 'William', 'Olivia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']

def generate_random_names(num_names):
    random_names = []
    for _ in range(num_names):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_names.append(f"{first_name} {last_name}")
    return random_names

if __name__ == "__main__":
    num_names = int(input("Enter the number of random names to generate: "))  # Prompt user for number of names
    random_names = generate_random_names(num_names)
    
    # Write the names to a text file
    with open("random_names.txt", "w") as file:
        for name in random_names:
            file.write(name + "\n")

# Generates heading (e.g., ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Displays instructions
def instructions():

    statement_generator("Instructions", "♦")
    print('''
Instructions go here.
- Enter a number between 1 and 200 to find its factors.
- Type 'xxx' to exit the program.
    ''')

# Ask the user for an integer between 1 and 200
def num_check(question):

    error = "ENTER A NUMBER BETWEEN 1 AND 200 OR PREPARE TO GET DIE\n"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = int(response)  # Convert input to integer

            # Check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Find factors of a number
def find_factors(n):

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Main Routine
statement_generator("The Ultimate Factor Finder ", "_")


want_instructions = input("Press <enter> to read the instructions or any key to continue: ")
if want_instructions == "":
    instructions()

while True:
    # Ask user for a number to factor
    to_factor = num_check("Enter a number to factor (1-200): ")

    if to_factor == "xxx":
        print("Thank you for using the factors calculator! ")
        break

    # Get factors for integers that are 2 or more
    if to_factor != 1:
        factors = find_factors(to_factor)
        print(f"The factors of {to_factor} are: {factors} ")
    else:
        print("One is UNITY! It only has one factor: Itself. ")

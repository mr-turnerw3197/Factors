
# Generates heading (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "♦")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc.

    ''')

# Main routine goes here
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")
# Display functions if requested
if want_instructions == "":
    instructions()

    print("program continues")

    # Ask the user for width and loop until they
    # enter a number that is more than zero


def int_check(question, low):
    error = "ENTER A INTEGER MORE THAN ZERO, OR ELSE\n"
    while True:
        response = input(question)
        if response == "xxx":
            return response
        try:
            # Ask the user for a number
            response = int(response)

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes Here
for item in range(0, 373):
    integer = int_check(question="integer: ", low=1)
    if integer == "xxx":
        break
    print(integer)



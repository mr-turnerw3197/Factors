# Ask the user for an integer between 1 and 200
def num_check(question):

    error = "ENTER A NUMBER BETWEEN 1 AND 200 INCLUSIVE\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask the user for a number
            response = (int(response))

    # check that the number is between 1 and 200
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes Here
while True:
    to_factor = num_check("to factor: ")
    print("You choose to factor", to_factor)

    if to_factor == "xxx":
        break


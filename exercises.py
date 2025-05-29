def check_letter():
    letter = input("Enter a single letter (a-z or A-Z): ")

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single alphabetical letter.")
        return

    letter_lower = letter.lower()

    if letter_lower in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()


def check_voting_eligibility():
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)

        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return

        voting_age = 18

        if age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote yet.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

check_voting_eligibility()




def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Age cannot be negative.")
            return
        
        if age <= 2:
            dog_years = age * 10
        else:
            dog_years = 2 * 10 + (age - 2) * 7
        
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

calculate_dog_years()




def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

weather_advice()


def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").strip().title()
    day_input = input("Enter the day of the month: ").strip()

    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    if month not in months:
        print("Invalid month entered.")
        return

    try:
        day = int(day_input)
        if day < 1 or day > 31:
            print("Invalid day entered.")
            return
    except ValueError:
        print("Invalid day entered.")
        return

    month_numbers = {m: i+1 for i, m in enumerate(months)}
    m_num = month_numbers[month]

    if (m_num == 12 and day >= 21) or (m_num in (1, 2)) or (m_num == 3 and day <= 19):
        season = "Winter"
    elif (m_num == 3 and day >= 20) or (m_num in (4, 5)) or (m_num == 6 and day <= 20):
        season = "Spring"
    elif (m_num == 6 and day >= 21) or (m_num in (7, 8)) or (m_num == 9 and day <= 21):
        season = "Summer"
    elif (m_num == 9 and day >= 22) or (m_num in (10, 11)) or (m_num == 12 and day <= 20):
        season = "Fall"
    else:
        season = "Unknown"

    print(f"{month} {day} is in {season}.")

determine_season()


def guess_number():
    target = 42
    max_attempts = 5

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt} - Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please guess a number within the range 1 to 100.")
                continue

            if guess == target:
                print("Congratulations, you guessed correctly!")
                return
            elif guess < target:
                print("Guess is too low.")
            else:
                print("Guess is too high.")

            if attempt == max_attempts:
                print("Last chance!")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("Sorry, you failed to guess the number in five attempts.")

guess_number()


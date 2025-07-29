def get_user_info():
    print("\nLet's collect some fun facts about you ")

    name = input("What's your name? ")
    age = input("How old are you? ")
    color = input("What's your favorite color? ")
    food = input("What's your favorite food? ")
    city = input("Which city do you live in? ")
    shs = input("Which SHS did you attend? ")
    team = input("What's your favorite soccer team? ")

    summary = (
        f"Hello, {name}!\n"
        f"You are {age} years old, love the color {color}, and enjoy eating {food}.\n"
        f"Life must be awesome in {city}!\n"
        f"You attended {shs} SHS and proudly support {team} on match days! \n"
    )

    print("\n Here's your personalized summary:")
    print(summary)

    save_option = input("Do you want to save this summary to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        rating = input("Rate your assistant experience from 1 to 5 stars ⭐: ")
        filename = f"{name}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(summary)
            file.write(f"Assistant Rating: {rating} stars\n")
        print(f" Summary saved to '{filename}'")

def main():
    print(" Welcome to the Personal Summary Generator!")

    while True:
        get_user_info()
        restart = input("\nWould you like to create another summary? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thanks for hanging out! Stay awesome ")
            break

if __name__ == "__main__":
    main()

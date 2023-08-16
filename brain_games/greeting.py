import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string("May I have your name? ")
    print(f"hello, {name}!")
    return name


if __name__ == '__main__':
    welcome_user()

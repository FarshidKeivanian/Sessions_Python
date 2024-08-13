import random

def get_computer_choice():
    """انتخاب تصادفی کامپیوتر"""
    options = ['سنگ', 'کاغذ', 'قیچی']
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
    """تعیین برنده بین بازیکن و کامپیوتر"""
    if player_choice == computer_choice:
        return "مساوی!"
    elif (player_choice == 'سنگ' and computer_choice == 'قیچی') or \
         (player_choice == 'کاغذ' and computer_choice == 'سنگ') or \
         (player_choice == 'قیچی' and computer_choice == 'کاغذ'):
        return "شما برنده شدید!"
    else:
        return "کامپیوتر برنده شد!"

def play_game(rounds):
    """اجرای بازی در چندین دور"""
    player_score = 0
    computer_score = 0

    for round in range(1, rounds + 1):
        print(f"\n--- دور {round} ---")
        player_choice = input("انتخاب شما (سنگ، کاغذ، قیچی): ")
        computer_choice = get_computer_choice()

        print(f"انتخاب کامپیوتر: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "شما برنده شدید!":
            player_score += 1
        elif result == "کامپیوتر برنده شد!":
            computer_score += 1

    print("\n--- نتیجه نهایی ---")
    print(f"امتیاز شما: {player_score}")
    print(f"امتیاز کامپیوتر: {computer_score}")

    if player_score > computer_score:
        print("شما برنده نهایی بازی هستید!")
    elif computer_score > player_score:
        print("کامپیوتر برنده نهایی بازی است!")
    else:
        print("بازی مساوی شد!")

# اجرای بازی
rounds = int(input("چند دور می‌خواهید بازی کنید؟ "))
play_game(rounds)

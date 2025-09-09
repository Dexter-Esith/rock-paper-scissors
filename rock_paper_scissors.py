import random

# ASCII hands
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

print("=== Rock-Paper-Scissors ===")

while True:
    mode = input("Play vs computer (c) or vs player (p)? ").strip().lower()
    if mode not in ("c", "p"):
        print("Invalid! Type 'c' or 'p'.\n")
        continue

    # Player 1
    while True:
        p1_raw = input("Player 1, choose 0=Rock, 1=Paper, 2=Scissors: ").strip()
        if p1_raw.isdigit() and 0 <= int(p1_raw) <= 2:
            p1 = int(p1_raw)
            break
        print("Invalid! Please enter 0, 1, or 2.")

    # Player 2 or Computer
    if mode == "c":
        p2 = random.randint(0, 2)
        p2_name = "Computer"
    else:
        while True:
            p2_raw = input("Player 2, choose 0=Rock, 1=Paper, 2=Scissors: ").strip()
            if p2_raw.isdigit() and 0 <= int(p2_raw) <= 2:
                p2 = int(p2_raw)
                break
            print("Invalid! Please enter 0, 1, or 2.")
        p2_name = "Player 2"

    # Show choices with ASCII art
    print(f"\nPlayer 1 chose:\n{hands[p1]}")
    print(f"{p2_name} chose:\n{hands[p2]}")

    # Determine winner: (p1 - p2) % 3 → 0=draw, 1=Player1 wins, 2=Player2/Computer wins
    outcome = (p1 - p2) % 3
    if outcome == 0:
        print("Draw!\n")
    elif outcome == 1:
        print("Player 1 wins!\n")
    else:
        print(f"{p2_name} wins!\n")

    # Play again?
    again = input("Play again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break

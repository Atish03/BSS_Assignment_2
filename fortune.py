import os

NAME = os.getenv("NAME", "Atish Shah")
ADM_NO = os.getenv("ADM_NO", "21JE0191")

FORTUNES = {
    "happy": f"✨ {NAME.split()[0]}, you will have a great day today! ✨",
    "sad": f"😊 Don't worry {NAME.split()[0]}, tomorrow will be better. 😊",
    "neutral": "😐 Just another day, nothing special. 😐"
}

print(f"🔮 Welcome to {NAME}'s Fortune Teller! ({ADM_NO}) 🔮")

while True:
    try:
        print("How are you feeling today? (happy/sad/neutral): ", end="")
        feeling = input().strip().lower()
        if feeling in FORTUNES:
            print(FORTUNES[feeling])
        else:
            print("Invalid input. Please enter 'happy', 'sad', or 'neutral'.")
    except KeyboardInterrupt:
        print("\nGoodbye! Have a great day!")
        break
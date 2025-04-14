import os

NAME = os.getenv("NAME", "Atish Shah")
ADM_NO = os.getenv("ADM_NO", "21JE0191")

FORTUNES = {
    "happy": f"✨ {NAME.split()[0]}, you will have a great day today! ✨",
    "sad": f"😊 Don't worry {NAME.split()[0]}, tomorrow will be better. 😊",
    "neutral": "😐 Just another day, nothing special. 😐",
    "bored": "😴 Try to find something interesting to do! 😴",
    "excited": f"🎉 Something amazing is coming your way {NAME.split()[0]}! 🎉"
}

print(f"🔮 Welcome to {NAME}'s Fortune Teller! ({ADM_NO}) 🔮")

while True:
    try:
        print("How are you feeling today? (happy/sad/neutral/bored/excited): ", end="")
        feeling = input().strip().lower()
        if feeling in FORTUNES:
            print(FORTUNES[feeling])
        else:
            print("Invalid input. Please enter 'happy', 'sad', or 'neutral'.")
    except KeyboardInterrupt:
        print(f"\nGoodbye {NAME.split()[0]}! Have a great day!")
        break
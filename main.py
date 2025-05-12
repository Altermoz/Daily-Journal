from datetime import datetime

today = datetime.now()
formatted_date = today.strftime("%Y-%m-%d %H:%M:%S")

entry = input("Write your diary entry for today:\n")

print("\nEntry saved with timestamp! Here's your full diary\n")

with open("dailyJournal.txt", "a") as file:
    file.write(f"[{formatted_date}] {entry}\n")
    
with open("dailyJournal.txt", "r") as file:
    diary_contents = file.read()
    print(diary_contents)
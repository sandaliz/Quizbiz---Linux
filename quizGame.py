import json
from datetime import datetime
import os

print("🌍 Welcome, brave explorer! You've stumbled upon the gates of the **Linux Temple** 🏛️, where only the wise survive the command-line challenge! 🧠⚔️")
print("To earn your title as a Terminal Tactician 🧙‍♀️, you must prove your knowledge in the ancient art of Linux!")

play = input("🎒 Do you dare to begin this journey? (yes/no) 👣: ").strip().lower()

if play != "yes":
    print("😌 No problem, traveler. Return when you're ready to unlock the secrets of the shell. 🐚🗝️\n")
    quit()

print("🔥 Your journey begins now... May the `man` pages guide you. 📜🐧\n")

def ask_question(q_num, question, correct_answer, wrong_responses, options=None):
    print(f"🧩 Question {q_num}: {question}")
    if options:
        for letter, option_text in options.items():
            print(f"  {letter}) {option_text}")
        answer = input("⚔️ Your answer (letter or 'quit'): ").strip().lower()
        if answer == "quit":
            print("🛑 You have chosen to retreat from the Linux Temple. Farewell, warrior! 🏕️")
            quit()
        if answer == correct_answer:
            print("✅ Well done!\n")
            return True
        else:
            print(f"❌ {wrong_responses.get(answer, 'Hmm, that’s not quite right. Keep trying!')}\n")
            return False
    else:
        answer = input("⚔️ Your answer (or type 'quit' to exit): ").strip().lower()
        if answer == "quit":
            print("🛑 You have chosen to retreat from the Linux Temple. Farewell, warrior! 🏕️")
            quit()
        if answer == correct_answer.lower():
            print("✅ Well done!\n")
            return True
        else:
            print(f"❌ {wrong_responses.get(answer, 'Hmm, that’s not quite right. Keep trying!')}\n")
            return False


score = 0

questions = [
    {
        "q_num": 1,
        "question": "What command lists files and folders in the current directory?",
        "correct": "ls",
        "wrong_responses": {
            "pwd": "Nope! `pwd` shows where you are, not what's inside.",
            "cd": "Oops! `cd` changes directory, it doesn't list files.",
            "rm": "`rm` deletes files, so not what we want here."
        }
    },
    {
        "q_num": 2,
        "question": "Which command shows your current directory path?",
        "correct": "pwd",
        "wrong_responses": {
            "ls": "`ls` lists files, but doesn't tell you where you are.",
            "cd": "`cd` moves directories, not shows current location.",
            "find": "`find` searches for files, but doesn't print current path."
        }
    },
    {
       "q_num": 3,
        "question": "What does `chmod` do?",
        "options": {"a": "Change file permissions", "b": "List files", "c": "Delete files", "d": "Rename files"},
        "correct": "a",
        "wrong_responses": {
            "b": "`ls` lists files, it doesn't change permissions.",
            "c": "`rm` removes files, not permissions.",
            "d": "`mv` moves or renames files, not change permissions."
        }
    },
    {
        "q_num": 4,
        "question": "Which command lets you move between directories?",
        "correct": "cd",
        "wrong_responses": {
            "mv": "`mv` moves or renames files, not change directories.",
            "cp": "`cp` copies files, not move directories.",
            "rm": "`rm` deletes files or directories."
        }
    },
    {
        "q_num": 5,
        "question": "How do you check available disk space?(enter the relevant command)",
        "correct": "df",
        "wrong_responses": {
            "free": "`free` shows memory usage, not disk space.",
            "diskspace": "`diskspace` isn’t a standard Linux command.",
            "top": "`top` shows running processes, not disk space."
        }
    },
    {
        "q_num": 6,
        "question": "Which command displays memory usage?",
        "correct": "free",
        "wrong_responses": {
            "top": "`top` shows processes, but `free` is for memory stats.",
            "df": "`df` shows disk space, not memory.",
            "ps": "`ps` shows processes, not memory usage."
        }
    },
    {
        "q_num": 7,
        "question": "Who created Linux?",
        "options": {"a": "Linus Torvalds", "b": "Bill Gates", "c": "Richard Stallman", "d": "Ken Thompson"},
        "correct": "a",
        "wrong_responses": {
            "b": "Bill Gates is known for Windows, not Linux.",
            "c": "Richard Stallman founded the Free Software Foundation, but didn’t create Linux.",
            "d": "Ken Thompson worked on Unix, not Linux."
        }
    },
    {
        "q_num": 8,
        "question": "What is the Linux mascot?",
        "correct": "tux",
        "wrong_responses": {
            "fox": "Fox is Mozilla’s mascot, not Linux.",
            "dragon": "Dragons aren’t related to Linux mascot.",
            "squirrel": "Squirrels aren’t mascots here."
        }
    },
    {
        "q_num": 9,
        "question": "Which package manager does Red Hat use?",
        "correct": "yum",
        "wrong_responses": {
            "apt": "`apt` is used in Debian-based distros.",
            "zypper": "`zypper` is for SUSE Linux.",
            "pacman": "`pacman` is Arch Linux’s package manager."
        }
    },
    {
        "q_num": 10,
        "question": "True or False: Linux is less prone to viruses.",
        "correct": "true",
        "wrong_responses": {
            "false": "Actually, Linux’s architecture helps reduce virus risks."
        }
    },
    {
        "q_num": 11,
        "question": "What can you use to run Windows apps on Linux?",
        "correct": "wine",
        "wrong_responses": {
            "virtualbox": "VirtualBox runs full OS, but Wine runs Windows apps directly.",
            "dual-boot": "Dual-boot lets you switch OS, but doesn’t run apps simultaneously.",
            "none": "There are ways, like Wine!"
        }
    },
    {
        "q_num": 12,
        "question": "Can you have both Linux and Windows installed?",
        "correct": "yes",
        "wrong_responses": {
            "no": "Yes, dual-booting lets you install both."
        }
    },
    {
        "q_num": 13,
        "question": "In what year was Linux first released?",
        "correct": "1991",
        "wrong_responses": {
            "1989": "1989 was before Linux’s official release.",
            "1993": "1993 is too late, Linux came earlier.",
            "1995": "1995 is after the first release."
        }
    },
    {
        "q_num": 14,
    "question": "What does “sudo” allow you to do?",
    "options": {
        "a": "Copy files",
        "b": "Schedule tasks",
        "c": "Run commands as superuser",
        "d": "Remove directories"
    },
    "correct": "a",
    "wrong_responses": {
        "b": "`cron` schedules tasks, not sudo.",
        "c": "`cp` copies files.",
        "d": "`rm` removes files/directories."
        }
    },
    {
        "q_num": 15,
        "question": "Before naming it Linux, Torvalds called it what?",
        "options": {"a": "Freax", "b": "Maniax", "c": "Finnix", "d": "Torvalx"},
        "correct": "a",
        "wrong_responses": {
            "b": "Maniax isn’t correct.",
            "c": "Finnix is a Linux distro, but not the original name.",
            "d": "Torvalx is a made-up name."
        }
    }
]

for q in questions:
    if "options" in q:
        if ask_question(q["q_num"], q["question"], q["correct"], q["wrong_responses"], q["options"]):
            score += 1
    else:
        if ask_question(q["q_num"], q["question"], q["correct"], q["wrong_responses"]):
            score += 1

print(f"🎉 You've completed the Linux Temple Quiz! Your score: {score}/{len(questions)}")

if score == len(questions):
    print("🏆 Incredible! You're a Linux Legend! 👑")
    print("You've earned the title of Terminal Tactician 🧙‍♀️ — may your command line skills reign supreme! 🏆🐧")
elif score >= len(questions) / 2:
    print("Not bad! Keep sharpening those skills! ⚔️")
else:
    print("Keep practicing amateur! The Terminal Temple awaits your return.")

def load_leaderboard(filename="leaderboard.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def save_leaderboard(data, filename="leaderboard.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def update_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({
        "name": name,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    leaderboard.sort(key=lambda x: (-x["score"], x["date"]), reverse=False)

    leaderboard = leaderboard[:5] #only top 5
    save_leaderboard(leaderboard)
    return leaderboard

def display_leaderboard(leaderboard):
    print("\n🏅 Top Scores - Linux Temple Leaderboard 🏅")
    print("-" * 40)
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']} — Score: {entry['score']} — {entry['date']}")
    print("-" * 40)

player_name = input("\n📝 Enter your name to record your score (or type 'skip' to skip): ").strip()
if player_name.lower() != "skip" and player_name != "":
    updated_leaderboard = update_leaderboard(player_name, score)
    display_leaderboard(updated_leaderboard)
else:
    print("⚠️ Score not recorded. Thank you for playing!")

print("\n🛡️ Safe travels, warrior! Until next time... 🐧")


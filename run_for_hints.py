# In this challenge, you’ll unlock Python hints one by one.
# Each hint is hidden behind a simple math puzzle.
# Type a question number (1–23) to get your puzzle.
# Then use Python to solve it, type your answer, and unlock the hint!
# Type "help" for setup instructions or "exit" to quit.
# ===============================

import base64
import random

# Daniel’s 2025-11-10 updated key
encoded_hints = [
    "VXNlIC5zcGxpdCgpIHRvIHNlcGFyYXRlIHRoZSB3b3JkcyBhbmQgY29udmVydCBpbmRleGVzIDEgYW5kIDMgdG8gaW50cy4=",
    "UmVwbGFjZSBhbGwgZXhpc3Rpbmcgc3BhY2VzIHdpdGggdW5kZXJzY29yZXMgdXNpbmcgLnJlcGxhY2UoIiAiLCJfIiku",
    "VHVybiAiR0xPQ0FMIiB0byBsb3dlcmNhc2UgYW5kIGNvbnZlcnQgdG8gYSBsaXN0IHdpdGggbGlzdCh0ZXh0Lmxvd2VyKCkpLg==",
    "U2VwYXJhdGUgdGhlIHN0cmluZyBieSBzcGFjZXMgYW5kIGNvbnZlcnQgdGhlIHNlY29uZCB3b3JkIHRvIGFuIGludC4=",
    "UmVwbGFjZSBjb21tYXMgKHwiLCJ8KSB3aXRoIHNlbWljb2xvbnMgKHwiOyJ8KS4=",
    "VXNlIC50aXRsZSgpIHRvIGNhcGl0YWxpemUgZWFjaCB3b3JkLg==",
    "UmV2ZXJzZSB0aGUgc3RyaW5nIHVzaW5nIHNsaWNpbmcgOiB0ZXh0Wzo6LTFdLg==",
    "VXNlIHN0cmluZyBpbmRleGluZyB0byBnZXQgJzEyMycgZnJvbSBwb3NpdGlvbnMgNSB0byA4Lg==",
    "Q29udmVydCB0byBpbnQgdXNpbmcgaW50KCkgYW5kIGFkZCA4Lg==",
    "Sm9pbiBhIGxpc3Qgd2l0aCBjb21tYXMgaW4gYmV0d2VlbiB1c2luZyAiLCIuam9pbihsaXN0KS4=",
    "U3BsaXQgdGhlIHN0cmluZyBieSBoeXBoZW4gdXNpbmcgLnNwbGl0KCItIiku",
    "U3BsaXQgdGhlIG5hbWVzIGJ5ICIsICIgYW5kIGNvdW50IHRoZW0gd2l0aCBsZW4oKS4=",
    "RGl2aWRlIHBhZ2VzX3JlYWQv dG90YWxfcGFnZXMgYW5kIHJvdW5kIHRvIDIgZGVjaW1hbHMu",
    "U3VidHJhY3QgdGhlIGZvdW5kaW5nIHllYXIgZnJvbSAyMDI1IHRvIGdldCBDYW5hZGEncyBhZ2Uu",
    "VXNlIC5zdHJpcCgpIHRvIHJlbW92ZSBzcGFjZXMgZnJvbSBib3RoIGVuZHMu",
    "U3BsaXQgdGhlIHN0cmluZyBhdCB0aGUgQCwgdGhlbiByZXR1cm4gdGhlIHNlY29uZCBwYXJ0Lg==",
    "Q29udmVydCB0byB1cHBlcmNhc2UgYW5kIHR1cm4gaW50byBhIGxpc3QgdXNpbmcgbGlzdCgpLg==",
    "VXNlIG1lYW4oKSBmcm9tIHRoZSBzdGF0aXN0aWNzIG1vZHVsZS4=",
    "U2xpY2UgdGhlIHN0cmluZyBiZXR3ZWVuIDQ6NyBhbmQgMTA6MTMgYW5kIGNvbmNhdGVuYXRlIHRoZW0u",
    "U3BsaXQgdGhlIGRhdGUgYnkgIi0iLCBjb252ZXJ0IGVhY2ggcGFydCB0byBpbnQsIHJldHVybiBhIHR1cGxlLg==",
    "U3BsaXQgdGhlIHdvcmRzLCB0dXJuIHNlY29uZCB0byB1cHBlcmNhc2UsIHRoZW4gam9pbiBiYWNrLg==",
    "VXNlIC5jb3VudCgicyIpIHRvIGNvdW50IGhvdyBtYW55ICJzInMgdGhlcmUgYXJl",
    "TG9vcCBvdmVyIHRoZSBsaXN0LCBjb252ZXJ0IGVhY2ggZWxlbWVudCB0byBpbnQgdXNpbmcgaW50KCku",
]


def get_random_puzzle():
    """Create a random math problem and its answer."""
    a, b, c = random.randint(2, 10), random.randint(2, 10), random.randint(1, 5)
    problems = [
        (f"{a} + {b} * {c}", a + b * c),
        (f"({a} * {b}) - {c}", (a * b) - c),
        (f"{a} ** 2 - {b}", a**2 - b),
        (f"({a} + {b}) // {c}", (a + b) // c),
        (f"{a} * {b} + {c}", a * b + c),
    ]
    return random.choice(problems)


def show_help():
    """Explain what Python is and how to open it."""
    print("""
============================================
HOW TO USE THE PYTHON TERMINAL
============================================

Step 1: What is Python?
Python is a computer language that lets you tell the computer what to do.
You can use it to calculate, automate, or analyze data.

Step 2: How to Install It
1. Go to https://www.python.org/downloads/
2. Click “Download Python” (the latest version is fine).
3. Run the downloaded file and make sure you check:
   Check “[ ] Add Python to PATH” before clicking “Install Now”.

Step 3: Open the Python Terminal
- On Windows: press the Windows key, type **cmd**, then type `python`
- On Mac: open **Terminal** and type `python3`
- You’ll see something like:
      >>> 
  That means Python is ready!

Step 4: Try Simple Math
In the Python terminal, type something like:
    >>> 3 + 4 * 2
    11
That’s it! Python can solve math for you.

Step 5: Use It Here
When this program gives you a math challenge,
open Python, type the expression exactly as shown,
press Enter, and use the result as your answer!

============================================
""")


def main():
    print("  Welcome to the GLOCAL Data Track Hint Locker  ")
    print("Each question’s hint is locked behind a math puzzle.")
    print("Use the Python terminal to solve it, then enter your answer below.")
    print("Type a question number (1–23) to unlock a hint.")
    print("Type 'help' for instructions or 'exit' to quit.\n")

    while True:
        choice = input("Enter a question number (1–23), 'help', or 'exit': ").strip().lower()

        if choice == "exit":
            print("\nGoodbye!\n")
            break
        elif choice == "help":
            show_help()
            continue
        elif not choice.isdigit() or not (1 <= int(choice) <= len(encoded_hints)):
            print("Please type a number between 1 and 23, or 'help'.\n")
            continue

        q_index = int(choice) - 1
        expression, answer = get_random_puzzle()

        print(f"\nTo unlock hint #{choice}, solve this math challenge:")
        print(f"  🔹 {expression}")
        print("\nTip: Open the Python terminal, type that expression, and press Enter.")
        print("Then type your answer below.\n")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("That doesn’t look like a number. Try again!\n")
            continue

        if user_answer == answer:
            decoded = base64.b64decode(encoded_hints[q_index]).decode("utf-8")
            print(f"\nCorrect! Here’s your hint #{choice}:\n{decoded}\n")
        else:
            print("Nope! Try opening Python and typing it exactly as shown.\nKeep practicing - you’ll get it!\n")


if __name__ == "__main__":
    main()

from pathlib import Path

result = Path("guest_book.txt")

storage = ""
while True:
    user = input("Enter a name q to quit : ")

    if user.lower() == "q":
        break

    storage += user + "\n"

result.write_text(storage)

get_file = result.read_text()
get_file = get_file.splitlines()

print(get_file)

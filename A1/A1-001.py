name = input("")
surname = input("")

name_letters = name[:2] if len(name) >= 2 else name
surname_letters = surname[:2] if len(surname) >= 2 else surname
print(f"Hello {name} {surname}")
print(f"{name_letters}{surname_letters}")

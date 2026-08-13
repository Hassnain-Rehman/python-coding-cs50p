name = input("what's your name? ")

# removing extra space or whitespace from str
name = name.strip().title()

first, middle, last = name.split(" ")

print(f"hello,  {first},{middle}")

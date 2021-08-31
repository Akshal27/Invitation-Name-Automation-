# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'
name_list = []

with open(".\\Input\\Names\\invited_names.txt", mode="r") as file:
	for word in (file.read()).splitlines():
		name = word.strip()
		name_list.append(name)

with open(".\\Input\\Letters\\starting_letter.txt", mode="r") as letter:
	letter_content = letter.read()
	for name in name_list:
		data = letter_content.replace(PLACEHOLDER, name)
		with open(f".\\Output\\ReadyToSend\\{name}.txt", mode="w") as invite:
			invite.write(data)

# Replace the target string


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

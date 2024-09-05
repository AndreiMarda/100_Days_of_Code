with open("input/Names/invited_names.txt") as names:
    list_of_names= names.readlines()
    for name in list_of_names:
        stripped_name=name.strip()
        with open("input/Letters/starting_letter.txt") as letter_example:
            letter = str(letter_example.read())
            replaced_letter = letter.replace("[name]", f"{stripped_name}")
            with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as file_to_save:
                file_to_save.write(replaced_letter)

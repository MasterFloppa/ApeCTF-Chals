def format(input_string):
    # Replace spaces with underscores
    formatted_string = input_string.replace(" ", "_")
    
    # Convert to Leet speak
    leet_string = formatted_string.maketrans({'a': '4', 'b': '8', 'e': '3', 'g': '6', 'l': '1', 'o': '0', 's': '5', 't': '7'})
    formatted_string = formatted_string.translate(leet_string)

    # Wrap the string in curly braces
    formatted_string = "ApeCTF{" + formatted_string + "}"

    return formatted_string


input_text = "Piet is a very unique language i3s8e"            # Put your sentence here
result = format(input_text)
print(result)

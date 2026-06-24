import pyperclip 
 
text = pyperclip.paste() # Get the text off the clipboard 
alt_text = '' # This strings holds the alternating case
make_uppercase = False 
for charcter in text:
    # Gp through each character and add it to alt_text:
    if make_uppercase:
        alt_text += charcter.upper()
    else:
        alt_text += charcter.lower()
        
    # set make_upperchase to its opposite value:
    make_uppercase = not make_uppercase
pyperclip.copy(alt_text) # Put the result on the clipboard 
print(alt_text) # Print the results on the screen
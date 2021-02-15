##python 3 encoder ring 

#declare the keys for encoding
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#prompt user for which type of key they want to use
#prompt the user for their secret message. If they put in something incorrectly, loop back and ask again. 

while True:
    print("Enter secret message (letters and spaces only, please.)")
    ##takes the input and converts it to all upper case (for simplicity)
    secret = (input()).upper()
    #define and reset the output 
    output = ''
    try:
        #loop through each letter of the message. If it's a space, add a space to the output, encrypt the letter based on what's selected
        for i in secret:
            if i == ' ':
                output+=' '
            else:
                output+=alphabet[25 - alphabet.index(i)]
        #print the final output and exit the program
        print(output)
        break
    except:
        #catch when a user doesn't follow directions
        print("Oops, there was a problem with your message.")
#cleanly end the program
exit(0)
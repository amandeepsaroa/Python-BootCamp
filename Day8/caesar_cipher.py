from art import logo

def ceaser(message , shift_number , choice):

    end_txt = ""
    for char in message:
        # only encode char dont encode spaces and numbers or other symbols and work with only lower case so convert all to lowercase before doing operation
        if str(char).isalpha():

            
            if choice == 'encode':

                shifted = ord(char) + shift_number
                if shifted > ord('z'):  # Wrap around if it goes beyond 'z'
                    shifted -= 25       # to start from 'a' again if shifted is 28 therefore more than z ascii -26 = 2 therefore 'b'

                coded_char = chr(shifted)
                end_txt += coded_char
            
            elif choice == 'decode':

                shifted = ord(char) - shift_number
                if shifted < ord('a'):  # Wrap around if it goes before 'a'
                    shifted += 25


                coded_char = chr(shifted)
                end_txt += coded_char

        else:

            end_txt += char

    return end_txt

# def encode(message , shift_number):

#     # use 'ord(char)' to get its ascii value and 'chr(ascii)' to convert back to char
#     # for every char in message add shift number to ascii of each char and convert back to chr
#     encoded_txt = ""
#     for char in message:
#         # only encode char dont encode spaces and numbers or other symbols and work with only lower case so convert all to lowercase before doing operation
#         if str(char).isalpha():

#             shifted = ord(char) + shift_number
#             if shifted > ord('z'):  # Wrap around if it goes beyond 'z'
#                 shifted -= 25       # to start from 'a' again if shifted is 28 therefore more than z ascii -26 = 2 therefore 'b'

#             encoded_char = chr(shifted)
#             encoded_txt += encoded_char
#         else:

#             encoded_txt += char

#     return encoded_txt
    
# def decode(message , shift_number):

#     # use 'ord(char)' to get its ascii value and 'chr(ascii)' to convert back to char
#     # for every char in message add shift number to ascii of each char and convert back to chr
#     # to check if char is alpha you can use isalpha() which works for only str type so convert each char to string to check if its alpha or no
#     decoded_txt = ""
#     for char in message:
#         # only encode char dont encode spaces and numbers or other symbols
#         if str(char).isalpha():
            
#             shifted = ord(char) - shift_number
#             if shifted < ord('a'):  # Wrap around if it goes before 'a'
#                 shifted += 25
#             decoded_char = chr(shifted)
#             decoded_txt += decoded_char

#         # if not a alpha add it unchanged
#         else:
#             decoded_txt += char  

#     return decoded_txt

# main function 
def main():

    
    print(logo)

    state = 'yes'
    while state == 'yes':

        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number\n"))
        
        
        cipher_message = ceaser(message , shift_number , choice)
        print(f"Here's the {choice}ed result: {cipher_message}")
        
        state = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

        if state.lower() == 'no':
            break

            
if __name__ == "__main__":
    main()
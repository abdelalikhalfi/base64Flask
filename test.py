from app import deencode



"""
Welcome to the Decoder/Encoder Base64 Script.

To Decode Enter ~~> D
To encode Enter ~~> E

"""

letter = raw_input("If you want to decode Enter D, or E to encode : > ")

if letter == 'D':
    hash = raw_input("Enter the Hash You want to decode : > ")
    try:
     a = deencode.decode(hash)
     print(a)
    except:
     print("Enter a valid hash Please ")

elif letter == 'E':
    text = raw_input("Enter the text you want to encode : > ")
    print(deencode.encode(text))






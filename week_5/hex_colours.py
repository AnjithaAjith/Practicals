COLOUR_CODES = {"Red": "#ff0000", "Green": "#006400", "Blue": "	#0000ff", "Yellow": "#ffff00",
                "Violet": "#ee82ee", "Brown": "#a52a2a", "Black": "	#000000", "Orange": "#ff8c00", "Pink": "#ff1493",
                "Orchid": "#da70d6"}

colour_name = input("Enter a colour: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "is ", COLOUR_CODES[colour_name])
    else:
        print("Invalid code")
    colour_name = input("Enter a colour: ")

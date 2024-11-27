from Data.Lab4.Constants.GrayscaleDensityMap import DENSITY_MAP

def map_char_to_custom_set(char, color_symbols, color_option):
    if color_option == "grayscale":
        if char in DENSITY_MAP:
            index = DENSITY_MAP.index(char) * (len(color_symbols['grayscale']) - 1) // (len(DENSITY_MAP) - 1)
            return color_symbols['grayscale'][index]
    elif color_option == "black_and_white":
        if char in '@#*%':
            return color_symbols['black'][0]
        elif char in "=-:. ":
            return color_symbols['white'][1]
        else:
            return color_symbols['white'][0]
    return char

def old_macdonald(name):
    # first_letter = name[0]
    # inbetween = name[1:3]
    # fourth_letter = name[3]
    # rest = name[4:]

    first_half = name[:3]
    secound_half = name[3:]

    return first_half.capitalize() + secound_half.capitalize()


print(old_macdonald('macdolanld'))
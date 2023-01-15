def plainText(absPathFile):
    text = ""

    file = open(absPathFile, 'r')
    lines = file.readlines()

    for line in lines:
        text += line

    return text

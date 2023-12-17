alpha = list("abcdefghijklmonpqurstvwxyz")
translate = {"A":"@", "B":"8", "C":"(", "D":"|)", "E":"3", "F":"#", "G":"6", "H":"[-]", "I":"|", "J":"_|", "K":"|<", "L":"1", "M":"[]\/[]", "N":"[]\[]", "O":"0", "P":"|D", "Q":"(,)", "U":"|_|", "R":"|Z", "S":"$", "T":"']['", "V":"\/", "W":"\/\/", "X":"}{", "Y":"`/", "Z":"2"}
print("".join(translate[i.upper()] if i.isalpha() else i for i in input()))

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

    
print is_isogram("Dermatoglyphics")
print is_isogram("aba")
print is_isogram("moOse")
print is_isogram("")
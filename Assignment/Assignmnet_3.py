def rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return str1 in str2 + str2

# Example usage
string1 = "abcd"
string2 = "cdab"
print(rotation(string1, string2))

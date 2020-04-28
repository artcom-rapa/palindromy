
def palindrom(text):
    i = len(text)
    if i %2 == 1 and text[::1] == text[::-1]:
        return True
    else:
        return False
text = "kajak"

print(palindrom(text))

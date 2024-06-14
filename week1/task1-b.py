usr_input = input()

def checkVowel(usr_input):
    if usr_input.lower() in ['a','e','i','o','u']:
        return True
    else:
        return False

print(checkVowel(usr_input))
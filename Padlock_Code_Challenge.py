# Padlock Code Challenge - www.101computing.net

# Challenge 1: Total of all numbers from 1 to 40
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-1/
def padlock_challenge_1():
    code = sum(range(1, 41))
    # print(code)
    return code

# Challenge 2: Total number of 3-digit combinations where digit1 < digit2 < digit3
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/
def padlock_challenge_2():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(digit1+1, 10):
            for digit3 in range(digit2+1, 10):
                code += 1
            # print(str(digit1)+str(digit2)+str(digit3))
    return code

# Challenge 3: Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-3/
def padlock_challenge_3():
    code = 0
    for digit1 in range(0, 10, 2):
        for digit2 in range(0, 10, 2):
            for digit3 in range(0, 10, 2):
                code += 1
            # print(str(digit1)+str(digit2)+str(digit3))
    return code

# Challenge 4: Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-4/
def padlock_challenge_4():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if (digit1 + digit2 + digit3) % 2 != 0:
                    code += 1
                # print(str(digit1)+str(digit2)+str(digit3))
    return code

# Challenge 5: Total number of 3-digit combinations where at least two digits are equal
#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-5/
def padlock_challenge_5():
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
                    code += 1
                # print(str(digit1)+str(digit2)+str(digit3))
    return code


# Testing the functions
print("Challenge 1: Code =", padlock_challenge_1())
print("Challenge 2: Code =", padlock_challenge_2())
print("Challenge 3: Code =", padlock_challenge_3())
print("Challenge 4: Code =", padlock_challenge_4())
print("Challenge 5: Code =", padlock_challenge_5())

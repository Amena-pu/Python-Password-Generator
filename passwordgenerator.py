import string
import random
if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.ascii_lowercase
    s6 = string.ascii_letters
    s6 = string.hexdigits
    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    s.extend(list(s6))

    print("Your password: ", end="")
    print("".join(random.sample(s, plen)))
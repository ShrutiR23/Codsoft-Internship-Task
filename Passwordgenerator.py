import string
import random
#code
if __name__ == "__main__":
    l = string.ascii_lowercase
    u = string.ascii_uppercase
    d = string.digits
    p = string.punctuation
    plen = int(input("Enter password length\n"))
    s = []
    s.extend(list(l))
    s.extend(list(u))
    s.extend(list(d))
    s.extend(list(p))
#Password generator is ready.
    print("Your password is: ")
    print("".join(random.sample(s, plen)))
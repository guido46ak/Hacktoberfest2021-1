def rev_string(s):
    w = s.split()
    result = ' '.join(reversed(w))
    return result

s = "Aniket kasturi"
print(rev_string(s))
def spacify_string(s):
    w = []
    cur = ""
    for c in s:
        if c.isupper():
            w.append(cur)
            cur = ""
            cur += c.lower()
        else:
            cur += c
    w.append(cur)
    return "_".join(w)

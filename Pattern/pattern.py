if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum()==True:
            alnum=True
print(alnum)
for i in s:
    if i.isalpha()==True:
        alpha=True
print(alpha)
for i in s:
    if i.isdigit()==True:
        digit=True
print(digit)
for i in s:
    if i.islower()==True:
        lower=True
print(lower)
for i in s:
    if i.isupper()==True:
        upper=True
print(upper)
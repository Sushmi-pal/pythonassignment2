def is_palindrome(s):
    li=[]
    for i in range(len(s)-1,-1,-1):
        # revstring=''.join(s[i])
        li.append(s[i])
    revstring=''.join(li)
    if revstring==s:
        print('The given string {} is palindrome'.format(s))
    else:
        print('The given string {} is not a palindrome'.format(s))

is_palindrome('liril')
def searchinlist(l):
    for i,t in enumerate(l):
        if t!='John':
            continue
        print('John is found at index {}'.format(i))

    if 'John' not in l:
        print('Not found')



searchinlist(['Sabin','Neha','Siddhatha','Sanima','Shailendra','Saraswati','Shruti'])
searchinlist(['Sabin','Neha','Siddhatha','Sanima','Shailendra','Saraswati','John'])
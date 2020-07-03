while True:
    try:
        operatorr = input('Enter an operator:')
        num1=int(input('Enter a number:'))
        num2 = int(input('Enter another number:'))


    except ValueError:
        print('Provide the correct input')
        continue

    else:
        break


if operatorr=='+':
    sum=num1+num2
    print('Sum is',sum)

elif operatorr=='*':
    mul=num1*num2
    print('Multiplication of two nums is',mul)

elif operatorr=='/':
    if num2==0:
        print('Divide by zero error')
    else:
        div=num1/num2
        print('Division of two nums is',div)

elif operatorr == '-':
    sub=num1-num2
    print('Difference is',sub)

else:
    print("Please enter the correct operator")








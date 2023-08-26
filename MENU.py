while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-CODE BY AMIT-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print()
    print("1. CALCULATOR")
    print()
    print("2. FIND GRADE")
    print()
    print('3. TABLE')
    print()
    print('4. AREA AND CIRCUMFERENCE OF CIRCE')
    print()
    print("5. PALINDROME NUMBER")
    print()
    print('6. PATTERN')
    print()
    print("7. TIME YEAR CALCULATION")
    print()
    print('8. EXIT ')
    print()
    n=int(input("ENTER YOUR CHOICE : "))
    print()
    if n==1:
        while True:
            print('------------------------------------------------------------------------------CALCULATOR----------------------------------------------------------------------------------')
            print()
            print()
            print('WHAT DO YOU WANT TO DO?')
            print()
            print('1. ADDITION')
            print()
            print('2. SUBSTRACTION')
            print()
            print('3. MULTIPLICATION')
            print()
            print('4. DIVISION')
            print()
            print('5. EXPONENT')
            print()
            print('6. MAIN MENU')
            print()
            ch=int(input("ENTER YOUR CHOICE:- "))
            if ch==1:
                print()
                a=float(input("ENTER FIRST NO. : "))
                print()
                b=float(input("ENTER SECOND NO. : "))
                r=a+b
                print()
                print('THE SUM OF',a,'AND',b,'IS',r)
            elif ch==2:
                print()
                a=float(input("ENTER FIRST NO. : "))
                print()
                b=float(input("ENTER SECOND NO. : "))
                r=a-b
                print()
                print('THE DIFFERENCE OF',a,'AND',b,'IS',r)
            elif ch==3:
                print()
                a=float(input("ENTER FIRST NO. : "))
                print()
                b=float(input("ENTER SECOND NO. : "))
                print()
                r=a*b
                print('THE MULTIPLICATION OF',a,'AND',b,'IS',r)
            elif ch==4:
                print()
                a=float(input("ENTER DIVIDEND : "))
                print()
                b=float(input("ENTER DIVISIOR : "))
                if b==0:
                    print("0 DIVIDE ERROR!")
                else:
                    r=a/b
                    print()
                    print('THE OUTPUT OF THE DIVISION',a,'AND',b,'IS',r)
            elif ch==5:
                print()
                a=float(input("ENTER BASE : "))
                print()
                b=float(input("ENTER EXPONENTIAL : "))
                r=a**b
                print()
                print(a,'TO THE POWER',b,'IS',r)
            elif ch==6:
                break
            else:
                print()
                print("INVALID INPUT ENTERED!")

            print()
            print()
            print("---------------------------------------------------------------------------!!!RESTARTING!!!!!-------------------------------------------------------------------------------")
            print()
            print()
    elif n==2:
        n=float(input('ENTER YOUR PERCENTAGE: '))
        if n>=90 and n<=100:
            print()
            print('YOU GOT A+ GRADE')
        elif n>=80 and n<90:
            print()
            print('YOU GOT B GRADE')
        elif n>=70 and n<80:
            print()
            print('YOU GOT C GRADE')
        elif n>=60 and n<70:
            print()
            print('YOU GOT D GRADE')
        elif n>=0 and n<60:
            print()
            print('YOU GOT E GRADE. YOU MUST NEED MORE PRACTICE :(')
        else:
            print()
            print('INVALID INPUT ENTERED!')
    elif n==3:
        n1=int(input("ENTER NO. FROM WHERE TO START: "))
        print()
        n2=int(input("ENTER NO. FROM WHERE TO END: "))
        print()
        while n1<=n2:
            for i in range(1,11):
                print(n1,'X',i,'=',n1*i)
            print()
            print('PRESS ENTER FOR NEXT')
            n=input()
            print()
            n1+=1
    elif n==4:
        r=float(input("ENTER RADIUS OF THE CIRCLE: "))
        print()
        print("1. CALCULATE CIRCUMFERENCE")
        print()
        print("2. CALCULATE AREA")
        print()
        ch=int(input("ENTER YOUR CHOICE: "))
        print()
        if ch==1:
            print("THE CIRCUMFERENCE OF THE CIRCLE IS: ",2*3.14*r)
        elif ch==2:
            print("THE AREA OF THE CIRCLE IS: ",3.14*r*r)
        else :
            print('INVALID CHOICE')
    elif n==5:
        print('--------------------------------------------------------------------PALINDROME NO.------------------------------------------------------------------------------------')
        a=int(input('ENTER ANY NO.'))
        print()
        rev=0
        b=a
        while (b!=0):
            digit=b%10;
            b=b//10
            rev=rev*10+digit
        if rev==a:
            print(a,'IS A PALINDROME NO.')
        else:
            print(a,'IS NOT A PALINDROME NO.')
    elif n==6:
        t=input("ENTER THE TEXT YOU WANT TO PRINT IN PATTERN: ")
        print()
        n=int(input("ENTER NO. OF LINE YOU WANT TO PRINT: "))
        print()
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(t,end=" ")
            print()
    elif n==7:
        n=int(input("HOW MANY YEARS? "))
        print()
        print(n,"years is:-")
        print()
        print(365*n, "DAYS")
        print()
        print(365*n*24,"HOURS")
        print()
        print(365*n*24*60,"MINUTES")
        print()
        print(365*n*24*60*60,"SECONDS")
    elif n==8:
        print("JALDI WAHA SE HATO :( ")
        print()
        break
    else:
        print('INVALID CHOICE ENTERED')
    print()
    print("---------------------------------------------------------------------------!!!RESTARTING!!!!!-------------------------------------------------------------------------------")
    print()

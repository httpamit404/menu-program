print('---------------------------------------CODE BY AMIT--------------------------------')
print()
while True:
    print('what do you want to do?')
    print('1. counting of character in a string')
    print('2. replace all vowels in a string with *')
    print('3. reverse a string')
    print('4. check the phone no.')
    print('5. exit')
    ch=int(input('enter ur choice: '))
    if ch==1:
        st=input("ENTER A STRING: ")
        sst=input('ENTER THE CHARACTER TO COUNT: ')
        if sst in st:
            l=st.count(sst)
            print(sst,'OCCURS',l,'times')
        else:
            print(sst,'IS NOT PRESENT IN',st)
    elif ch==2:
        st=input('enter a string: ')
        vow='aeiouAEIOU'
        for i in st:
            if i in vow:
                st.replace(st,'*')
                print(st)
            else:
                print('error!')
    elif ch==3:
        st=input('enter any string to reverse: ')
        st1=st[: :-1]
        print(st1)
    elif ch==4:
        print('example: XXX-XXX-XXXX')
        n=input('enter phone no. in above format: ')
        l=len(n)
        fl=False
        if l==12:
            if n[3]==n[7]=='-':
                if (n[:3]+n[4:7]+n[8:]).isdigit():
                    fl=True
        if fl:
            print('It is valid phone no.')
        else:
            print('It is invalid phone no.')
    elif ch==5:
        print("JALDI WAHA SE HATO :( ")
        break
    else:
        print('INVALID CHOICE ENTERED')
        print()
        print()
        print('---------------------------------------!!!RESTARTING!!!-------------------------------------')
        print()
        print()

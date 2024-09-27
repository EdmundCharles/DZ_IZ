m = input("Enter month's number: from 1 to 12 \n")
if m.isdigit() and 1<=int(m)<=12 :
    m = int(m)
    if 3<=m<=5 :
        print('Spring')
        if m==3:
            print('March')
        elif m==4 :
            print('April')
        else :
            print('May')    
    elif 6<=m<=8 :
        print('Summer')
        if m==6 :
            print('June')
        elif m==7 :
            print('July')
        else :
            print('August')
    elif 9<=m<=11 :
        print('Autumn')
        if m==9 :
            print('September')
        elif m==10 :
            print('October')
        else :
            print('November')
    else :
        print('Winter')
        if m==1 :
            print('January')
        elif m==2 :
            print('February')
        else :
            print('December')      
else :
    print('Please, enter correct values.')
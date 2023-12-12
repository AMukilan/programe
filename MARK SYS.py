m1=int(input("enter the mark of physic:"))
m2=int(input("enter the mark of computer science:"))
m3=int(input("enter the mark of english:"))
avg=(m1+m2+m3)/3
if avg>=80:
    print("GRADE:A")
elif avg>=70 and avg<80:
    print("GRADE:B")
elif avg>=60 and avg<70:
    print("GRADE:C")
elif avg>=50 and avg<60:
    print("GRADE:D")
else:
    print("GRADE:E")
    

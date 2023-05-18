tamil=int(input())
english=int(input())
maths=int(input())
science=int(input())
social=int(input())
total=(tamil+english+maths+science+social)
print(total)
a=total/5.0
if tamil>=35 and english>=35 and maths>=35 and science>=35 and social>=35:
    print("result:pass")
    if a>=95:
        print("Distinction A+:")
    elif a>=90 and a<=95:
        print("Excellent A:")
    elif a>=80 and a<=90:
        print("Very Good B:")
    elif a>=60 and a<=80:
        print("Average c:")
    elif a>=35 and a<=60:
        print("Poor Pass D,try to improve")
    else:
        print("result:fail")

else:
    print("fail")


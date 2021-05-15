city_name=open("question4.txt","r")
for i in city_name:
    if "delhi"  in i :
        A=open("delhi.txt","a")
        A.write(i)
    elif "shimla" in i:
        B=open("shimla.txt","a")
        B.write(i)
    else:
        C=open("other.txt","a")
        C.write(i)



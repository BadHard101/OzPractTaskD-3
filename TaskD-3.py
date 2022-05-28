import re

s1="Шакал разгоняется до скорости 72 км/ч, а гепард до 108 км/ч"

if __name__ == '__main__':

    print(s1)

    s2 = re.findall(r'\d+[^\D]',s1)
    #print(s2)

    for i in s2:
        x = str(int(int(i)*1000/3600))
        s1 = re.sub(i,x,s1)
    print(s1)

    s3 = re.findall(r'\b\w./\w\b',s1)
    #print(s3)

    for i in s3:
        x = "м/с"
        s1 = re.sub(i,x,s1)
    print(s1)
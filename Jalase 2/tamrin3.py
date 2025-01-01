a1=float(input('Please enter first number : '))
a2=float(input('Please enter second number : '))
a3=float(input('Please enter third number : '))
b=(a1+a2+a3)/3
print(b)

if  b < 0 :
    print('manfi')
elif b <= 10 :
    print('miyangin 0 ta 10 ast')
elif b <= 20 :    
    print('miyangin 11 ta 20 ast')
else: 
    print('miyangin bozorgtar az 20 ast')

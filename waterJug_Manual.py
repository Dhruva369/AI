def solution(a,b,ai,bi,af,bf):
  print("\nList Of Operations You can Do:\n")
  print("1.Fill Jug A Completely \n2.Fill Jug B Completely")
  print("3.Empty Jug A Completely \n4.Empty Jug B Completely")
  print("5.Pour From Jug A till Jug B filled Completely or A becomes empty")
  print("6.Pour From Jug B till Jug A filled Completely or B becomes empty")
  print("7.Pour all From Jug B to Jug A")
  print("8.Pour all From Jug A to Jug B\n")
  while ((ai!=af or bi!=bf)):
    op=int(input("Enter the Operation: "))
    if(op==1):
      ai=a
    elif(op==2):
      bi=b
    elif(op==3):
      ai=0
    elif(op==4):
      bi=0
    elif(op==5):
      if(b-bi>ai):
        bi=ai+bi
        ai=0
      else:
        ai=ai-(b-bi)
        bi=b
    elif(op==6):
      if(a-ai>bi):
        ai=ai+bi
        bi=0
      else:
        bi=bi-(a-ai)
        ai=a
    elif(op==7):
      if (a-ai>=bi):
        ai=ai+bi
        bi=0
      else:
        print('Overflow in Jug A')
        pass
    elif(op==8):
      if (b-bi>=ai):
        bi=ai+bi
        ai=0
      else:
        print('Overflow in Jug B')
        pass
    print(ai,bi)


a=int(input("Enter Jug A Capacity: "))
b=int(input("Enter Jug B Capacity: "))
ai=int(input("Initially Water in Jug A: "))
bi=int(input("Initially Water in Jug B: "))
af=int(input("Final State of Jug A: "))
bf=int(input("Final State of Jug B: "))

if (a==af or b==bf or a==bf or b==af):
  solution(a,b,ai,bi,af,bf)
elif (a%b==0 or b%a==0):
  print("No solution")
else:
  solution(a,b,ai,bi,af,bf)

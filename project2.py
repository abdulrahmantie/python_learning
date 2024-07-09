#khalf il kawaliss
import random
aaa=random.random()
bbb=random.randint(1,2)
print("""
welcome to the coin guessing game!
choose a method to toss the coin :
 1_using random.random
 2_using random.randint   
""")
first=input("enter you choise (1 or 2) : ")
if first =="1" or first =="2" :
 print("good")

 second=int(first)
 first2=input("enter you guess (heads or tails): ").lower()
   #il bidaya

 if second ==1 and aaa>0.5 and first2=="heads" :
  print("Congratulations. The answer is true.")
 elif second == 1 and aaa>0.5 and first2=="tails":
  print(""" 
 sorry you lost
 THE computer's coin toss redult was : heads
 """)
 elif second == 1 and aaa<0.5 and first2=="tails" :
  print("Congratulations. The answer is true.")
 elif second == 1 and aaa<0.5 and first2=="heads":
  print(""" 
 sorry you lost
 THE computer's coin toss redult was : tails
 """)

 #nihaya

 elif second == 2 and bbb ==1  and first2=="heads":
  print("Congratulations. The answer is true.")
 elif second ==2 and bbb ==1  and first2=="tails":
  print(""" 
 sorry you lost
 THE computer's coin toss redult was : heads
 """)
 elif second == 2 and bbb== 2 and first2 =="heads":
  print(""" 
 sorry you lost
 THE computer's coin toss redult was : tails
 """)
 elif second == 2 and bbb== 2 and first2 =="tails":
  print("Congratulations. The answer is true.")

 else :
  print("erorr, Promoters' commitment to information")

else :
 print("erorr, Promoters' commitment to information")
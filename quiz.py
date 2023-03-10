#QUiZ
import time
import random
qdict={"Python filename extensions are/is ?":"a","When was python released ?":"b","Who created python programming language?":"a","Which operator has higher precedence in the following list ?":"c","Is python case sensitive when dealing with indentifiers?":"b","Which of the following is used to define a block of code in python ?":"a","Which keyword is used to create a  function in python ?":"b","Which of the following is the truncation division operator in python ?":"d","Which of the following functions is a built in function in python ?":"c","Which of the following statements is used to create an empty set in python ?":"d"}
q=[]
pc=[]
pc1=[]
pc2=[]
sec="sec"
wins=0
points=0
points1=0
points2=0
wins1=0
space=" "
wins2=0
Time=0
time1=0
time2=0
title="WELCOME TO PYTHON PROGRAMMING QUIZ"
print(f'{title:>50}')
print()
print("GAME RULES:")
print("1)There are 10 questions each question carry 1 point")
print("2)Choose a,b,c,d ")
print("3)Single player game: 1 / Multiplayer game: 2")
print()
print()
time.sleep(4)
players=input("ENTER HOW MANY PLAYERS(min=1/max=2):")
while players.isnumeric()!=True or int(players)>2 or int(players)==0:
				if players.isnumeric()==True and int(players)==0:
					print("ERROR!!!MINIMUM PLAYERS SHOULD BE:1")
					players=input("ENTER HOW MANY PLAYERS(min=1/max=2):")
				else:
					print("INVALID INPUT CANNOT BE TAKEN!!!")
					players=input("ENTER HOW MANY PLAYERS(min=1/max=2):")
if int(players)==1:
	print()
	print("YOU SELECTED SINGLE PLAYER GAME!!!")
else:
	print()
	print("YOU SELECTED MULTIPLAYER GAME!!!")
print("")
if players=='1':
						print()
						pname=input("ENTER PLAYER NAME:")
else:
						print()
						pname1=input("ENTER PLAYER 1 NAME:")
						pname2=input("ENTER PLAYER 2 NAME:")
#starting quiz
print()
s=input("DO YOU WANT TO START THE GAME(yes/no):")
while s!='yes' and s!='no' and s!='YES' and s!='NO':
		print("PLEASE TELL YES OR NO")
		print()
		s=input("DO YOU WANT TO START THE GAME(yes/no):")
while s=='yes' or s=='YES':
					#questions loop
					for i in range(10):
						q1=random.choice(list(qdict.keys()))
						while q1 in q !=True:
							q1=random.choice(list(qdict.keys()))
						q.append(q1)
						print()
						print(f'{i+1:>2}){q1}')
						if q1==list(qdict.keys())[0]:#options
							print(f' a).py\n b).pyi\n c).pyc and .pyd\n d)All the above')
						elif q1==list(qdict.keys())[1]:
							print(f' a)1980\n b)1991\n c)1887\n d)2001')
						elif q1==list(qdict.keys())[2]:
							print(f' a)Guido van rossum\n b)Dennis ritchie\n c)James Gosling\n d)Steeve jobs')
						elif q1==list(qdict.keys())[3]:
							print(f' a)%\n b)&\n c)**\n d)>')
						elif q1==list(qdict.keys())[4]:
							print(f' a)No\n b)Yes\n c)Machine dependent\n d)None of the mentioned')
						elif q1==list(qdict.keys())[5]:
							print(f' a)Indentation\n b)Key\n c)Brackets\n d)All of the mentioned')
						elif q1==list(qdict.keys())[6]:
							print(f' a)Function\n b)def\n c)Fun\n d)Define')
						elif q1==list(qdict.keys())[7]:
							print(f' a)|\n b)%\n c)/\n d)//')
						elif q1==list(qdict.keys())[8]:
							print(f' a)factorial()\n b)seed()\n c)print()\n d)sqrt()')
						elif q1==list(qdict.keys())[9]:
							print(' a)( )\n b)[ ]\n c){ }\n d)set()')
						if players=='1':#player choice
							print()
							time.sleep(2)
							run=time.time()
							pchoice=input(f' CHOOSE YOUR OPTION {pname.upper()}:')
							while pchoice>'d' or pchoice.isnumeric()==True or pchoice.isalpha()!=True or len(pchoice)!=1 or pchoice.islower()!=True:
								print(' PLEASE CHOOSE VALID OPTION')
								print()
								pchoice=input(f' CHOOSE YOUR OPTION {pname.upper()}:')
							end=time.time()
							Time+=round(end-run)
							if pchoice==qdict.get(q1):
								pc.append(pchoice)
								pc.append("CORRECT")
								points+=1
							else:
								pc.append(pchoice)
								pc.append("WRONG")
						elif players=='2':
							print()
							time.sleep(2)
							run1=time.time()
							pchoice1=input(f' CHOOSE YOUR OPTION {pname1.upper()}:')#player1 choice
							while pchoice1>'d' or pchoice1.isnumeric()==True or pchoice1.isalpha()!=True or pchoice1.islower()!=True or len(pchoice1)!=1:
								print()
								print(' PLEASE CHOOSE VALID OPTION')
								print()
								pchoice1=input(f' CHOOSE YOUR OPTION {pname1.upper()}:')
							end1=time.time()
							time1+=round(end1-run1)
							if pchoice1==qdict.get(q1):
								pc1.append(pchoice1)
								pc1.append("CORRECT")
								points1+=1
							else:
								pc1.append(pchoice1)
								pc1.append("WRONG")
							print()
							run2=time.time()
							pchoice2=input(f' CHOOSE YOUR OPTION {pname2.upper()}:')#player2 choice
							while pchoice2>'d' or pchoice2.isnumeric()==True or pchoice2.isalpha()!=True or pchoice2.islower()!=True or len(pchoice2)!=1:
								print()
								print(' PLEASE CHOOSE VALID OPTION')
								print()
								pchoice2=input(f' CHOOSE YOUR OPTION {pname2.upper()}:')
							end2=time.time()
							time2+=round(end2-run2)
							if pchoice2==qdict.get(q1):
								pc2.append(pchoice2)
								pc2.append("CORRECT")
								points2+=1
							else:
								pc2.append(pchoice2)
								pc2.append("WRONG")
						
					#printing scores
					if players=='1':
						sr=(points/10)*100
					else:
						sr1=(points1/10)*100
						sr2=(points2/10)*100
					if players=='2':
						if points1>points2:
							wins1+=1
						else:
							wins2+=1
				
					if players=='1':
							print()
							print(f'{pname:>10} (You got {points} points out of 10)')
							print()
							print()
							for i in range(0,20,2):
								print(f' {pc[i]:<3}',end="")
								print(f'- {pc[i+1]:>5}')
							print()
							print()
							print(f'{pname:>10}\n\nPoints{space:>7}: {points}\nTime{space:>8} : {Time} sec\nSuccess rate : {sr}%')
					else:
						print()
						print(f'{pname1:>5} got {points1} points:- {pname2:>15} got {points2} points:-')
						print()
						print()
						for i in range(0,20,2):
							print(f' {pc1[i]:<3}',end="")
							print(f'-{pc1[i+1]:>10}',end="")
							print(f'{pc2[i]:>20}',end="")
							print(f'    -{pc2[i+1]:>10}')
						print()
						print()
						print(f' {pname1:>10}  {pname2:>32}\n\nWins         : {wins1:<20}Wins   {space:>6}: {wins2}\nPoints       : {points1:<16}    Points {space:>6}: {points2}\nTime         : {time1} sec { space:<13}Time   {space:>6}: {time2} sec\nSuccess rate : {sr1}% {space:>13} Success rate : {sr2}%')
						print()
						print()
					if players=='2':
						if points1>points2:
							print(f'{space:<17}{pname1.upper():*^15} IS WINNER!!!!')
						else:
							print(f'{space:<17}{pname2.upper():*^15} IS WINNER!!!!!')
					if players=='1':
						q.clear()
						pc.clear()
						points=0
						Time=0
					else:
						q.clear()
						pc1.clear()
						pc2.clear()
						points1=0
						points2=0
						time1=0
						time2=0
					time.sleep(2)
					print()
					s=input("DO YOU WANT TO PLAY AGAIN??")
					while s!='yes' and s!='no' and s!='YES' and s!='NO':
						print("PLEASE TELL YES OR NO")
						print()
						s=input("DO YOU WANT TO START THE GAME(yes/no):")
				
				
							
								
						
						
		
		
		


	
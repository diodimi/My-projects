import random

def answer(player):
	global list,y
	answer=str(input('Player %d pull or pass?: ' %y))
	sum=0
	for i in player:
			sum+=dict[i[0]]
	while answer=='pull':
		player.append(list.pop())
		print(player)
		sum+=dict[player[-1][0]]
		if sum<21:
			answer=str(input('Pull or pass?: '))
		elif sum>21:
			print('You lost :(')
			sum= 0
			answer=0
	return sum
		
			
		
dict={'K':10,'Q':10,'J':10,1:1,1:11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}
num=[]
y=1
for i in range(1,11):
	num.append(i)
chars=['K','J','Q']
cards=num+chars
colour=['K','H','S','V']
list=[]
for i in cards:
	for j in colour:
		list.append([i,j])
	
random.shuffle(list)
player1=[]
player2=[]
player1.append(list.pop())
player1.append(list.pop())
print(player1)
player2.append(list.pop())
player2.append(list.pop())
print(player2)
answer_1=answer(player1)
y+=1
if answer_1!=0:
	answer_2=answer(player2)
	if answer_1>answer_2:
		print('Player 1 wins!')
	elif answer_1<answer_2:
		print('Player 2 wins!')
	else:
		print('It\'s a draw!')
else:
	print('Player 2 wins!')



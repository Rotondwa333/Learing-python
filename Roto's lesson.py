print('welcome to my quiz game ')
playing = input("Do you want to play?  ")

if playing !='yes':
    quit()

print('okay! lets play:) ')
score = 1
answer = input('who is my lover? ')
if answer.lower() =='arinaho' :
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input('what does he do? ')
if answer.lower() == 'software engineering' :
    print('correct!')
    score += 1
else:
    print('incorrect!')

answer = input('his favourite song? ')
if answer.lower() == 'They not like us' :
    print('correct!')
    score += 1
else:
    print('incorrect!')

print("you got " + str(score) +  " questions correct!")
print("you got " + str((score / 4) * 100 ) +  " %.")



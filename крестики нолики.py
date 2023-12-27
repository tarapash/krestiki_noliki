#Разметим клетки игрового поля следующим образом:
# 1 2 3
# 4 5 6
# 7 8 9
board=[1,2,3,4,5,6,7,8,9]
#Нарисуем поле:
def draw_board():
    print ('_'*13)
    for i in range(3):
        print ('|', board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print ('|'+('_' * 3 + '|') * 3)

#Проверка выигрыша и выиграшные комбинации 
def check_win():
    win = False
    win_combination =  (
		(0,1,2), (3,4,5), (6,7,8),	# горизонтальные линии
		(0,3,6), (1,4,7), (2,5,8),	# вертикальные линии
		(0,4,8), (2,4,6) 			# диагональные линии
	)
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
            win = board[pos[0]]
    return win

#Описание одного хода игрока
def game_step(namber, char):
	if (namber == range(1,10) or board[namber-1] in ('X','O')):
		return False
        
	board[namber-1] = char
	return True

#Ход игры
def game():
    player = 'X' #Пусть первый всегда ходит Х
    step = 1 #Номер хода
    draw_board()
    while step<9 and (check_win()==False):
        namber = (input('Ходит:' + player + '.Введите номер поля, куда хотите сходить: '))
        if(game_step(int(namber), player)):
            print('Ход сделан, смена игрока' )
            if(player == 'X'):
                player = 'O'
            else:
                player = 'X'
            draw_board()
            step += 1
        else:
            print('Невозможный ход, потворите попытку')
    if(step==9):
        print('Ничья :(')
    else:
        print('Победил', check_win())

print('Давайте сыграем в "Крестики-нолики"!')
game()

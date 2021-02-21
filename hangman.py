import random
answer_list = ["cat", "dog", "cow", "mause"]
word = random.choice(answer_list)
word = str(word)

def hangergame(word):
    wrong = 0
    stages = ["",
              "_______      ",
              "|     |      ",
              "|     |      ",
              "|     O      ",
              "|   / | \    ",
              "|    / \     ",
              "|            ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    #なぜ最初にwin=Falseと設定している？
    print("ハンガーゲムヘようこそ")
    while wrong  < len(stages) - 1:
        print("\n")
        msg = "1文字を入力してね"
        char = input(msg)
        if char in rletters:
            num = rletters.index(char)
            board[num] = char
            rletters[num] = "$"
        else:
            wrong += 1
        print("".join(board))
        #もう一度boardの中身を表示している
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            win = True
            break
    if win == False:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け。正解は{}です".format(word))

hangergame(word)

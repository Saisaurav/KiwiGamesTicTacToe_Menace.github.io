from flask import Flask, render_template, request, redirect, url_for
import MENACE_tictactoe

app = Flask(__name__)

# 1. Create a global MENACE instance
menace = MENACE_tictactoe.MENACE()

@app.route('/')
def index():
    return render_template("TicTacToeAI.html")

@app.route('/play', methods=['POST'])
def play():
    Turn = request.json['currentTurn']
    Board = request.json['boardState']
    MoveNumber = request.json['moveNumber']

    if Turn == 'O':
        # Convert all board elements to int!
        board_tuple = tuple(int(x) for x in Board)
        move = menace.play(MoveNumber, board_tuple)
        return str(move)
    else:
        return "Invalid turn. Only 'O' can make a move."

# 2. Add an endpoint to update MENACE after a game
@app.route('/learn', methods=['POST'])
def learn():
    result = request.json['result']  # 1 for win, 0 for draw, -1 for loss
    menace.update(result)
    return "AI updated"

if __name__ == '__main__':
    app.run(debug=True)

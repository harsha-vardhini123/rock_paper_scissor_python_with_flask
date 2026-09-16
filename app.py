from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

# Score
player_score = 0
computer_score = 0
draw_score = 0


def get_result(player, computer):
    if player == computer:
        return "Draw"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "You Win!"

    return "Computer Wins!"


@app.route("/", methods=["GET", "POST"])
def home():
    global player_score, computer_score, draw_score

    player_choice = None
    computer_choice = None
    result = None

    if request.method == "POST":
        player_choice = request.form.get("choice")

        if player_choice in choices:
            computer_choice = random.choice(choices)

            result = get_result(player_choice, computer_choice)

            # Update score
            if result == "You Win!":
                player_score += 1

            elif result == "Computer Wins!":
                computer_score += 1

            else:
                draw_score += 1

    return render_template(
        "index.html",
        player_choice=player_choice,
        computer_choice=computer_choice,
        result=result,
        player_score=player_score,
        computer_score=computer_score,
        draw_score=draw_score
    )


@app.route("/reset")
def reset():
    global player_score, computer_score, draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    return render_template(
        "index.html",
        player_choice=None,
        computer_choice=None,
        result=None,
        player_score=player_score,
        computer_score=computer_score,
        draw_score=draw_score
    )


if __name__ == "__main__":
    app.run(debug=True)

🪨 Rock Paper Scissors – Python Flask

A simple web-based Rock Paper Scissors game built using Python and Flask. The player chooses Rock, Paper, or Scissors, and the computer randomly selects its choice. The application displays the result and maintains the scores for the player, computer, and draws.

🚀 Features

Play Rock Paper Scissors through a web browser

Computer makes a random choice for every round

Displays:

Player choice

Computer choice

Game result

Maintains scores for:

You

Computer

Draws

Reset the score at any time

Responsive and simple user interface

Flask/Jinja templates for dynamic content

🛠️ Technologies Used

Python 3

Flask

HTML5

CSS3

Jinja2

Python random module

📁 Project Structure

Rock_paper_scissor_python_with_flask/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md

The env/ virtual environment is not required to be included in GitHub. It is recommended to create a new virtual environment locally.

⚙️ Installation and Setup

1. Clone the repository

git clone <your-github-repository-url>
cd Rock_paper_scissor_python_with_flask

2. Create a virtual environment

Windows:

python -m venv env

Activate it:

env\Scripts\activate

macOS/Linux:

python3 -m venv env
source env/bin/activate

3. Install Flask

pip install flask

If you have a requirements.txt file, you can install dependencies with:

pip install -r requirements.txt

4. Run the application

python app.py

The Flask development server will start. Open the URL shown in the terminal, usually:

http://127.0.0.1:5000/

🎮 How to Play

Open the application in your browser.

Select one of:

🪨 Rock

📄 Paper

✂️ Scissors

The computer randomly selects its choice.

The application determines the winner.

The score is automatically updated.

Click Reset Score to start the scoreboard again.

🧠 Game Rules

The game follows the standard Rock Paper Scissors rules:

Player

Computer

Result

Rock

Scissors

Player Wins

Paper

Rock

Player Wins

Scissors

Paper

Player Wins

Same choice

Same choice

Draw

All other combinations



Computer Wins

🔄 Application Flow

User selects Rock/Paper/Scissors
              ↓
        Flask receives POST
              ↓
     Computer selects randomly
              ↓
       Winner is calculated
              ↓
          Score updated
              ↓
      Result shown in browser

📌 Main Components

app.py

Contains the Flask application and game logic.

Creates the Flask application

Defines the available choices

Generates the computer's random choice

Determines the winner

Maintains the scores

Handles the / game route

Handles the /reset route

templates/index.html

Contains the user interface using HTML and Jinja2 template syntax.

It displays the scoreboard, game buttons, player/computer choices, and result.

static/style.css

Contains the styling for the application, including:

Page layout

Game card

Buttons

Scoreboard

Result section

Reset button

Responsive layout

🧪 Example

If the player chooses:

Player: Rock
Computer: Scissors

The application displays:

You Win!

and increases the player's score by 1.

🔮 Future Improvements

Possible enhancements include:

Add player names

Add best-of-3 or best-of-5 mode

Store scores using Flask sessions

Add sound effects and animations

Add game history

Add difficulty levels

Add persistent score storage using a database

Deploy the application to a cloud platform

Add automated tests

▶️ How to Run
1. Clone the Repository
git clone https://github.com/harsha-vardhini123/Calculator_using_python_with_flask.git
2. Navigate to the Project Folder
cd Calculator_using_python_with_flask
3. Create a Virtual Environment
python -m venv env
4. Activate the Virtual Environment
Windows PowerShell:

.\env\Scripts\Activate.ps1
Windows Command Prompt:

env\Scripts\activate
5. Install Flask
pip install flask
Or install all project dependencies from requirements.txt:

pip install -r requirements.txt
6. Run the Flask Application
python app.py
The application will start on the local Flask server.

Open your browser and visit:

http://127.0.0.1:5000/
You can also use:

http://localhost:5000/
7. Stop the Application
To stop the Flask server, press:

Ctrl + C
🔒 GitHub .gitignore
# Virtual environment
env/
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Environment variables
.env

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

👩‍💻 Author

Harshavardhini Yeluri

Built as a Python + Flask web development project.

📄 License

This project is intended for learning and educational purposes. You may modify and extend it for your own projects.

## Video Demo

https://github.com/user-attachments/assets/7b66db55-4089-4f7e-8e0e-dd00d86ea805

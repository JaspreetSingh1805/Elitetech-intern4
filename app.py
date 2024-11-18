from flask import Flask, render_template
import random

app = Flask(__name__)

# Dictionary for dice images
dice_images = {
    1: "dice1.png",
    2: "dice2.png",
    3: "dice3.png",
    4: "dice4.png",
    5: "dice5.png",
    6: "dice6.png"
}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

@app.route("/")
def home():
    dice_value = roll_dice()  # Roll the dice
    dice_image = dice_images[dice_value]  # Get the corresponding dice image filename
    return render_template("dice.html", dice_image=dice_image)

if __name__ == "__main__":
    app.run(debug=True)

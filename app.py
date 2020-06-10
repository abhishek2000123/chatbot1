from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, render_template, request
app = Flask(__name__)
#Create a chatbot
bot=ChatBot('Candice')



from chatterbot.trainers import ListTrainer


trainer = ListTrainer(bot)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run()

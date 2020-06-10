from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, render_template, request
app = Flask(__name__)
#Create a chatbot
bot=ChatBot('Candice')


trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
from chatterbot.trainers import ListTrainer

trainer.train(['What is dexconnect','DexConnect is an opportunity discovery and preparation platform that increases the levels of access, aspiration and achievement across schools and communities.'+
'Through a widespread network of schools, libraries, nonprofits, media houses and influencers, DexConnect connects students with global educational'+ 'opportunities that enable them to explore varied academic and co-curricular disciplines and unlock their hidden interests and potential'])
trainer.train(['Who is the founder','Sharad Sagar (born October 24, 1991) is an Indian social entrepreneur and the Founder and CEO of Dexterity Global[1]. He is enlisted in the 2016 Forbes 30 under 30 list as a social entrepreneur.'])
trainer.train(['Initiatives taken by dexconnect','1)India first nonprofitnewspaper partnership'
+
'2)Global opportunities in local languages'+
'DexConnect eliminates the language barrier for'+ 'millions of students by reaching global opportunities to students in local languages'+
])
trainer.train(['What does  dexeterity global ','Dexterity Global is a 21st century leadership movement powering the next generation of leaders for India and the world'])

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

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def show_madlib_form():
    '''Displays madlib form'''

    story_prompts = silly_story.prompts
    return render_template("questions.html", prompts = story_prompts)




@app.get("/results")
def show_madlib():
    '''#Displays created madlib'''
    #need to put the arguments in the story template
    #request.args is key-vaue pairs since i changed the keys to parts of speech back in the html
        #i get in my brain why this works but conceptually

    story_template = silly_story.get_result_text(request.args)

    return render_template("results.html", story = story_template)
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)



@app.get("/")
def render_survey():
    """renders survey template on / page"""
    session["responses"] = []

    return render_template("/survey_start.html", survey=survey)

@app.post("/begin")
def redirect_button():
    """sets button to redirect to /questions/0"""
    """edit"""

    session["responses"].clear()
    return redirect("/questions/0")

@app.get("/questions/<int:num>")
def render_question(num):
    """renders *specified question form on *redirect"""

    question = survey.questions[num]

    return render_template("/question.html", question=question)

@app.post("/answer")
def store_answer():
    """stores answers in response list and redirects to next question; or at end,
    shows completion page with question: answer pairs"""

    # global response
    # global survey comment about it

    answer = request.form["answer"]
    session["responses"] += answer

    next_num = len(session["responses"])


    if (next_num < len(survey.questions)):
        print("I'm in the if")
        print("next num:", next_num)
        print("responses", session["responses"])
        return redirect(f"/questions/{next_num}")
    else:
        print ("I'm in the else")
        response_dictionary = {}
        count = 0
        for question in survey.questions:
            response_dictionary[question.prompt] = session["responses"][count]
            count += 1
        return render_template("/completion.html", response_dictionary=response_dictionary)

    # if (next_num < len(survey.questions)):
    #     return redirect(f"/questions/{next_num}")
    # else:
    #     return render_template("/completion.html",
    #                            survey=survey, response=response)
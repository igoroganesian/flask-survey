from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

response = []
#store question answers here
# ex. ['Yes', 'No', 'Less than $10,000', 'Yes']

@app.get("/")
def render_survey():
    """renders survey template on / page"""

    return render_template("/survey_start.html", survey=survey)

@app.post("/begin")
def redirect_button():
    """sets button to redirect to /questions/0"""

    return redirect("/questions/0")

@app.get("/questions/<int:num>")
def render_question(num):
    """renders specified question form on redirect"""

    question = survey.questions[num]

    return render_template("/question.html", question=question)

@app.post("/questions/<int:num>")
def send_answers(num):

    answer = request.form["answer"]

    global response
    response.append(answer)

    # next_num = num + 1

    # if question[next_num]:

    # return redirect(f"/questions/{next_num}")

@app.post("/answer")
def store_answer():


    return redirect(f"/questions/<int:num>")
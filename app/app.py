from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Transfer Machine Language",
            "Hyper Tool Multi Language",
            "Home Text Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which language is used with Flask?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "What is Docker used for?",
        "options": [
            "Containerization",
            "Photo editing",
            "Word processing",
            "Web browsing"
        ],
        "answer": "Containerization"
    },
    {
        "question": "Which tool automates CI/CD workflows on GitHub?",
        "options": ["GitHub Actions", "MS Paint", "Notepad", "Calculator"],
        "answer": "GitHub Actions"
    },
    {
        "question": "Which command downloads a Git repository?",
        "options": ["git push", "git clone", "git status", "git add"],
        "answer": "git clone"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0

        for i, question in enumerate(questions):
            selected = request.form.get(f"question_{i}")

            if selected == question["answer"]:
                score += 1

        return render_template(
            "result.html",
            score=score,
            total=len(questions)
        )

    return render_template("quiz.html", questions=questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
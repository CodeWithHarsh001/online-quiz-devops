
document.addEventListener("DOMContentLoaded", function () {
    const quizForm = document.querySelector("form");

    if (quizForm) {
        quizForm.addEventListener("submit", function (event) {
            const questions = document.querySelectorAll(".question-card");
            let unanswered = 0;

            questions.forEach(function (question) {
                const selected = question.querySelector(
                    'input[type="radio"]:checked'
                );

                if (!selected) {
                    unanswered++;
                }
            });

            if (unanswered > 0) {
                event.preventDefault();
                alert("Please answer all questions before submitting!");
            }
        });
    }

    console.log("Online Quiz System JavaScript loaded successfully.");
});


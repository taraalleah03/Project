const puzzles = {
    "What is 25 x 11? ": "171",
    "What color do you get by mixing red and blue? ": "purple",
    "What is the capital of France? ": "paris",
    "How many legs does a cow have? ": "4",
    "What is 10 - 3? ": "7",
    "What is 'Thank you' in Finnish ": "kiitos",
    "Is Cleopatra from India? ": "no",
    "What language do Japanese people speak ": "japanese"
};

let lives = 3;
let timeLeft = 90;
let questionCount = 0;

setInterval(() => {
    timeLeft--;
    document.getElementById("timer").textContent = "Time left: " + timeLeft + "s";

    if (timeLeft <= 0) {
        document.getElementById("timer").textContent = "Time left: 0s";
        document.getElementById("message").textContent = "You ran out of time! The farmer has captured the cow!";
        document.getElementById("answerInput").disabled = true;
        document.getElementById("submitButton").disabled = true;
    }
}, 1000);

function selectRandom(item) {
    return Math.floor(Math.random() * item);
}
const puzzleKeys = Object.keys(puzzles);

let randomNumber = selectRandom(puzzleKeys.length);
let selectedQuestion = puzzleKeys[randomNumber];
let selectedAnswer = puzzles[selectedQuestion];

document.getElementById("question").textContent = selectedQuestion;

let currentPuzzle = {
    question: selectedQuestion,
    answer: selectedAnswer,
}

document.getElementById("lives").textContent = "Lives: " + lives;

document.getElementById("submitButton").addEventListener("click", () => {
    const answer = document.getElementById("answerInput").value.toLowerCase();

    if (answer === currentPuzzle.answer) {
        document.getElementById("message").textContent = "Correct!"
    }
    else {
        document.getElementById("message").textContent = "Wrong! You lose a life!"
        lives--;
        document.getElementById("lives").textContent = "Lives: " + lives;

        if (lives <= 0) {
            document.getElementById("message").textContent = "Game Over! the Farmer has captured the cow!";
            document.getElementById("answerInput").disabled = true;
            document.getElementById("submitButton").disabled = true;
        }
    }
})cc
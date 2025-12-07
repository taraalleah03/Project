let timeLeft = 90;
let timerInterval = null;

function showTimer() {
    document.getElementById("timer").textContent = "Time left: " + timeLeft + "s";
}

let countries = {};
let answer = null;
let hints_list = [];
let currentHintIndex = 0;

document.getElementById("start_btn").onclick = async () => {

    if (!timerInterval) {
        timerInterval = setInterval(() => {

            timeLeft--;

            if (timeLeft <= 0) {
                document.getElementById("timer").textContent = "Time left: 0s";
                document.getElementById("message").textContent = "GAME OVER! Time ran out!";

                document.getElementById("answerInput").disabled = true;
                document.getElementById("submitButton").disabled = true;
                document.getElementById("guess_ans").disabled = true;
                document.getElementById("guess_btn").disabled = true;

                clearInterval(timerInterval);
            }
            showTimer();
        }, 1000);
    }

    showTimer();

    const res = await fetch("http://127.0.0.1:5000/api/start");
    const data = await res.json();

    countries = data.countries;

    const countryNames = Object.keys(countries);

    answer = countryNames[Math.floor(Math.random() * countryNames.length)];

    hints_list = [
        "Continent: " + countries[answer].continent,
        "City: " + countries[answer].city];

    currentHintIndex = 0;

    document.getElementById("countries").innerHTML =
        "Countries to choose from:<br>" + countryNames.join("<br>");

    document.getElementById("result").textContent = "";
    document.getElementById("hint").textContent = "";
    document.getElementById("guess_ans").value = "";
};

document.getElementById("guess_btn").onclick = () => {
    const guess = document.getElementById("guess_ans").value.trim();
    if (!guess) return;

    if (guess.toLowerCase() === answer.toLowerCase()) {
        document.getElementById("result").textContent = "Correct! Yipee, You found the country with the best grass!";
        document.getElementById("hint").textContent = "";
    } else {
        document.getElementById("result").textContent = "YOU MAY NOW GUESS ANOTHER COUNTRY.";

        if (currentHintIndex < hints_list.length) {
            document.getElementById("hint").textContent = hints_list[currentHintIndex];
            currentHintIndex++;
        } else {
            document.getElementById("hint").textContent = "No more hints!";
        }
        loadPuzzle()
    }

    document.getElementById("guess_ans").value = "";
};

const puzzles = {
    "What is 25 x 11?": "275",
    "What color do you get by mixing red and blue?": "purple",
    "What is the capital of France?": "paris",
    "How many legs does a cow have?": "4",
    "What is 10 - 3?": "7",
    "What is 'Thank you' in Finnish?": "kiitos",
    "Is Cleopatra from India?": "no",
    "What language do Japanese people speak?": "japanese"
};

let lives = 3;
let puzzleActive = false;
let currentPuzzle = null;

function loadPuzzle() {
    showTimer()
    puzzleActive = true;

    document.getElementById("guessSection").style.display = "none";
    document.getElementById("puzzleSection").style.display = "block";

    const keys = Object.keys(puzzles);
    const randomValue = Math.floor(Math.random() * keys.length);
    const question = keys[randomValue];
    const answer = puzzles[question];

    currentPuzzle = {
        question,
        answer
    };

    document.getElementById("question").textContent = question;
    document.getElementById("answerInput").value = "";
    document.getElementById("message").textContent = "";
    document.getElementById("lives").textContent = "Lives: " + lives;

}

document.getElementById("submitButton").onclick = () => {
    const userAnswer = document.getElementById("answerInput").value.toLowerCase().trim();

    if (userAnswer === currentPuzzle.answer.toLowerCase()) {
        document.getElementById("message").textContent = "Correct! You may now guess another country.";
        puzzleActive = false;

        document.getElementById("puzzleSection").style.display = "none";
        document.getElementById("guessSection").style.display = "block";
    } else {
        lives--;
        document.getElementById("lives").textContent = "Lives: " + lives;

        if (lives <= 0) {
            document.getElementById("message").textContent = "GAME OVER! The farmer captured the cow!";
            document.getElementById("answerInput").disabled = true;
            document.getElementById("submitButton").disabled = true;
            document.getElementById("guess_ans").disabled = true;
            document.getElementById("guess_btn").disabled = true;
        } else {
            document.getElementById("message").textContent = "Wrong! Try again!";
        }
    }
};
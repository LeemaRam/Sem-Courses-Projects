let currentQuestion = 0;
const answers = {};

function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.getElementById(pageId).classList.add('active');
}

function startQuiz() {
    currentQuestion = 0;
    showPage('quiz-page');
    displayQuestion();
}

function displayQuestion() {
    const question = questions[currentQuestion];
    document.getElementById('question-text').textContent = question.text;
    document.getElementById('question-number').textContent = `Question ${currentQuestion + 1} of ${questions.length}`;
    
    // Update navigation buttons
    document.getElementById('prev-btn').disabled = currentQuestion === 0;
    document.getElementById('next-btn').textContent = currentQuestion === questions.length - 1 ? 'Finish' : 'Next';
    
    // Reset option selection
    document.querySelectorAll('.option').forEach(option => {
        option.classList.remove('selected');
        if (answers[currentQuestion] === option.dataset.value) {
            option.classList.add('selected');
        }
    });
}

function selectOption(event) {
    if (!event.target.classList.contains('option')) return;
    
    document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
    event.target.classList.add('selected');
    answers[currentQuestion] = event.target.dataset.value;
}

function previousQuestion() {
    if (currentQuestion > 0) {
        currentQuestion--;
        displayQuestion();
    }
}

function nextQuestion() {
    if (!answers[currentQuestion]) {
        alert('Please select an answer before proceeding.');
        return;
    }

    if (currentQuestion === questions.length - 1) {
        showResults();
    } else {
        currentQuestion++;
        displayQuestion();
    }
}

function showResults() {
    showPage('results-page');
}

function restartQuiz() {
    currentQuestion = 0;
    Object.keys(answers).forEach(key => delete answers[key]);
    showPage('home-page');
}

// Event Listeners
document.querySelector('.options').addEventListener('click', selectOption);

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    showPage('home-page');
});
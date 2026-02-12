const questions = [
    {
        id: 1,
        text: "I enjoy solving complex problems and puzzles"
    },
    {
        id: 2,
        text: "I prefer working with people rather than working alone"
    },
    {
        id: 3,
        text: "I am comfortable taking risks and making important decisions"
    },
    {
        id: 4,
        text: "I enjoy creating and expressing myself artistically"
    },
    {
        id: 5,
        text: "I like working with machines and technical equipment"
    },
    {
        id: 6,
        text: "I am good at explaining things to others"
    },
    {
        id: 7,
        text: "I enjoy analyzing data and finding patterns"
    },
    {
        id: 8,
        text: "I am interested in helping others solve their problems"
    },
    {
        id: 9,
        text: "I prefer having a structured and organized routine"
    },
    {
        id: 10,
        text: "I enjoy learning about new technologies and innovations"
    },
    {
        id: 11,
        text: "I enjoy working in a fast-paced environment"
    },
    {
        id: 12,
        text: "I am interested in understanding how things work"
    },
    {
        id: 13,
        text: "I like to lead and inspire others"
    },
    {
        id: 14,
        text: "I am passionate about protecting the environment"
    },
    {
        id: 15,
        text: "I enjoy working with numbers and financial data"
    },
    {
        id: 16,
        text: "I am good at negotiating and persuading others"
    },
    {
        id: 17,
        text: "I like to work on creative projects"
    },
    {
        id: 18,
        text: "I am interested in healthcare and helping people"
    },
    {
        id: 19,
        text: "I enjoy working with my hands and building things"
    },
    {
        id: 20,
        text: "I am interested in learning about different cultures"
    }
];let currentQuestion = 0;
const answers = {};
let shuffledQuestions = [];

function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
    document.getElementById(pageId).classList.add('active');
}

function startQuiz() {
    currentQuestion = 0;
    shuffledQuestions = shuffleArray(questions);
    showPage('quiz-page');
    displayQuestion();
}

function shuffleArray(array) {
    const shuffled = array.slice();
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

function displayQuestion() {
    const question = shuffledQuestions[currentQuestion];
    document.getElementById('question-text').textContent = question.text;
    document.getElementById('question-number').textContent = `Question ${currentQuestion + 1} of ${shuffledQuestions.length}`;
    
    // Update navigation buttons
    document.getElementById('prev-btn').disabled = currentQuestion === 0;
    document.getElementById('next-btn').textContent = currentQuestion === shuffledQuestions.length - 1 ? 'Finish' : 'Next';
    
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

    if (currentQuestion === shuffledQuestions.length - 1) {
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
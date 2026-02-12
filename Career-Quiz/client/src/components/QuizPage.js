import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import questions from '../questions';

function QuizPage() {
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [answers, setAnswers] = useState({});
    const history = useHistory();

    const handleOptionClick = (value) => {
        setAnswers({ ...answers, [currentQuestion]: value });
    };

    const handleNextClick = () => {
        if (!answers[currentQuestion]) {
            alert('Please select an answer before proceeding.');
            return;
        }

        if (currentQuestion === questions.length - 1) {
            history.push('/results');
        } else {
            setCurrentQuestion(currentQuestion + 1);
        }
    };

    const handlePrevClick = () => {
        if (currentQuestion > 0) {
            setCurrentQuestion(currentQuestion - 1);
        }
    };

    return (
        <div className="container mt-5">
            <div className="quiz-container neon-card p-4">
                <h2 className="neon-heading">Career Assessment Quiz</h2>
                <p className="quiz-instruction">Answer honestly for the most accurate results</p>
                
                <div className="question-container">
                    <p id="question-text">{questions[currentQuestion].text}</p>
                    <div className="options">
                        {['STRONGLY_AGREE', 'AGREE', 'NEUTRAL', 'DISAGREE', 'STRONGLY_DISAGREE'].map((option) => (
                            <button
                                key={option}
                                className={`option btn btn-outline-primary ${answers[currentQuestion] === option ? 'selected' : ''}`}
                                onClick={() => handleOptionClick(option)}
                            >
                                {option.replace('_', ' ')}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="navigation mt-4">
                    <button className="btn btn-secondary" onClick={handlePrevClick} disabled={currentQuestion === 0}>Previous</button>
                    <span id="question-number" className="mx-3">Question {currentQuestion + 1} of {questions.length}</span>
                    <button className="btn btn-primary" onClick={handleNextClick}>{currentQuestion === questions.length - 1 ? 'Finish' : 'Next'}</button>
                </div>
            </div>
        </div>
    );
}

export default QuizPage;

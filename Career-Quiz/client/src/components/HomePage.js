import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
    return (
        <div className="container text-center mt-5">
            <header className="hero">
                <div className="neon-text">
                    <i className="fas fa-rocket icon-float"></i>
                    <h1>Discover Your Perfect Career Path</h1>
                    <i className="fas fa-lightbulb icon-float"></i>
                </div>
                <p>Take our comprehensive career assessment quiz to find the career path that aligns with your personality, skills, and interests.</p>
                <Link to="/quiz" className="btn btn-primary btn-lg mt-3">Start Quiz</Link>
            </header>
            
            <section className="info-section mt-5">
                <h2 className="neon-heading">Why Career Choice Matters</h2>
                <div className="row">
                    <div className="col-md-3">
                        <div className="feature neon-card p-3">
                            <i className="fas fa-heart feature-icon"></i>
                            <h3>Job Satisfaction</h3>
                            <p>Choose a career that aligns with your interests and values for long-term satisfaction.</p>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="feature neon-card p-3">
                            <i className="fas fa-balance-scale feature-icon"></i>
                            <h3>Work-Life Balance</h3>
                            <p>Different careers offer different lifestyle opportunities. Find what works for you.</p>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="feature neon-card p-3">
                            <i className="fas fa-chart-line feature-icon"></i>
                            <h3>Growth Potential</h3>
                            <p>Consider careers with opportunities for advancement and skill development.</p>
                        </div>
                    </div>
                    <div className="col-md-3">
                        <div className="feature neon-card p-3">
                            <i className="fas fa-piggy-bank feature-icon"></i>
                            <h3>Financial Security</h3>
                            <p>Understanding career prospects helps in planning for a stable financial future.</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
}

export default HomePage;

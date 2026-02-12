import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './HomePage';
import QuizPage from './QuizPage';
import ResultsPage from './ResultsPage';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={HomePage} />
                    <Route path="/quiz" component={QuizPage} />
                    <Route path="/results" component={ResultsPage} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;

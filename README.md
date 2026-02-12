# Career Suggestion Quiz

## Overview
The Career Suggestion Quiz is a web application designed to help users discover their ideal career path based on their personality, skills, and interests. The quiz consists of a series of questions, and based on the user's responses, it provides career recommendations.

## Features
- Neon-themed UI: A visually appealing neon-themed user interface.
- Responsive Design: The application is fully responsive and works on various devices.
- Question Shuffling: Questions are shuffled each time the quiz is started to ensure a unique experience.
- Career Recommendations: Provides personalized career recommendations based on quiz responses.
- Next Steps Guidance: Offers actionable next steps for users to pursue their recommended careers.
- **User Authentication**: Secure user login and registration using Node.js and Express.js.
- **Database Integration**: Store user data and quiz results in MongoDB.
- **Bootstrap Integration**: Enhanced UI with Bootstrap components and styles.
- **React Integration**: Modern front-end framework for building interactive user interfaces.

## Technologies Used
- HTML
- CSS
- JavaScript
- Bootstrap
- React
- Node.js
- Express.js
- MongoDB

## File Structure
```
csa/
├── client/
│   ├── public/
│   │   ├── index.html
│   │   └── ...
│   ├── src/
│   │   ├── components/
│   │   │   ├── App.js
│   │   │   ├── HomePage.js
│   │   │   ├── QuizPage.js
│   │   │   ├── ResultsPage.js
│   │   │   └── ...
│   │   ├── App.css
│   │   ├── index.js
│   │   └── ...
│   ├── package.json
│   └── ...
├── server/
│   ├── app.js
│   ├── routes/
│   │   └── api.js
│   └── models/
│       └── User.js
├── package.json
└── README.md
```

## Getting Started
To get started with the Career Suggestion Quiz, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:
    ```sh
    cd csa
    ```

3. **Install server dependencies**:
    ```sh
    cd server
    npm install
    ```

4. **Start the server**:
    ```sh
    npm start
    ```

5. **Navigate to the client directory**:
    ```sh
    cd ../client
    ```

6. **Install client dependencies**:
    ```sh
    npm install
    ```

7. **Start the client**:
    ```sh
    npm start
    ```

8. **Open `http://localhost:3000` in your web browser**.

## Detailed Explanation

### client/public/index.html
The main HTML file that structures the web application.

### client/src/components/App.js
The main React component that sets up the application routes and structure.

### client/src/components/HomePage.js
The React component for the home page, including the introduction and start button.

### client/src/components/QuizPage.js
The React component for the quiz page, displaying quiz questions and options.

### client/src/components/ResultsPage.js
The React component for the results page, showing career recommendations based on quiz responses.

### client/src/App.css
Contains all the styles for the web application, including:
- Neon Theme: Defines neon colors and applies them to various elements.
- Responsive Design: Ensures the application looks good on different screen sizes.
- Bootstrap Integration: Utilizes Bootstrap classes for enhanced styling.

### server/app.js
The main server file that sets up the Node.js and Express.js server, connects to MongoDB, and defines routes.

### server/routes/api.js
Defines the API routes for user authentication and quiz data handling.

### server/models/User.js
Defines the User model for MongoDB, including schema and methods for user data.

## Usage
1. Start the Quiz: Click the "Start Quiz" button on the home page.
2. Answer Questions: Select an option for each question and navigate using the "Next" and "Previous" buttons.
3. View Results: After answering all questions, view your career recommendations on the results page.
4. Restart Quiz: Click the "Take Quiz Again" button to restart the quiz.

## Customization
To customize the quiz, you can:
- Add/Remove Questions: Modify the `questions.js` file to add or remove questions.
- Change Styles: Update the `App.css` file to change the look and feel of the application.
- Modify Logic: Update the React components to change the quiz logic or add new features.
- Extend Server Functionality: Update the `server` files to add new API routes or database interactions.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or feedback, please contact [leemaramf22@nutech.edu.pk].


### Test Case 1: Home Page Load
**Test Case ID:** TC001  
**Description:** Verify that the home page loads correctly with all elements visible.  
**Preconditions:** None  
**Test Steps:**
1. Open the website.
2. Verify that the home page is displayed.
3. Check that the hero section, including the title, icons, and start button, is visible.
4. Verify that the info section with features is displayed.
**Expected Result:** The home page should load with all elements visible and correctly styled.

### Test Case 2: Start Quiz Button
**Test Case ID:** TC002  
**Description:** Verify that clicking the "Start Quiz" button navigates to the quiz page.  
**Preconditions:** Home page is loaded.  
**Test Steps:**
1. Open the website.
2. Click the "Start Quiz" button.
**Expected Result:** The quiz page should be displayed with the first question visible.

### Test Case 3: Answer Selection
**Test Case ID:** TC003  
**Description:** Verify that selecting an answer highlights the selected option.  
**Preconditions:** Quiz page is loaded.  
**Test Steps:**
1. Start the quiz.
2. Click on any of the answer options (e.g., "Strongly Agree").
**Expected Result:** The selected option should be highlighted, and other options should not be highlighted.

### Test Case 4: Navigation Buttons
**Test Case ID:** TC004  
**Description:** Verify the functionality of the "Previous" and "Next" buttons.  
**Preconditions:** Quiz page is loaded.  
**Test Steps:**
1. Start the quiz.
2. Answer the first question and click "Next".
3. Click "Previous".
**Expected Result:** The "Next" button should navigate to the next question, and the "Previous" button should navigate back to the previous question.

### Test Case 5: Finish Quiz
**Test Case ID:** TC005  
**Description:** Verify that completing the quiz navigates to the results page.  
**Preconditions:** Quiz page is loaded.  
**Test Steps:**
1. Start the quiz.
2. Answer all questions.
3. Click the "Finish" button on the last question.
**Expected Result:** The results page should be displayed with career recommendations.

### Test Case 6: Restart Quiz
**Test Case ID:** TC006  
**Description:** Verify that clicking the "Take Quiz Again" button on the results page restarts the quiz.  
**Preconditions:** Results page is loaded.  
**Test Steps:**
1. Complete the quiz and navigate to the results page.
2. Click the "Take Quiz Again" button.
**Expected Result:** The quiz should restart, and the first question should be displayed.

### Test Case 7: Shuffle Questions
**Test Case ID:** TC007  
**Description:** Verify that the questions are displayed in a random order each time the quiz is started.  
**Preconditions:** None  
**Test Steps:**
1. Start the quiz and note the order of the questions.
2. Complete the quiz and restart it.
3. Note the order of the questions again.
**Expected Result:** The order of the questions should be different each time the quiz is started.

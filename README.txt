Mental Anguish README - Author: Devin Kinkead

How to open the program:

- To begin the program: Run the gui.py file 
- A list of the required python modules are provided in requirements.txt

---------------------------------------------------------------------------------------------------------------
For reduce technical jargon, all references to the provided "questions.json" file will be simply the "data file" 

----------------------------------------------------------------------------------------------------------------
Using the Program:

Main Menu:

Each time you reach the main menu, you will see an updated list of questions from the data file provided. Additionally, you will be given the option to use the following 5 features: Add Question, Delete Question, Search Questions, Edit Question, and Play Now. 

Instructions on how to use each of the 5 features are provided below, in the order they are presented in the main menu (left to right).

If you want to exit the program, you can select "File" and then "Exit" to immediately and cleanly close the program. 
You can do this at any point besides playing the Trivia Game itself ("Play Now" in the main menu). 
Currently, If you try to close the program during game play, you will exit at the end of the game. 
---------------------------------------------------------------------------------------------------------------------------
How to Add a Question:
	You have the ability to create your own questions on an individual basis. You can do so with 	the following steps:
	
	1. Select the "Add Question" button. 
	2. Fill out all available entries that appear 
	- Question Text, Question Value, Choices 1-4, Correct Answer #, Correct Feedback and Incorrect Feedback"
	- Note: 'Question Value' is a selection of the Number of points your question will be worth. You can only select a value of 1-3. 		
	- Additionally, when entering the 'Correct Answer #', select the radio button next to the choice number of the correct answer 
	(If Choice 1 is correct, then select the radio button next to the number 1). 

	
	3. Press the "Submit" button. 
	Your question will be automatically save to the provided data file, and you will return to the main menu. You will see your new question 
	at the bottom of the menu box.
	
	Note: At any time in the question entry process, you can select "Cancel". Nothing will be saved, and you will return to the Main Menu.
-------------------------------------------------------------------------------------------------------------------------	
How to Delete a question:
	You have the option to delete any question with 3 easy steps:
	1. In the main menu, find the question you want to delete within the box.
	2. Click on the question you want to delete
	3. Press the "Delete Question" button.
	
	You question will be deleted from the data file, and the box in the main menu will automatically reflect the deleted question.
------------------------------------------------------------------------------------------------------------------------	
How to Search for a question:
	You have the ability to find questions based on their Question Text, Choices, or Correct/Incorrect Feedback within the question. 
	You can do so through the following steps:
	1. In the Main Menu, press the "Search Questions" button
	2. In the "Search Term" entry box, type in your search term
	3. Press Search. If any questions have an attribute that is at least 51% matching to the search term 
	(Whether it is Question Text, Choices, or Correct/Incorrect feedback), the question text of that question will appear in the box.
	4. To return to the main menu, press Cancel
------------------------------------------------------------------------------------------------------------------------
How to Edit a question:
	You can edit any questions that are available in the main menu. You can do so through the following steps.
	1. In the main menu, find the question you want to edit within the box.
	2. Click on the question you want to edit.
	3. Press the "Edit Question" button
	4. Make any changes that you want to make in the entry box.
	5. Press Submit. The data file and the box in the main menu will be updated.
	Note: If you change your mind about editing a question, press "Cancel", and no changes will be made. You will return to the main menu.
	
	Note: If you change the question text while editing your question, 
	a new question will be created, and it will show up as the last question on the bottom of the Main Menu box 
	(you may need to use the scroll bar to see it). 
	If this happens, You can follow the steps under "How to Delete a question" to delete the old question.
	
---------------------------------------------------------------------------------------------------------------------
How to Play the Trivia Game:
	With this program, you can play a 3-question trivia game as many times as you like. 
	The program will select 3 random, but unique questions from the data file to present to you.
	
	1. In the main menu, press the "Play Now" button.
	2. The first question will be presented, as well as 4 answer choices, the number of questions left, and the 
	total number of points you have earned. 
	Select the radio button next to the answer you believe is correct.
	3. Click "Submit"
	4a. If you are correct, you will see a smiley face, with feedback specific to the question ("Correct Feedback"), as well as the number of points
	you have earned for the question (1-3). Press the "OK" button to continue.
	4b. If you are incorrect, you will see a similar format, but with a frowny face, the question's "Incorrect Feedback", as well as the message "0 points earned" for the question. 
	Press the "OK" button to continue.
	
	
	5. Repeat steps 2-4 for the next two questions.
	6. After answering 3 questions, you will see a "Game Over" screen with your total score. Press "Main Menu" to return to the main menu.
	
	
	
--------------------------------------------------------------------------------------------------------------------
	

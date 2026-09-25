# General Knowledge Quiz

A simple Python-based General Knowledge Quiz that asks the user five multiple-choice questions and calculates the final score based on the correct answers.

## Features

* Contains 5 multiple-choice questions.
* Accepts answers in uppercase or lowercase.
* Calculates the score automatically.
* Displays the final score out of 5.
* Provides feedback based on the user's score.
* Beginner-friendly Python project.

## Technologies Used

* Python

## How It Works

1. The program displays the General Knowledge Quiz title.
2. The score starts from 0.
3. The program displays five multiple-choice questions.
4. The user enters an answer for each question.
5. The `lower()` method converts the answer to lowercase.
6. If the answer is correct, the score increases by 1.
7. After all five questions, the final score is displayed.
8. The program gives feedback based on the score.

## Code

```python
print("===== GENERAL KNOWLEDGE QUIZ =====")
score = 0

# Question 1
print("\n1. Who is the national poet of Pakistan?")
print("a) Allama Iqbal")
print("b) Faiz Ahmed Faiz")
print("c) Mirza Ghalib")
ans = input("Enter answer: ")
if ans.lower() == "a":
    score += 1

# Question 2
print("\n2. Imran Khan served as the Prime Minister of Pakistan from:")
print("a) 2013 to 2017")
print("b) 2018 to 2022")
print("c) 2020 to 2024")
ans = input("Enter answer: ")
if ans.lower() == "b":
    score += 1

# Question 3
print("\n3. Which is the largest continent in the world?")
print("a) Africa")
print("b) Europe")
print("c) Asia")
ans = input("Enter answer: ")
if ans.lower() == "c":
    score += 1

# Question 4
print("\n4. Imran Khan is famous for winning the Cricket World Cup in which year?")
print("a) 1987")
print("b) 1992")
print("c) 1996")
ans = input("Enter answer: ")
if ans.lower() == "b":
    score += 1

# Question 5
print("\n5. Which is the fastest land animal?")
print("a) Lion")
print("b) Horse")
print("c) Cheetah")
ans = input("Enter answer: ")
if ans.lower() == "c":
    score += 1

print("\n===== RESULT =====")
print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")
```

## Example Output

```text
===== GENERAL KNOWLEDGE QUIZ =====

1. Who is the national poet of Pakistan?
a) Allama Iqbal
b) Faiz Ahmed Faiz
c) Mirza Ghalib
Enter answer: a

2. Imran Khan served as the Prime Minister of Pakistan from:
a) 2013 to 2017
b) 2018 to 2022
c) 2020 to 2024
Enter answer: b

===== RESULT =====
Your Score: 5 / 5
Excellent!
```

## Concepts Practiced

This project helped me practice:

* `print()`
* `input()`
* Variables
* `if`, `elif`, and `else`
* Comparison operators
* `lower()` string method
* Incrementing a variable using `+=`
* User input
* Multiple-choice questions
* Score calculation

## How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file named:

```text
general_knowledge_quiz.py
```

3. Open the terminal in the project folder.
4. Run the following command:

```bash
python general_knowledge_quiz.py
```

5. Answer each question by entering `a`, `b`, or `c`.

## Clone Repository

To clone this repository to your local computer, run:

```bash
git clone https://github.com/hamnanadeem04/Python_General_Knowledge_Quiz.git
```

Then move into the project folder:

```bash
cd YOUR-REPOSITORY-NAME
```

Run the quiz:

```bash
python general_knowledge_quiz.py
```

## Project Purpose

This project was created as a beginner Python exercise to practice conditional statements, user input, string manipulation, and score calculation while building a simple interactive quiz.

## Author

Hamna Khan

Computer Science Student

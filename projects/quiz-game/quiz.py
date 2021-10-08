import json
import random

QUESTIONS = [
    {"q": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": 1},
    {"q": "Which planet is closest to the Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": 2},
    {"q": "What year did the World Wide Web launch?", "options": ["1989", "1991", "1993", "1995"], "answer": 1},
    {"q": "Which language is used for web styling?", "options": ["HTML", "Python", "CSS", "JavaScript"], "answer": 2},
    {"q": "How many bits in a byte?", "options": ["4", "8", "16", "32"], "answer": 1},
    {"q": "What does CPU stand for?", "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility"], "answer": 1},
    {"q": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": 1},
    {"q": "What is 2^10?", "options": ["512", "1000", "1024", "2048"], "answer": 2},
]

def run_quiz(num_questions=5):
    questions = random.sample(QUESTIONS, min(num_questions, len(QUESTIONS)))
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['q']}")
        for j, opt in enumerate(q["options"]):
            print(f"  {j}: {opt}")
        answer = int(input("Answer: "))
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Answer: {q['options'][q['answer']]}")
    print(f"\nScore: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()

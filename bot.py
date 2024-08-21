# Quiz Bot

import random

# Quiz questions and answers
quiz_questions = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct": 0},
    {"question": "What is the largest planet in our solar system?", "answers": ["Jupiter", "Earth", "Saturn"], "correct": 0},
    {"question": "Who painted the Mona Lisa?", "answers": ["Leonardo da Vinci", "Michelangelo", "Raphael"], "correct": 0},
    {"question": "What is the smallest country in the world?", "answers": ["Vatican City", "Monaco", "Nauru"], "correct": 0},
    {"question": "Who wrote Romeo and Juliet?", "answers": ["William Shakespeare", "Jane Austen", "Charles Dickens"], "correct": 0},
]

# User's answers
user_answers = {}

def record_current_answer(user_id, question_id, answer):
    user_answers[user_id] = user_answers.get(user_id, {})
    user_answers[user_id][question_id] = answer

def get_next_question(user_id, current_question_id):
    if current_question_id < len(quiz_questions):
        return quiz_questions[current_question_id]
    else:
        return None

def generate_final_response(user_id):
    score = sum(1 for question_id, answer in user_answers[user_id].items() if quiz_questions[question_id]["correct"] == answer)
    return f"Your final score is {score} out of {len(quiz_questions)}!"

def main():
    user_id = 1
    current_question_id = 0

    print("Welcome to the Quiz Bot!")
    print("Please answer the questions with the number of your answer.")

    while True:
        question = get_next_question(user_id, current_question_id)
        if question is None:
            print(generate_final_response(user_id))
            break
        print(f"\nQuestion {current_question_id+1}: {question['question']}")
        for i, answer in enumerate(question["answers"]):
            print(f"{i+1}. {answer}")
        user_answer = int(input("Enter the number of your answer: ")) - 1
        record_current_answer(user_id, current_question_id, user_answer)
        current_question_id += 1

if __name__ == "__main__":
    main()


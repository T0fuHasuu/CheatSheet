import random

def python_quiz():
    questions = [
        {
            "question": "What is the correct way to declare a variable in Python?",
            "options": ["var x = 10", "x = 10", "int x = 10", "declare x = 10"],
            "answer": "x = 10"
        },
        {
            "question": "Which of these is a valid Python data type?",
            "options": ["float", "number", "digit", "string_num"],
            "answer": "float"
        },
        {
            "question": "What will the following code return? bool('False')",
            "options": ["True", "False", "Error", "None"],
            "answer": "True"
        },
        {
            "question": "What is the output of 5 + 3 * 2?",
            "options": ["16", "13", "11", "10"],
            "answer": "11"
        },
        {
            "question": "What is the syntax for a function in Python?",
            "options": ["function myFunc():", "def myFunc():", "void myFunc():", "func myFunc():"],
            "answer": "def myFunc():"
        },
        {
            "question": "Which of these is a valid Python list?",
            "options": ["(1, 2, 3)", "{1, 2, 3}", "[1, 2, 3]", "1, 2, 3"],
            "answer": "[1, 2, 3]"
        },
        {
            "question": "How can you loop through a list in Python?",
            "options": [
                "for i in range(list):",
                "while i in list:",
                "for i in list:",
                "for i loop list:"
            ],
            "answer": "for i in list:"
        },
        {
            "question": "What is the output of lambda x: x + 10 when x=5?",
            "options": ["5", "10", "15", "None"],
            "answer": "15"
        },
        {
            "question": "How do you add a new element to a set?",
            "options": ["set.add(element)", "set.append(element)", "set.push(element)", "set.insert(element)"],
            "answer": "set.add(element)"
        },
        {
            "question": "How do you create a dictionary in Python?",
            "options": ["{key: value}", "[key: value]", "(key: value)", "key -> value"],
            "answer": "{key: value}"
        },
    ]

    random.shuffle(questions)
    score = 0

    print("Welcome to the Python Quiz!")
    print("Answer the following 10 questions. Good luck!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")
        
        answer = input("Enter the number of your answer: ")
        
        try:
            if q["options"][int(answer) - 1] == q["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}\n")
        except (ValueError, IndexError):
            print(f"Invalid input! The correct answer is: {q['answer']}\n")

    print(f"Quiz Complete! Your score is {score}/10.")

if __name__ == "__main__":
    python_quiz()

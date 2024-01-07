from random import shuffle


class Mystery:
    def __init__(self, question: str, answer: str, choices: list):
        self.question = question
        self.answer = answer
        if answer not in choices:
            choices.append(answer)
        self.choices = choices

    def quiz(self) -> bool:
        print(f'Question: {self.question}')
        shuffle(self.choices)
        for i, choice in enumerate(self.choices):
            print(f'{i + 1}. {choice}')
        user_input = input('Select option(you can skip if you write any symbol(not digit): ')
        if user_input.isdigit() and int(user_input) < len(self.choices):
            if self.choices[int(user_input) - 1] == self.answer:
                return 3
            return -3
        else:
            return 0


questions = [
    Mystery(question="What is the capital of Myanmar?",
            answer="Naypyidaw",
            choices=[
                "Thimpu",
                "Sana",
                "Nikosia",
                "Vindhuk"
            ]),
    Mystery(question="What does HTTP stand for?",
            answer="HyperText Transfer Protocol",
            choices=[
                "HyperText Transfer Pillow",
                "HyperText Transmission Protocol",
                "HyperText Transmission Protocol",
                "HyperText Transfer Plague"
            ]),
    Mystery(question="What does SQL stand for?",
            answer="Structured Query Language",
            choices=[
                "Stylish Question Language",
                "Stylish Query Language",
                "Statement Question Language",
                "Structured Query Library"
            ]),
    Mystery(question="What is the derivative of x^2?",
            answer="2x",
            choices=[
                "2x^2",
                "x^2",
                "2",
                "x"
            ]),
    Mystery(question="What is the integral of x^2?",
            answer="1/3*x^3",
            choices=[
                "1/3*x^2",
                "2x",
                "x^2",
                "x"
            ]),
    Mystery(question="What is the sum of the first 10 natural numbers?",
            answer="55",
            choices=[
                "44",
                "60",
                "50",
                "45"
            ])
]

shuffle(questions)
score = 0
for q in questions:
    score += q.quiz()
    print('\n————————————————————————————————————————————————————————————————\n')

print(f"Your score is: {score}. You could have gotten {len(questions) * 3} points")

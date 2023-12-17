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
            print(f'{i+1}. {choice}')
        user_input = int(input('Select option: '))
        if self.choices[user_input-1] == self.answer:
            return True
        return False


q1 = Mystery(question="Откуда на Беларусь готовилось нападение?",
             answer="там 4 позиции, я карту принёс, сейчас покажу",
             choices=[
                 "Откуда мне знать?",
                 "Со склада грязи.",
                 "С планеты Нибиру.",
                 "С загнивающег запада."
             ])

print(q1.quiz())

# Devin Kinkead
import json


class Question:
    def __init__(self, text, value, answer, choices=None, c_feedback="", i_feedback=""):
        """

        :param text: String
        :param value: Integer with point value - between 1 and 3
        :param answer: Correct answer to question - String
        :param choices: list of strings with choices to question
        :param c_feedback: Feedback for correct answer
        :param i_feedback: Feedback for incorrect answer

        """
        self.q_text = text
        self.point_value = value
        if choices is not None:
            self.choices = choices
        else:
            self.choices = list()
        self.answer = answer
        self.correct_feedback = c_feedback
        self.incorrect_feedback = i_feedback
    @property
    def q_text(self):
        return self.__q_text

    @q_text.setter
    def q_text(self, text):
        if text != '':
            self.__q_text = text
        else:
            self.__q_text = '(blank)'

    @property
    def point_value(self):
        return self.__point_value

    @point_value.setter
    def point_value(self, value):
        try:
           temp = int(value)
        except (TypeError, ValueError):
            temp = 1
        # Will store value between 1 and 3 inclusive
        if temp >= 1:
            if temp <= 3:
                self.__point_value = temp
            else:
                self.__point_value = 1
        else:
            self.__point_value = 1

    @property
    def answer(self):
        return self.__answer

    @answer.setter
    def answer(self, answer):
        if answer in self.choices:
            self.__answer = answer
        else:
            self.__answer = 'Invalid'

    @property
    def correct_feedback(self):
        return self.__correct_feedback

    @correct_feedback.setter
    def correct_feedback(self, feedback):
        if feedback != "":
            self.__correct_feedback = feedback
        else:
            self.__correct_feedback = "Correct!"

    @property
    def incorrect_feedback(self):
        return self.__incorrect_feedback

    @incorrect_feedback.setter
    def incorrect_feedback(self, feedback):
        if feedback != "":
            self.__incorrect_feedback = feedback
        else:
            self.__incorrect_feedback = "Incorrect!"

    @property
    def choices(self):
        return self.__choices

    @choices.setter
    def choices(self, choices_lst):
        if type(choices_lst) == list:
            rqd_length = 4
            if len(choices_lst) == rqd_length:
                self.__choices = choices_lst
            elif len(choices_lst) < rqd_length:
                temp_lst = list()
                count = len(choices_lst)
                for n in choices_lst:
                    temp_lst.append(n)
                for n in range(1, (rqd_length-count+1)):
                    temp_lst.append('(blank)')
                self.__choices = temp_lst
            elif len(choices_lst) > rqd_length:
                tmp_list = list()
                for n in range(0, rqd_length):
                    tmp_list.append(choices_lst[n])
                self.__choices = tmp_list
            else:
                self.__choices = ['(blank)', '(blank)', '(blank)', '(blank)']
        else:
            self.__choices = ['(blank)', '(blank)', '(blank)', '(blank)']

    def __str__(self):
        return f'{self.q_text}'


def save_questions(questions):
    """
    Saves questions into a json file
    :param questions: List of dictionaries with the question data to be encoded
    :return: None
    """
    with open('questions.json', 'w') as fp:
        json.dump(questions, fp)



def load_questions():
    """
    Loads the questions from a json file
    :return: s - decoded list of dictionaries with question data
    """
    with open('questions.json') as fp:
        questions = json.load(fp)
    # print(s)
    return questions


def question_prep_save(question):
    """
    Converts question object into dictionary
    :param question: Question object
    :return: dictionary with Question data
    """
    question_dict = dict()
    question_dict['text'] = question.q_text
    question_dict['value'] = question.point_value
    question_dict['choices'] = question.choices
    question_dict['answer'] = question.answer
    question_dict['cFeedback'] = question.correct_feedback
    question_dict['iFeedback'] = question.incorrect_feedback
    return question_dict


def question_prep_load(questions):
    """
    Converts a list of dictionary data and returns a list of Question objects
    :param questions: list of dictionaries
    :return: q_list - list of Questions
    """

    q_list = list()
    for question in questions:
        text = question['text']
        value = question['value']
        choices = question['choices']
        answer = question['answer']
        c_feedback = question['cFeedback']
        i_feedback = question['iFeedback']
        temp_question = Question(text, value, answer, choices, c_feedback, i_feedback)
        q_list.append(temp_question)
    return q_list


def question_remove(question_lst, q):
    """
    Removes selected question from list of questions and the question data file.
    :param question_lst: List of question objects
    :param q: Question to be removed
    :return: New list of question objects
    """
    count = 0
    count2 = 0
    for question in question_lst:
        if question.__str__() == q:
            # removed = question_lst.pop(count)
            question_file_lst = load_questions()
            for file_question in question_file_lst:
                if file_question['text'] == q:
                    question_file_lst.pop(count2)
                count2 += 1
            save_questions(question_file_lst)
        count += 1
        count2 = 0

    return question_lst

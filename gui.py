# Devin Kinkead CIS345 12:00pm Project (final)
import questions
from difflib import get_close_matches
from tkinter import *
import random
from PIL import Image, ImageTk

window = Tk()
window.title("Mental Anguish")
# Geometry determined in functions
# window.geometry('800x250')


def add_question_start():
    main_frame.grid_forget()
    window.geometry('800x600')
    edit_frame.grid(row=0, column=0)


def question_maker(text, value, answer_var, choice_lst, c_feedback_var, i_feedback_var):
    """
    Takes question attributes and creates and saves new question. If question text of the new question already exists
    in the question file, it will overwrite the existing question.
    :param text: Text of the question
    :param value: Point value
    :param answer_var: Integer selecting correct choice
    :param choice_lst: List of choices
    :param c_feedback_var: Correct Feedback
    :param i_feedback_var: Incorrect Feedback
    :return:
    """
    # Obtain entered data
    text = text.get()
    value = value.get()

    choices = list()
    for n in choice_lst:
        choices.append(n.get())

    answer_var = answer_var.get()
    answer1 = choices[answer_var - 1]
    c_feedback_var = c_feedback_var.get()
    i_feedback_var = i_feedback_var.get()

    # create Question object
    temp = questions.Question(text, value, answer1, choices, c_feedback_var, i_feedback_var)
    prepped = questions.question_prep_save(temp)
    quests = questions.load_questions()

    # Check for presence of prepped question in current question list
    for q in quests:
        if q['text'] == prepped['text']:
            # Replace old question values with new values
            for k in q.keys():
                q[k] = prepped[k]

    # if a new question
    if prepped not in quests:
        quests.append(prepped)

    # Save new question data
    questions.save_questions(quests)

    clear_entries()
    # Label(text="Question Added").grid(row=10, column=0)
    main_menu()


def main_menu():
    """Display the main menu"""
    window.geometry('800x250')
    clear_entries()
    game_end_frame.grid_forget()
    edit_frame.grid_forget()
    search_frame.grid_forget()
    main_frame.grid(row=0, column=0)
    view_question()


def clear_entries():
    """Clear entries of gui"""
    global question_text, question_value, choice_1, choice_2, choice_3, choice_4, answer, c_feedback, i_feedback,\
        question_quiz_list, points_earned_variable, total_points
    question_text.set('')
    question_value.set(1)
    choice_1.set('')
    choice_2.set('')
    choice_3.set('')
    choice_4.set('')
    answer.set(1)
    c_feedback.set('')
    i_feedback.set('')
    question_quiz_list = list()
    points_earned_variable.set('')
    total_points.set('')
    search_term.set('')


def edit_question_start():
    """Start the edit question menu"""
    global list_box, question_text, question_value, choice_1, choice_2, choice_3, choice_4, answer, c_feedback, \
        i_feedback
    window.geometry('800x600')
    s_question = list_box.selection_get()
    data = questions.load_questions()
    list_q = questions.question_prep_load(data)

    for q in list_q:
        if q.q_text == list_box.selection_get():
            s_question = q
            break

    question_text.set(s_question.q_text)
    question_value.set(s_question.point_value)
    choice_1.set(s_question.choices[0])
    choice_2.set(s_question.choices[1])
    choice_3.set(s_question.choices[2])
    choice_4.set(s_question.choices[3])

    count = 0
    for choice in s_question.choices:
        if s_question.answer == choice:
            answer.set(count+1)
        count += 1

    c_feedback.set(s_question.correct_feedback)
    i_feedback.set(s_question.incorrect_feedback)
    main_frame.grid_forget()
    edit_frame.grid(row=0, column=0)


def view_question():
    """Add questions to listbox"""
    global list_q, list_box
    list_box.delete(0, END)
    data = questions.load_questions()
    list_q = questions.question_prep_load(data)

    for q in list_q:
        list_box.insert(END, q)
    list_box.selection_set(0)


def delete_question():
    """Remove a question"""
    global list_box, list_q
    question = list_box.selection_get()
    questions.question_remove(list_q, question)
    view_question()


def search_question_start():
    """Set up the search menu"""
    window.geometry('800x250')
    main_frame.grid_forget()
    search_frame.grid(row=0, column=0)
    list_box_search.delete('0', 'end')
    for q in list_q:
        list_box_search.insert(END, q)


def search():
    """Performs a search through each question's text, choices, and feedback text"""
    global list_box_search, search_term, list_q
    results_list = list()

    question_dict = dict()
    for q in list_q:
        question_dict[f'{q}'] = [q.q_text, q.choices[0], q.choices[1], q.choices[2], q.choices[3],
                                 q.correct_feedback, q.incorrect_feedback]

    for k in question_dict.keys():
        result_temp = get_close_matches(search_term.get(), question_dict[k], cutoff=0.51)
        if len(result_temp) > 0:
            results_list.append(k)

    # results_list = get_close_matches(search_term.get(), q_text_list, cutoff=0.45)

    list_box_search.delete('0', 'end')
    for result in results_list:
        list_box_search.insert(END,result)


def play_game():
    """
    Runs a 3 Question quiz for the User. 3 Random, and Unique questions are chosen
    :return:
    """
    window.geometry('800x250')
    global question_quiz_list, list_q, answer, c_ok_btn, i_ok_btn, ok_btn_variable, question_value, question_progress
    question_quiz_list = list()
    c_answer = int()
    # 3 unique questions
    while len(question_quiz_list) < 3:
        num = random.randint(0, len(list_q)-1)
        # print(num)
        if num not in question_quiz_list:
            question_quiz_list.append(num)
        else:
            continue
    # Switch Frames
    main_frame.grid_forget()
    quiz_frame.grid(row=0, column=0)
    q_count = 3
    total = 0
    total_points.set(f'Point Total: {total}')
    # question_text.set(list_q[question_quiz_list[0]])
    for q in question_quiz_list:
        question_given = list_q[q]
        question_progress.set(f'{q_count}/3 questions left')
        c_count = 1
        for c in question_given.choices:
            if question_given.answer == c:
                c_answer = c_count
                break
            c_count += 1
        user_answer = quiz_question(question_given, c_answer)
        if user_answer:
            quiz_frame.grid_forget()
            correct_frame.grid(row=0, column=0)
            total += question_value.get()
            total_points.set(f'Point Total: {total}')
            if question_value.get() == 1:
                points_earned_variable.set(f'{question_value.get()} points earned')

            else:
                points_earned_variable.set(f'{question_value.get()} points earned')
            c_ok_btn.wait_variable(ok_btn_variable)
            ok_btn_variable = IntVar()
            correct_frame.grid_forget()
            quiz_frame.grid(row=0, column=0)
        else:
            quiz_frame.grid_forget()
            points_earned_variable.set(f'No points earned')
            incorrect_frame.grid(row=0, column=0)
            i_ok_btn.wait_variable(ok_btn_variable)
            ok_btn_variable = IntVar()
            incorrect_frame.grid_forget()
            quiz_frame.grid(row=0, column=0)
        q_count -= 1

    quiz_frame.grid_forget()
    game_end_frame.grid(row=0, column=0)
    # print(question_quiz_list)


def quiz_question(quest, c_answer):
    """
    Asks user a question, and compares user's answer to the correct answer. Returns whether user's answer is correct.
    :param quest: Question object
    :param c_answer: Correct Answer
    :return:
    """
    global question_text, question_value, choice_1, choice_2, choice_3, choice_4, answer, \
        c_feedback, i_feedback, submit_btn, quiz_frame, quiz_button_clicked, selected_quiz_answer

    answer_correct = False
    selected_quiz_answer.set(0)

    question_text.set(quest.q_text)
    question_value.set(quest.point_value)
    choice_1.set(quest.choices[0])
    choice_2.set(quest.choices[1])
    choice_3.set(quest.choices[2])
    choice_4.set(quest.choices[3])
    c_feedback.set(quest.correct_feedback)
    i_feedback.set(quest.incorrect_feedback)
    quiz_frame.wait_variable(quiz_button_clicked)

    if selected_quiz_answer.get() == c_answer:
        answer_correct = True

    return answer_correct


# Menu Bar
menu_bar = Menu(window, tearoff=False)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit)


# Gui Variables
question_text = StringVar()
question_value = IntVar()
question_value.set(1)
choice_1 = StringVar()
choice_2 = StringVar()
choice_3 = StringVar()
choice_4 = StringVar()
answer = IntVar()
answer.set(1)
c_feedback = StringVar()
i_feedback = StringVar()
list_q = list()
search_term = StringVar()
question_quiz_list = list()
selected_quiz_answer = IntVar()
ok_btn_variable = IntVar()
quiz_button_clicked = IntVar()

# Feedback images
correct_img = Image.open('smiley.png')
c_img_render = ImageTk.PhotoImage(correct_img)
incorrect_img = Image.open('frowny.png')
i_img_render = ImageTk.PhotoImage(incorrect_img)

# Game-over Image
game_end_img = Image.open('game-end.jpg')
game_end_render = ImageTk.PhotoImage(game_end_img)

# User Point variables
points_earned_variable = StringVar()
question_progress = StringVar()
total_points = StringVar()


# Frames
main_frame = Frame(window)
list_box_frame_main = Frame(main_frame)
main_frame.grid(row=0, column=0)
edit_frame = Frame(window)
search_frame = Frame(window)
list_box_frame_search = Frame(search_frame)
quiz_frame = Frame(window)

correct_frame = Frame(window)
incorrect_frame = Frame(window)
game_end_frame = Frame(window)


# Main Frame Items
Label(main_frame, text="Main Menu").grid(row=0,column=1, columnspan=3)
add_q = Button(main_frame, text="Add Question", command=add_question_start)
add_q.grid(row=1, column=0)

delete_q = Button(main_frame, text="Delete Question", command=delete_question)
delete_q.grid(row=1,column=1)
search_q = Button(main_frame, text="Search Questions", command=search_question_start)
search_q.grid(row=1,column=2)

edit_q = Button(main_frame, text="Edit Question", command=edit_question_start)
edit_q.grid(row=1,column=3)
quizzer = Button(main_frame, text="Play Now", command=play_game)
quizzer.grid(row=1,column=4)


# list_box_frame_main - Within main_frame
list_box_frame_main.grid(row=2, column=0, padx=10, columnspan=5)
list_box = Listbox(list_box_frame_main, width=95)
list_box.pack(side=LEFT)
scrollbar = Scrollbar(list_box_frame_main, command=list_box.yview, orient='vertical')
scrollbar.pack(side=RIGHT, fill=Y)
list_box.config(yscrollcommand=scrollbar.set)


# Edit Frame
q_text_lbl = Label(edit_frame, text="Question Text")
q_text_lbl.grid(row=0,column=0, ipady=25, ipadx=25)
q_text = Entry(edit_frame, textvariable=question_text, width=50)
q_text.grid(row=0, column=1, columnspan=3)

value_lbl = Label(edit_frame, text="Question Value")
value_lbl.grid(row=1, column=0)

rad_frame = Frame(edit_frame)
rad_frame.grid(row=1, column=1)
q_value_1 = Radiobutton(rad_frame, variable=question_value, text='1', value=1, indicatoron=1, command=lambda: None)
q_value_1.grid(row=0, column=0)

q_value_2 = Radiobutton(rad_frame, variable=question_value, text='2', value=2, indicatoron=1, command=lambda: None)
q_value_2.grid(row=0, column=1)

q_value_3 = Radiobutton(rad_frame, variable=question_value, text='3', value=3,indicatoron=1, command=lambda: None)
q_value_3.grid(row=0, column=2)

q_choice_1_lbl = Label(edit_frame, text="Choice 1")
q_choice_1_lbl.grid(row=2, column=0, ipady=20)
q_choice_1 = Entry(edit_frame, textvariable=choice_1, width=50)
q_choice_1.grid(row=2, column=1, columnspan=3)

q_choice_2_lbl = Label(edit_frame, text="Choice 2")
q_choice_2_lbl.grid(row=3, column=0, ipady=20)
q_choice_2 = Entry(edit_frame, textvariable=choice_2, width=50)
q_choice_2.grid(row=3, column=1, columnspan=3)

q_choice_3_lbl = Label(edit_frame, text="Choice 3")
q_choice_3_lbl.grid(row=4, column=0, ipady=20)
q_choice_3 = Entry(edit_frame, textvariable=choice_3, width=50)
q_choice_3.grid(row=4, column=1, columnspan=3)

q_choice_4_lbl = Label(edit_frame, text="Choice 4")
q_choice_4_lbl.grid(row=5, column=0, ipady=20)
q_choice_4 = Entry(edit_frame, textvariable=choice_4, width=50)
q_choice_4.grid(row=5, column=1, columnspan=3)

answer_lbl = Label(edit_frame, text="Correct Answer #:")
answer_lbl.grid(row=6, column=0)
choice_frame = Frame(edit_frame)
choice_frame.grid(row=6, column=1)

choice_1_btn = Radiobutton(choice_frame, variable=answer, text='1', value=1, indicatoron=1)
choice_1_btn.grid(row=0, column=0)

choice_2_btn = Radiobutton(choice_frame, variable=answer, text='2', value=2, indicatoron=1)
choice_2_btn.grid(row=0, column=1)

choice_3_btn = Radiobutton(choice_frame, variable=answer, text='3', value=3,indicatoron=1)
choice_3_btn.grid(row=0, column=2)

choice_4_btn = Radiobutton(choice_frame, variable=answer, text='4', value=4, indicatoron=1)
choice_4_btn.grid(row=0, column=3)

c_feedback_lbl = Label(edit_frame, text="Correct Feedback")
c_feedback_lbl.grid(row=7, column=0)
c_feedback_e = Entry(edit_frame, textvariable=c_feedback, width=50)
c_feedback_e.grid(row=7, column=1)

i_feedback_lbl = Label(edit_frame, text="Incorrect Feedback")
i_feedback_lbl.grid(row=8, column=0)
i_feedback_e = Entry(edit_frame, textvariable=i_feedback, width=50)
i_feedback_e.grid(row=8, column=1)

submit_btn = Button(edit_frame, text="Submit", command=lambda: question_maker(question_text, question_value, answer,
                                                                        [choice_1,choice_2, choice_3, choice_4],
                                                                        c_feedback, i_feedback
                                                                        ))
submit_btn.grid(row=9, column=1)
cancel_btn = Button(edit_frame, text="Cancel", command=main_menu)
cancel_btn.grid(row=9, column=0)

# Search Frame
search_lbl = Label(search_frame, text="Search Term")
search_lbl.grid(row=0, column=0, padx=10)
search_bar = Entry(search_frame, textvariable=search_term, width=40)
search_bar.grid(row=0, column=1, padx=0)
search_submit = Button(search_frame, text="Search", command=search)
search_submit.grid(row=0, column=2)
cancel_btn = Button(search_frame, text="Cancel", command=main_menu)
cancel_btn.grid(row=0, column=3)


# list_box_frame_search - Within search_frame
list_box_frame_search.grid(row=2, column=0, padx=10, columnspan=5)
list_box_search = Listbox(list_box_frame_search, width=95)
list_box_search.pack(side=LEFT)
scrollbar = Scrollbar(list_box_frame_search, command=list_box_search.yview, orient='vertical')
scrollbar.pack(side=RIGHT, fill=Y)
list_box_search.config(yscrollcommand=scrollbar.set)

# Quiz_Frame
quiz_text = Label(quiz_frame, textvariable=question_text)
quiz_text.grid(row=0, column=1, columnspan=3,padx=80)
quiz_choice1_radio = Radiobutton(quiz_frame, variable=selected_quiz_answer, value='1', indicatoron=1)
quiz_choice1_radio.grid(row=1, column=0, sticky='W')
quiz_choice_1 = Label(quiz_frame, textvariable=choice_1)
quiz_choice_1.grid(row=1, column=1, sticky='W')

quiz_choice2_radio = Radiobutton(quiz_frame, variable=selected_quiz_answer, value='2', indicatoron=1)
quiz_choice2_radio.grid(row=2, column=0, sticky='W')
quiz_choice_2 = Label(quiz_frame, textvariable=choice_2)
quiz_choice_2.grid(row=2, column=1, sticky='W')


quiz_choice3_radio = Radiobutton(quiz_frame, variable=selected_quiz_answer, value='3', indicatoron=1)
quiz_choice3_radio.grid(row=3, column=0, sticky='W')
quiz_choice_3 = Label(quiz_frame, textvariable=choice_3)
quiz_choice_3.grid(row=3, column=1, sticky='W')

quiz_choice4_radio = Radiobutton(quiz_frame, variable=selected_quiz_answer, value='4', indicatoron=1)
quiz_choice4_radio.grid(row=4, column=0, sticky='W')
quiz_choice_4 = Label(quiz_frame, textvariable=choice_4)
quiz_choice_4.grid(row=4, column=1, sticky='W')
question_progress_lbl = Label(quiz_frame, textvariable=question_progress)
question_progress_lbl.grid(row=5,column=0, columnspan=3, sticky='W', padx=10)
total_points_lbl = Label(quiz_frame, textvariable=total_points)
total_points_lbl.grid(row=6, column=0, columnspan=3, sticky='W', padx=10)
submit_btn = Button(quiz_frame, text="Submit", command=lambda: quiz_button_clicked.set(1))
submit_btn.grid(row=7, column=1)


# Correct Frame
c_image = Label(correct_frame, image=c_img_render)
c_image.grid(row=0, column=0, columnspan=3, padx=10)
correct_label = Label(correct_frame, textvariable=c_feedback, width=50)
correct_label.grid(row=1, column=0, columnspan=3, padx=10)
c_points_label = Label(correct_frame, textvariable=points_earned_variable)
c_points_label.grid(row=2, column=0, columnspan=2, padx=10)
c_ok_btn = Button(correct_frame, text="OK", command=lambda: ok_btn_variable.set(1))
c_ok_btn.grid(row=3, column=0, sticky='E', padx=200)


# Incorrect Frame
i_image = Label(incorrect_frame, image=i_img_render)
i_image.grid(row=0, column=0, columnspan=3, padx=10)
incorrect_label = Label(incorrect_frame, textvariable=i_feedback, width=50)
incorrect_label.grid(row=1, column=0, columnspan=3, padx=10)
c_points_label = Label(incorrect_frame, textvariable=points_earned_variable)
c_points_label.grid(row=2, column=0, columnspan=2, padx=10)
i_ok_btn = Button(incorrect_frame, text="OK", command=lambda: ok_btn_variable.set(1))
i_ok_btn.grid(row=3, column=0, sticky='E', padx=200)

# Game End Frame
g_end_img = Label(game_end_frame, image=game_end_render)
g_end_img.grid(row=0, column=0, columnspan=3, padx=10)
g_end_msg = Label(game_end_frame, text="Game Over!")
g_end_msg.grid(row=1, column=0, columnspan=3, sticky='W', padx=10)
total_points_end_lbl = Label(game_end_frame, textvariable=total_points)
total_points_end_lbl.grid(row=2, column=0, columnspan=3, sticky='W', padx=10)
main_btn = Button(game_end_frame, text="Main Menu", command=main_menu)
main_btn.grid(row=3, column=0, sticky='W', padx=10)

main_menu()
view_question()


window.mainloop()
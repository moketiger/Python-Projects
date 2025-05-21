import time
import os
import json

file_text = {}
node_number = 1

file_path_text = 'example37.txt'
file_path_number = 'number17.txt'


def timer(wait_time):
    time.sleep(wait_time)

def write_to_json(path , data):
    with open(path , "w") as file:
        json.dump(data , file)

def read_from_json(path):
    with open(path , "r") as file:
        return json.load(file)

ask_question_again = True
delete_ask_question = True

print("Hello this is your nodes program\nThis is where you can write your notes")
timer(3)

while ask_question_again:

    text_question = input("\nWould you like to read from your nodes or write something new?"
                      "\nPress 1 to write something new\nPress 2 to read from your nodes"
                      "\npress 3 to stop the program\nWrite your answer here: ")

    if text_question == "1":
        change_option = input("Do you want to add a note or change a note\nWrite your answer here: ")

        if "add" in change_option:
            appended_text = str(input("Write the note you want to add here: "))
            file_text[node_number] = appended_text

            write_to_json(file_path_text , file_text)
            node_number += 1
            write_to_json(file_path_number , node_number)
        elif "change" in change_option:
            change_note = input("Write the note you want to change here: ")
            timer(0.5)
            Change_text = input("Write the new text you want to change here: ")
            if change_note.isdigit() and int(change_note) < node_number:
                file_text[int(change_note)] = Change_text
                write_to_json(file_path_text, file_text)
            else:
                print("Invalid input")

    elif text_question == "2":
        file_text = read_from_json(file_path_text)
        node_number = read_from_json(file_path_number)
        print(file_text)
        print("---------------------------------------")
        for i in range(1 , node_number):
            print(str(i) + "\t" + str(file_text[str(i)]))
        print("---------------------------------------")
        quit_option = str(input("Do you want to continue, stop or delete a node?\nWrite your answer here: "))
        timer(0.5)

        if "continue" in quit_option:
            pass

        elif "delete" in quit_option:
            delete_ask_question = True
            while delete_ask_question:
                number_want_to_del = input("What number node do you want to delete?\nWrite your answer here: ")
                if number_want_to_del.isdigit():
                    if int(number_want_to_del) in range(1 , node_number):
                        file_text.pop(number_want_to_del)
                        delete_ask_question = False
                        for i in file_text.keys():
                            if int(i) > int(number_want_to_del):
                                val = file_text.pop(i)
                                file_text[int(i) - 1] = val
                        node_number -= 1

                        write_to_json(file_path_text , file_text)
                        write_to_json(file_path_number , node_number)
                    else:
                        print("there is no node like this that exist")

        elif "stop" in quit_option:
            ask_question_again = False

        else:
            print("Invalid answer try again")
            timer(0.1)



    elif text_question == "3":
        ask_question_again = False

    else:
        print("Invalid answer")

print("I hope you enjoyed and have a great day")
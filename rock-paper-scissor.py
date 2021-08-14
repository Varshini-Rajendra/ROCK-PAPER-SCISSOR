import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

user_point = 0
comp_point = 0
user_choice = ''
comp_choice = ''

def choice_to_number(choice):
    ctn = {'rock':0 , 'paper':1, 'scissor':2}
    return ctn[choice]

def number_to_choice(num):
    ntc = {0:'rock', 1:'paper', 2:'scissor'}
    return ntc[num]

def get_comp_choice():
    choices = ['rock','paper','scissor']
    return random.choice(choices)

def result(user_input, comp_input):
    global user_point, comp_point
    user = choice_to_number(user_input)
    comp = choice_to_number(comp_input)
    winner = ''
    usp = ''
    cmp = ''
    if(user==comp):
        winner = "Tie"
    elif((user-comp)%3==1):
        winner = "You win\n"
        user_point+=1
    else:
        winner = "Comp wins\n"
        comp_point+=1
    output = "User's choice: "+number_to_choice(user)+"\nComputer's choice: "+number_to_choice(comp)+"\n"
    lbl_output = tk.Label(master, text = output)
    lbl_output.grid(row = 1, column = 1, sticky="nsew")

    lbl_winner = tk.Label(master, text = winner)
    lbl_winner.grid(row = 2, column = 1, sticky="nsew")
    lbl_winner.config(text = winner)

    usp = "User's Points: "+str(user_point)
    lbl_user_points = tk.Label(master, text = usp)
    lbl_user_points.grid(row = 3, column = 1, sticky="nsew")
    lbl_user_points.config(text = usp)

    cmp = "Computer's Points: "+str(comp_point)+"\n"
    lbl_comp_points = tk.Label(master, text = cmp)
    lbl_comp_points.grid(row = 4, column = 1, sticky="nsew")
    lbl_comp_points.config(text = cmp)
    
    if user_point == 3:
        messagebox.showinfo("Winner", "User wins")
        user_point = 0
        comp_point = 0
        usp = "User's Points: "+str(user_point)
        lbl_user_points = tk.Label(master, text = usp)
        lbl_user_points.grid(row = 3, column = 1, sticky="nsew")
        lbl_user_points.config(text = usp)
        cmp = "Computer's Points: "+str(comp_point)+"\n"
        lbl_comp_points = tk.Label(master, text = cmp)
        lbl_comp_points.grid(row = 4, column = 1, sticky="nsew")
        lbl_comp_points.config(text = cmp)
    elif comp_point == 3:
        messagebox.showinfo("Winner", "Comp wins")
        user_point = 0
        comp_point = 0
        usp = "User's Points: "+str(user_point)
        lbl_user_points = tk.Label(master, text = usp)
        lbl_user_points.grid(row = 3, column = 1, sticky="nsew")
        lbl_user_points.config(text = usp)
        cmp = "Computer's Points: "+str(comp_point)+"\n"
        lbl_comp_points = tk.Label(master, text = cmp)
        lbl_comp_points.grid(row = 4, column = 1, sticky="nsew")
        lbl_comp_points.config(text = cmp)

def rock():
    global user_choice, comp_choice
    user_choice = 'rock'
    comp_choice = get_comp_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice, comp_choice
    user_choice = 'paper'
    comp_choice = get_comp_choice()
    result(user_choice, comp_choice)

def scissor():
    global user_choice, comp_choice
    user_choice = 'scissor'
    comp_choice = get_comp_choice()
    result(user_choice, comp_choice)


master = tk.Tk()
master.title("Rock Paper Scissors")
master.geometry("300x200")
#master.grid_rowconfigure(0, weight=1)
#master.grid_rowconfigure(2, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(2, weight=1)

btn_rock = tk.Button(master, text = "Rock", command = rock)
btn_rock.grid(row = 0, column = 0, sticky="e")
btn_paper = tk.Button(master, text = "Paper", command = paper)
btn_paper.grid(row = 0, column = 1)
btn_scissor = tk.Button(master, text = "Scissor", command = scissor)
btn_scissor.grid(row = 0, column = 2,sticky="w")

master.mainloop()
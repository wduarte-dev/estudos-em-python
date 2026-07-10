import tkinter as tk
from PIL import Image, ImageTk
from functions import game

root = tk.Tk()
root.title('JOKENPÔ')
root.geometry('1280x720')
root.rowconfigure(0, minsize=250)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

# TUDO RELACIONADO AO FRAME DE CIMA
upper_frame = tk.Frame(root, bg='yellow')
upper_frame.grid(row=0, column=0, sticky='nsew')
upper_frame.rowconfigure(0, weight=1)
upper_frame.columnconfigure(0, weight=1)
upper_frame.columnconfigure(1, weight=1)

user_points = tk.IntVar()
machine_points = tk.IntVar()
user_points.set(1)
machine_points.set(0)
user_points_label = tk.Label(upper_frame, textvariable=user_points, bg='yellow', font=('Arial', 60))
machine_points_label = tk.Label(upper_frame, textvariable=machine_points, bg='yellow', font=('Arial', 60))
user_points_label.grid(row=0, column=0)
machine_points_label.grid(row=0, column=1)

# TUDO RELACIONADO AO FRAME DE BAIXO
lower_frame = tk.Frame(root, bg='blue')
lower_frame.grid(row=1, column=0, sticky='nsew')
lower_frame.rowconfigure(0, weight=1)
lower_frame.rowconfigure(1, weight=1)
lower_frame.columnconfigure(0, weight=1)
lower_frame.columnconfigure(1, weight=1)
lower_frame.columnconfigure(2, weight=1)

rock_image_load = Image.open('rock.png')
paper_image_load = Image.open('paper.png')
scissor_image_load = Image.open('scissor.png')
markus_image_load = Image.open('markus.png')
rock_image_resized = rock_image_load.resize((160, 170))
paper_image_resized = paper_image_load.resize((180, 270))
scissor_image_resized = scissor_image_load.resize((170, 260))
markus_image_resized = markus_image_load.resize((200, 200))
rock_image = ImageTk.PhotoImage(rock_image_resized)
paper_image = ImageTk.PhotoImage(paper_image_resized)
scissor_image = ImageTk.PhotoImage(scissor_image_resized)
markus_image = ImageTk.PhotoImage(markus_image_resized)

rock_button = tk.Button(lower_frame, text='PEDRA', image=rock_image, command=lambda:game('Pedra', user_points, machine_points))
paper_button = tk.Button(lower_frame, text='PAPEL', image=paper_image, command=lambda:game('Papel', user_points, machine_points))
scissor_button = tk.Button(lower_frame, text='TESOURA', image=scissor_image, command=lambda:game('Tesoura', user_points, machine_points))
machine_choice_button = tk.Label(lower_frame, text='ESCOLHA DA MÁQUINA', image=markus_image)

rock_button.grid(row=1, column=0, sticky='nsew')
paper_button.grid(row=1, column=1, sticky='nsew')
scissor_button.grid(row=1, column=2, sticky='nsew')
machine_choice_button.grid(row=0, column=1, sticky='nsew')

root.mainloop()
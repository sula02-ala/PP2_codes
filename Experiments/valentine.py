import tkinter as tk

phrases = [
    "Ты точно уверена? 🥺",
    "Ну пожааалуйста 💔",
    "Я буду стараться 😭",
    "Это последний раз, честно…",
    "Ну давай, нажми ДА 💖"
]

count = 0

def say_no():
    global count
    text.set(phrases[count % len(phrases)])
    count += 1

def say_yes():
    text.set("УРААА 💘\nСпасибо большое 😍 \n В этот праздник я хотел бы тебе сделать приятное, \n и сказать что, как мне повезло \n с тобой познакомиться и иметь возможность общаться, \nТы делаешь мои дни теплее и счастливее \n С праздником родная)")
    btn_yes.config(state="disabled")
    btn_no.config(state="disabled")

root = tk.Tk()
root.title("Маленький подарочек")
root.geometry("600x400")
root.resizable(False, False)

text = tk.StringVar()
text.set("Будешь моей валентинкой? 💌")

label = tk.Label(root, textvariable=text, font=("Montserrat", 14), wraplength=350)
label.pack(pady=30)

frame = tk.Frame(root)
frame.pack()

btn_yes = tk.Button(frame, text="ДА 💖", font=("Montserrat", 12), width=10, command=say_yes)
btn_yes.grid(row=0, column=0, padx=10)

btn_no = tk.Button(frame, text="НЕТ 💔", font=("Montserrat", 12), width=10, command=say_no)
btn_no.grid(row=0, column=1, padx=10)

root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

phrases = [
    "Ты точно уверена? 🥺",
    "Ну пожааалуйста 💔",
    "Я буду стараться 😭",
    "Это последний раз, честно…",
    "Ну давай, нажми ДА 💖"
]

count = 0
frames = []
gif_label = None
gif_index = 0


def say_no():
    global count
    text.set(phrases[count % len(phrases)])
    count += 1


def play_gif():
    global gif_index
    gif_label.config(image=frames[gif_index])
    gif_index = (gif_index + 1) % len(frames)
    root.after(100, play_gif)


def say_yes():
    global gif_label, frames

    text.set(
        "УРААА 💘\n"
        "Спасибо большое 😍\n\n"
        "В этот праздник я хотел бы тебе сделать приятное,\n"
        "и сказать, как мне повезло\n"
        "с тобой познакомиться и иметь возможность общаться 💖\n\n"
        "Ты делаешь мои дни теплее и счастливее ✨\n"
        "С праздником, родная 💐"
    )

    btn_yes.config(state="disabled")
    btn_no.config(state="disabled")

    # Загружаем гифку через Pillow
    frames.clear()
    gif = Image.open("ijolove.gif")

    for frame in ImageSequence.Iterator(gif):
        frame = frame.resize((220, 165))  # размер гифки
        frames.append(ImageTk.PhotoImage(frame))

    gif_label = tk.Label(root)
    gif_label.pack(pady=10)

    play_gif()


# Главное окно
root = tk.Tk()
root.title("Маленький подарочек 💝")
root.geometry("600x450")
root.resizable(False, False)

text = tk.StringVar()
text.set("Будешь моей валентинкой? 💌")

label = tk.Label(
    root,
    textvariable=text,
    font=("Montserrat", 14),
    wraplength=520,
    justify="center"
)
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

btn_yes = tk.Button(frame, text="ДА 💖", font=("Montserrat", 12),
                    width=10, command=say_yes)
btn_yes.grid(row=0, column=0, padx=15)

btn_no = tk.Button(frame, text="НЕТ 💔", font=("Montserrat", 12),
                   width=10, command=say_no)
btn_no.grid(row=0, column=1, padx=15)

root.mainloop()


from tkinter import *
from PIL import Image, ImageTk
import pygame


pygame.mixer.init()


poyo_sound = pygame.mixer.Sound("Python stuff/poyo.wav")
birthday_music = "Python stuff/birthday.mp3"


pygame.mixer.music.load(birthday_music)
pygame.mixer.music.play(1)


root = Tk()
root.title("Happy Birthday!")
root.geometry("600x600")
root.resizable(False, False)


bg = Canvas(root, width=600, height=600, bg="#ffb6e6")
bg.pack(fill="both", expand=True)
bg.create_text(300, 100, text="🎉 HAPPY BIRTHDAY SYNTHEA DIDII!!🎉", font=("Comic Sans MS", 32, "bold"), fill="#ff0084")
bg.create_text(300, 150, text="To the BEST Sister Ever 💖", font=("Comic Sans MS", 20, "bold"), fill="#ff007f")


kirby_img = Image.open("Python stuff/kirby.png")
kirby_img = kirby_img.resize((200, 200), Image.Resampling.LANCZOS)
kirby_photo = ImageTk.PhotoImage(kirby_img)


def kirby_click(event):
    poyo_sound.play()


kirby_label = Label(root, image=kirby_photo, bg="#ffb6e6")
kirby_label.place(x=200, y=350)
kirby_label.bind("<Button-1>", kirby_click)

root.mainloop()
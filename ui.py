import customtkinter
import bot
from PIL import Image

def button_callback():
    textbox.delete("0.0", "end")
    textbox.insert("0.0", bot.main())

app = customtkinter.CTk()
app.geometry("300x350")

textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0", "")
textbox.pack(padx=20, pady=20)

button_image = customtkinter.CTkImage(Image.open("microphone.png"), size=(26, 26))

button = customtkinter.CTkButton(app, text="", command=button_callback, image=button_image)
button.pack(padx=20, pady=20)

app.mainloop()

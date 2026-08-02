import customtkinter as ctk

from ui import theme
from ui.main_window import MainWindow

app = ctk.CTk()

app.title("AI News Summarizer Pro")

app.geometry("1200x750")

app.configure(fg_color=theme.BACKGROUND)

MainWindow(app)

app.mainloop()
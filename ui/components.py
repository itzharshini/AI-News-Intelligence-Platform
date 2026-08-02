import customtkinter as ctk
from ui import theme


class InfoCard(ctk.CTkFrame):
    """
    Reusable information card.

    Example:
        Author
        John Doe
    """

    def __init__(self, master, title, value="N/A"):

        super().__init__(
            master,
            fg_color=theme.CARD,
            corner_radius=12
        )

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 13, "bold"),
            text_color=theme.SECONDARY
        )

        self.title.pack(anchor="w", padx=15, pady=(10, 2))

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 16),
            wraplength=280,
            justify="left"
        )

        self.value.pack(anchor="w", padx=15, pady=(0, 10))

    def set_value(self, text):
        self.value.configure(text=text)


class StatusBadge(ctk.CTkLabel):

    def __init__(self, master):

        super().__init__(

            master,

            text="🟢 Ready",

            font=("Segoe UI", 13, "bold"),

            corner_radius=8,

            fg_color="#1E3A1E",

            text_color="#A7F3D0",

            padx=10,

            pady=5
        )

    def ready(self):

        self.configure(
            text="🟢 Ready",
            fg_color="#1E3A1E",
            text_color="#A7F3D0"
        )

    def loading(self):

        self.configure(
            text="🟡 Processing...",
            fg_color="#3A3000",
            text_color="#FACC15"
        )

    def error(self):

        self.configure(
            text="🔴 Error",
            fg_color="#3A1111",
            text_color="#FCA5A5"
        )

    def success(self):

        self.configure(
            text="✅ Completed",
            fg_color="#052E16",
            text_color="#86EFAC"
        )


class PrimaryButton(ctk.CTkButton):

    def __init__(self, master, text, command=None):

        super().__init__(

            master,

            text=text,

            command=command,

            height=42,

            corner_radius=10,

            font=theme.BUTTON_FONT
        )
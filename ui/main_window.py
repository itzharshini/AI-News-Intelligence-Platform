import customtkinter as ctk
import tkinter.messagebox as messagebox

from ui import theme
from ui.components import InfoCard, StatusBadge, PrimaryButton
from core.summarizer import NewsSummarizer


class MainWindow:

    def __init__(self, app):

        self.app = app

        self.summarizer = NewsSummarizer()

        self.build_header()

        self.build_body()

    # =======================================================
    # HEADER
    # =======================================================

    def build_header(self):

        self.header = ctk.CTkFrame(
            self.app,
            fg_color=theme.CARD,
            corner_radius=15,
            height=90
        )

        self.header.pack(
            fill="x",
            padx=20,
            pady=20
        )

        title = ctk.CTkLabel(
            self.header,
            text="📰 AI News Intelligence Platform",
            font=theme.TITLE_FONT
        )

        title.pack(pady=(15, 0))

        subtitle = ctk.CTkLabel(
            self.header,
            text="Summarize • Analyze • Understand",
            font=theme.TEXT_FONT,
            text_color=theme.SECONDARY
        )

        subtitle.pack()

    # =======================================================
    # BODY
    # =======================================================

    def build_body(self):

        self.body = ctk.CTkFrame(
            self.app,
            fg_color="transparent"
        )

        self.body.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.build_sidebar()

        self.build_dashboard()

    # =======================================================
    # SIDEBAR
    # =======================================================

    def build_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.body,
            width=330,
            fg_color=theme.CARD,
            corner_radius=15
        )

        self.sidebar.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        self.sidebar.pack_propagate(False)

        title = ctk.CTkLabel(
            self.sidebar,
            text="🌐 News URL",
            font=theme.HEADING_FONT
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.url_entry = ctk.CTkEntry(
            self.sidebar,
            height=42,
            placeholder_text="Paste article URL..."
        )

        self.url_entry.pack(
            fill="x",
            padx=20
        )

        self.summarize_btn = PrimaryButton(
            self.sidebar,
            text="✨ Summarize",
            command=self.summarize_article
        )

        self.summarize_btn.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.clear_btn = PrimaryButton(
            self.sidebar,
            text="🗑 Clear",
            command=self.clear
        )

        self.clear_btn.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.copy_btn = PrimaryButton(
            self.sidebar,
            text="📋 Copy Summary",
            command=self.copy_summary
        )

        self.copy_btn.pack(
            fill="x",
            padx=20
        )

        status_title = ctk.CTkLabel(
            self.sidebar,
            text="Status",
            font=theme.HEADING_FONT
        )

        status_title.pack(
            anchor="w",
            padx=20,
            pady=(30, 10)
        )

        self.status = StatusBadge(
            self.sidebar
        )

        self.status.pack(
            anchor="w",
            padx=20
        )

    # =======================================================
    # DASHBOARD
    # =======================================================

    def build_dashboard(self):

        self.dashboard = ctk.CTkFrame(
            self.body,
            fg_color="transparent"
        )

        self.dashboard.pack(
            side="left",
            fill="both",
            expand=True
        )

                # ==========================
        # Row 1
        # ==========================

        top_row = ctk.CTkFrame(
            self.dashboard,
            fg_color="transparent"
        )

        top_row.pack(fill="x")

        self.title_card = InfoCard(
            top_row,
            "📰 Title"
        )

        self.title_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0,10)
        )

        self.author_card = InfoCard(
            top_row,
            "👤 Author"
        )

        self.author_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ==========================
        # Row 2
        # ==========================

        second_row = ctk.CTkFrame(
            self.dashboard,
            fg_color="transparent"
        )

        second_row.pack(fill="x", pady=15)

        self.date_card = InfoCard(
            second_row,
            "📅 Published"
        )

        self.date_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0,10)
        )

        self.sentiment_card = InfoCard(
            second_row,
            "😊 Sentiment"
        )

        self.sentiment_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ==========================
        # Row 3
        # ==========================

        third_row = ctk.CTkFrame(
            self.dashboard,
            fg_color="transparent"
        )

        third_row.pack(fill="x")

        self.reading_card = InfoCard(
            third_row,
            "⏱ Reading Time"
        )

        self.reading_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0,10)
        )

        self.words_card = InfoCard(
            third_row,
            "📖 Word Count"
        )

        self.words_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ==========================
        # Summary Section
        # ==========================

        summary_frame = ctk.CTkFrame(
            self.dashboard,
            fg_color=theme.CARD,
            corner_radius=15
        )

        summary_frame.pack(
            fill="both",
            expand=True,
            pady=(15,0)
        )

        summary_title = ctk.CTkLabel(
            summary_frame,
            text="📝 Summary",
            font=theme.HEADING_FONT
        )

        summary_title.pack(
            anchor="w",
            padx=20,
            pady=(20,10)
        )

        self.summary_box = ctk.CTkTextbox(
            summary_frame,
            font=theme.TEXT_FONT,
            corner_radius=10
        )

        self.summary_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

    def summarize_article(self):

        url = self.url_entry.get().strip()

        if not url:
            messagebox.showwarning(
                "Missing URL",
                "Please enter a news article URL."
            )
            return

        try:

            self.status.loading()

            self.app.update()

            data = self.summarizer.summarize(url)

            self.title_card.set_value(data["title"])
            self.author_card.set_value(data["author"])
            self.date_card.set_value(data["date"])
            self.sentiment_card.set_value(data["sentiment"])
            self.reading_card.set_value(data["reading_time"])
            self.words_card.set_value(data["word_count"])

            self.summary_box.delete("1.0", "end")
            self.summary_box.insert("1.0", data["summary"])

            self.status.success()

        except Exception as e:

            self.status.error()

            messagebox.showerror(
                "Error",
                str(e)
            )


    def clear(self):

        self.url_entry.delete(0, "end")

        self.summary_box.delete("1.0", "end")

        self.title_card.set_value("N/A")
        self.author_card.set_value("N/A")
        self.date_card.set_value("N/A")
        self.sentiment_card.set_value("N/A")
        self.reading_card.set_value("N/A")
        self.words_card.set_value("N/A")

        self.status.ready()


    def copy_summary(self):

        summary = self.summary_box.get("1.0", "end").strip()

        if not summary:
            messagebox.showwarning(
                "Nothing to Copy",
                "No summary available."
            )
            return

        self.app.clipboard_clear()
        self.app.clipboard_append(summary)

        messagebox.showinfo(
            "Copied",
            "Summary copied successfully!"
        )
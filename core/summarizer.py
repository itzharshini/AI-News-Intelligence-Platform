from newspaper import Article
from textblob import TextBlob
import trafilatura
import requests
from bs4 import BeautifulSoup
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


class NewsSummarizer:

    def summarize(self, url):

        try:
            return self._summarize_newspaper(url)

        except Exception:
            return self._summarize_trafilatura(url)

    # ------------------------------
    # Method 1 : Newspaper3k
    # ------------------------------

    def _summarize_newspaper(self, url):

        article = Article(url)

        article.download()
        article.parse()
        article.nlp()

        return self._build_result(
            title=article.title,
            author=", ".join(article.authors) if article.authors else "Unknown",
            date=str(article.publish_date.date()) if article.publish_date else "Unknown",
            text=article.text,
            summary=article.summary
        )

    # ------------------------------
    # Method 2 : Trafilatura
    # ------------------------------

    def _summarize_trafilatura(self, url):

        downloaded = trafilatura.fetch_url(url)

        if downloaded is None:
            raise Exception("Unable to download article.")

        text = trafilatura.extract(downloaded)

        if not text:
            raise Exception("Unable to extract article text.")

        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "Unknown"

        summary = " ".join(text.split(".")[:5]) + "."

        return self._build_result(
            title=title,
            author="Unknown",
            date="Unknown",
            text=text,
            summary=summary
        )

    # ------------------------------
    # Shared formatter
    # ------------------------------

    def _build_result(self, title, author, date, text, summary):

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😞 Negative"
        else:
            sentiment = "😐 Neutral"

        words = len(text.split())

        reading = max(1, round(words / 200))

        return {
            "title": title or "Unknown",
            "author": author,
            "date": date,
            "summary": summary,
            "sentiment": sentiment,
            "reading_time": f"~{reading} min read",
            "word_count": f"{words:,} words"
        }
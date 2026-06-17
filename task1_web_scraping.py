# ============================================================
# CodeAlpha Internship — Task 1: Web Scraping
# Description: Scrape book data from books.toscrape.com
#              (a free, legal practice site)
# Libraries  : requests, BeautifulSoup, pandas
# ============================================================

# Install dependencies:
# pip install requests beautifulsoup4 pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"


def get_star_rating(word):
    """Convert word-based rating to numeric."""
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return rating_map.get(word, 0)


def scrape_page(url):
    """Scrape all books from a single page."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.find_all("article", class_="product_pod"):
        title = article.h3.a["title"]
        price = article.find("p", class_="price_color").text.strip()
        availability = article.find("p", class_="instock availability").text.strip()
        rating_word = article.p["class"][1]
        rating = get_star_rating(rating_word)

        books.append({
            "Title": title,
            "Price (£)": float(price.replace("£", "").replace("Â", "")),
            "Rating (out of 5)": rating,
            "Availability": availability
        })

    # Find the next page link
    next_btn = soup.find("li", class_="next")
    next_url = BASE_URL + next_btn.a["href"] if next_btn else None

    return books, next_url


def scrape_all_pages(max_pages=5):
    """Scrape multiple pages (default: first 5 pages)."""
    all_books = []
    url = START_URL
    page = 1

    while url and page <= max_pages:
        print(f"Scraping page {page}: {url}")
        books, url = scrape_page(url)
        all_books.extend(books)
        page += 1
        time.sleep(1)  # Be polite — don't hammer the server

    return all_books


def main():
    print("=" * 50)
    print("  CodeAlpha — Task 1: Web Scraping")
    print("=" * 50)

    # Scrape data
    books = scrape_all_pages(max_pages=5)

    # Convert to DataFrame
    df = pd.DataFrame(books)

    # Basic summary
    print(f"\nTotal books scraped: {len(df)}")
    print(f"\nSample data:\n{df.head()}")
    print(f"\nBasic Statistics:\n{df.describe()}")

    # Save to CSV
    output_file = "scraped_books.csv"
    df.to_csv(output_file, index=False)
    print(f"\nData saved to '{output_file}'")

    # Top 5 highest-rated books
    print("\nTop 5 Highest Rated Books:")
    print(df.sort_values("Rating (out of 5)", ascending=False).head())

    # Cheapest 5 books
    print("\nTop 5 Cheapest Books:")
    print(df.sort_values("Price (£)").head())


if __name__ == "__main__":
    main()

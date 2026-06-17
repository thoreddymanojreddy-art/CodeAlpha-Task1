# 📚 Books Web Scraping and Analysis

### CodeAlpha Data Analytics Internship – Task 1

This project demonstrates web scraping using Python by extracting book information from the Books to Scrape website and performing basic data analysis.

---

## 📌 Project Overview

The objective of this project is to collect book data from an online bookstore using web scraping techniques and analyze the extracted information.

The script scrapes multiple pages from the Books to Scrape website and extracts details such as book title, price, rating, and availability.

---

## 🎯 Objectives

* Learn web scraping using Python.
* Extract structured data from web pages.
* Store scraped data in CSV format.
* Perform basic exploratory analysis.
* Identify highly rated and low-priced books.

---

## 📊 Dataset Information

Data is collected directly from:

**Website:** http://books.toscrape.com

### Features Extracted

| Feature | Description |
|----------|-------------|
| Title | Book Title |
| Price (£) | Book Price |
| Rating (out of 5) | Book Rating |
| Availability | Stock Availability |

---

## 🔍 Analysis Performed

* Multi-page Web Scraping
* Data Collection
* Data Cleaning
* CSV Export
* Statistical Summary
* Highest Rated Books Analysis
* Cheapest Books Analysis

---

## 📈 Output Generated

The script generates:

### CSV File

```text
scraped_books.csv
```

Contains all scraped book information.

### Console Output

* Total Books Scraped
* Sample Dataset
* Descriptive Statistics
* Top 5 Highest Rated Books
* Top 5 Cheapest Books

---

## 🔑 Key Insights

* Successfully scraped book information from multiple pages.
* Extracted pricing and rating information.
* Generated structured data suitable for further analysis.
* Identified highest-rated books available.
* Identified lowest-priced books available.

---

## 🛠 Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

---

## ⚙️ Installation

Install required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

---

## ▶️ How to Run

Execute:

```bash
python task1_web_scraping.py
```

The script will:

1. Scrape book data from the website.
2. Extract title, price, rating, and availability.
3. Store data in a DataFrame.
4. Save data to CSV.
5. Display analysis results.

---

## 📁 Project Structure

```text
Books_Web_Scraping/
│
├── task1_web_scraping.py
├── scraped_books.csv
└── README.md
```

---

## 🖼 Sample Output

### Example Dataset

| Title | Price (£) | Rating |
|---------|---------|---------|
| A Light in the Attic | 51.77 | 3 |
| Tipping the Velvet | 53.74 | 1 |
| Soumission | 50.10 | 1 |

---

## 🚀 Future Enhancements

* Scrape all available pages.
* Add data visualization.
* Perform price trend analysis.
* Export data to Excel.
* Build an interactive dashboard.

---

## 👨‍💻 Author

**Thoreddy Manoj Kumar***

Bachelor of Technology (Artificial Intelligence and Data Science)  
Prathyusha Engineering College

LinkedIn:
https://www.linkedin.com/in/thoreddy-manoj-reddy-937b18301?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

GitHub: https://github.com/thoreddymanojreddy-art

---

## 🙏 Acknowledgements

* CodeAlpha
* Books to Scrape
* Python Community
* BeautifulSoup Documentation

---

## 📄 License

This project is intended for educational and internship purposes.

---

⭐ If you found this project useful, consider giving it a star.

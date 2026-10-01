# Professional Scraping Toolkit 🕸️

> A robust, ethical, and portfolio-grade Python web scraping utility collection.

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![CI Status](https://github.com/chetanaybuilder/Data-Scraping-Automation/actions/workflows/ci.yml/badge.svg)

## 📌 Overview
This repository contains an automated scraping toolkit initially built to extract book titles and prices. It has been completely refactored into a scalable, object-oriented architecture employing best practices like retry mechanisms, rate-limiting delays, robust logging, and environmental configuration.

## ✨ Features
- **Robust HTTP Client**: Automatic retries, timeouts, and session management using `requests`.
- **Ethical Scraping**: Respects target servers with built-in request delays.
- **Data Export**: Cleans and serializes scraped data natively to JSON formats.
- **Price Drop Alerts**: Programmable logic to mock or execute price monitoring against historical data.
- **CLI Interface**: Built-in CLI allowing easy execution of varying scrapers.

## 🛠️ Tech Stack
- **Language**: Python 3.9+
- **Libraries**: `requests`, `beautifulsoup4`, `python-dotenv`
- **Testing & Formatting**: `pytest`, `black`, `ruff`

## 📂 Architecture
```
Data-Scraping-Automation/
├── src/scraping_toolkit/
│   ├── __init__.py          # Package initializer
│   ├── config.py            # Environment & config loader
│   ├── http_client.py       # Resilient Requests session wrapper
│   ├── book_scraper.py      # Core scraping logic for books
│   ├── price_tracker.py     # Aggregation and JSON export logic
│   ├── price_drop_alert.py  # Condition monitoring logic
│   ├── utils.py             # Logging and formatting tools
│   └── cli.py               # CLI entry point
├── tests/                   # Pytest suite with mocks
├── pyproject.toml           # Project metadata and tooling
├── requirements.txt         # Dependencies
├── .env.example             # Secret definitions
└── README.md                # Documentation
```

## 🚀 Installation & Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chetanaybuilder/Data-Scraping-Automation.git
   cd Data-Scraping-Automation
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   ```

## 💻 CLI Usage Examples

Run the suite using the built-in CLI:

- **Scrape books and print to console:**
  ```bash
  python -m src.scraping_toolkit.cli books
  ```

- **Track prices and save to JSON:**
  ```bash
  python -m src.scraping_toolkit.cli track --output price_history.json
  ```

- **Check for a price drop:**
  ```bash
  python -m src.scraping_toolkit.cli alert --url https://example.com/product --old-price 60000
  ```

## 🧪 Testing
The project uses `pytest` for unit testing with mocked HTTP responses to prevent unnecessary network load:

```bash
pytest
```

## 📜 Ethical Scraping Disclaimer
This toolkit is designed for educational purposes and authorized data extraction. Always review a website's `robots.txt` and Terms of Service before deploying scrapers. Ensure request delays are adequate to prevent denial-of-service impacts.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## 🧑‍💻 Author
**Chetanay Batra** - [@chetanaybuilder](https://github.com/chetanaybuilder)

## 📄 License
This project is [MIT](LICENSE) licensed.

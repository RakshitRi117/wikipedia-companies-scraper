# Wikipedia Companies Scraper

A Python web scraping project that extracts the table from Wikipedia's [List of largest companies in the United States by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue) and saves it as a CSV file.

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<!-- Add a screenshot of your CSV opened in Excel or of the script running, then delete these comment markers:
![Demo](docs/demo.png)
-->

## About

This project was built to practise web scraping with Beautiful Soup. The script downloads the Wikipedia page, finds the companies table in the HTML, reads the column headers and every row, and stores everything in a pandas DataFrame before writing it to `Companies.csv`.

## Features

- Downloads the page with a descriptive `User-Agent` header
- Stops with a clear error if the page fails to load
- Extracts the column names and all 100 company rows
- Cleans extra spaces and line breaks from every cell
- Exports the data to a CSV file with no index column

## Tech stack

- Python
- Requests
- Beautiful Soup 4
- pandas

## Project structure

```
wikipedia-companies-scraper/
├── data/
│   └── Companies.csv      # sample output
├── LICENSE
├── README.md
├── requirements.txt
└── scrape_wiki.py         # the scraper
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/<your-username>/wikipedia-companies-scraper.git
cd wikipedia-companies-scraper
```

2. Install the required libraries

```bash
pip install -r requirements.txt
```

## Before you run: add your own file path

The script saves the CSV to a location written in the last lines of `scrape_wiki.py`. Open the file and find this line:

```python
df.to_csv(r'C:\Users\YourName\Documents\Companies.csv', index = False)
```

Replace `C:\Users\YourName\Documents` with a folder that exists on your computer, for example your own Windows user name in place of `YourName`.

- Keep the `r` before the quotes. It lets Windows backslashes work correctly.
- The folder must already exist, otherwise Python raises an `OSError`.
- On Mac or Linux, use a path like `'/Users/yourname/Documents/Companies.csv'`.

Also update the `User-Agent` line near the top and replace `<your-username>` with your GitHub username. Wikipedia asks scrapers to identify themselves.

## Usage

```bash
python scrape_wiki.py
```

Expected output:

```
Done! Saved 100 rows to Companies.csv
```

You can also open `scrape_wiki.py` in IDLE and press **F5** to run it.

## Sample output

The full result is in [`data/Companies.csv`](data/Companies.csv). The first rows look like this:

| Rank | Name | Industry | Revenue (USD millions) | Revenue growth | Employees | Headquarters |
|---|---|---|---|---|---|---|
| 1 | Walmart | Retail | 680,985 | 5.1% | 2,100,000 | Bentonville, Arkansas |
| 2 | Amazon | Retail and cloud computing | 637,959 | 11.0% | 1,556,000 | Seattle, Washington |
| 3 | UnitedHealth Group | Healthcare | 400,278 | 7.7% | 400,000 | Minnetonka, Minnesota |
| 4 | Apple | Technology | 391,035 | 2.0% | 164,000 | Cupertino, California |
| 5 | CVS Health | Healthcare | 372,809 | 4.2% | 259,500 | Woonsocket, Rhode Island |

Wikipedia updates this list over time, so running the script later may give different numbers.

## How it works

1. **Request the page**: `requests.get()` downloads the HTML, and `raise_for_status()` stops the script if the request failed.
2. **Parse the HTML**: `BeautifulSoup` turns the page into a searchable structure.
3. **Find the table**: `soup.find_all('table')[0]` selects the first table on the page.
4. **Read the headers**: the `<th>` cells in the first row become the column names.
5. **Read the rows**: each remaining `<tr>` is looped over, and the text of its `<td>` cells is added to the DataFrame.
6. **Save**: `df.to_csv()` writes the DataFrame to a CSV file.

## What I learned

- How a web page is built from HTML tags, and how `table`, `tr`, `th` and `td` map to rows and columns
- How to pick the right table from a page by using its index
- Why a scraper should send a `User-Agent` header and check the response status
- How to build a pandas DataFrame row by row and export it to CSV
- How to prepare a project for GitHub with a README, requirements file and license

## Limitations

- Written for this page's layout. If Wikipedia changes the table structure, the script may need updating.
- All values are saved as text, for example `"680,985"` and `"5.1%"`, not as numbers.
- The output path must be edited by hand before running.
- The data is only as accurate as the Wikipedia page at the time of scraping.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'bs4'` | Run `pip install -r requirements.txt` |
| `OSError: Cannot save file into a non-existent directory` | The folder in your file path does not exist. Create it or correct the path. |
| `PermissionError` | Close `Companies.csv` if it is open in Excel, then run again |
| `HTTPError: 403` or `429` | Check the `User-Agent` line and wait a minute before trying again |

## Responsible scraping

The script makes a single request per run and identifies itself with a `User-Agent`. For heavy or repeated use, prefer the [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page). Wikipedia text is available under the CC BY-SA license.

## Future improvements

- [ ] Convert revenue, growth and employee columns to numbers
- [ ] Let the user choose the output folder from the command line
- [ ] Scrape other Wikipedia tables
- [ ] Add charts, such as revenue by industry

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**[Your Name]**
GitHub: [@your-username](https://github.com/<your-username>)

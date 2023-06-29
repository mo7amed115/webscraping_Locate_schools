# Locate School Data Scraper

This is a Python script that uses Selenium and Pandas libraries to scrape data from the CISCE Locate School website and save it to an Excel file.

## Prerequisites

To run this script, you need to have the following installed:

- Python 3
- Selenium
- Pandas
- Chrome Web Driver

You can install the required Python libraries using pip:

- pip install selenium pandas


## Usage

1. Clone the repository or download the script `locate_school_scraper.py` to your local machine.

2. Install the Chrome Web Driver. You can download it from the official Chrome Driver website: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to download the appropriate version of the driver that matches your Chrome browser version.

3. Update the `options` variable in the script if you want to customize the behavior of the Chrome Web Driver.

4. Run the script by executing the following command:
- python locate_school_scraper.py


5. The script will open the CISCE Locate School website, scrape the data from multiple pages, and save it to an Excel file named `Locate_school.xlsx` in the same directory as the script.

## Notes

- The script uses Selenium to automate web browsing and interact with the website. Make sure you have a stable internet connection while running the script.

- The `result` list stores the scraped data, which is then converted into a Pandas DataFrame. You can modify the `data_dict` dictionary to include additional fields if needed.

- The `columns` list defines the desired order of columns in the Excel file. You can modify it according to your preference.

- The script automatically scrolls to the end of each page to load more data. If you encounter any issues, such as incomplete data or missing pages, you may need to adjust the wait times or update the XPath expressions used for element locating.

- The script saves the data to an Excel file using the `df.to_excel()` method. If you prefer a different file format, you can modify the code accordingly.

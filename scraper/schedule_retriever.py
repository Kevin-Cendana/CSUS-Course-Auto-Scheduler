import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import json

# Set the path to the ChromeDriver executable. The driver for Apple ARM64 is included in the repo.
service = Service('./chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)

# Read the JSON file containing the list of majors
with open("fall-2024-majors.json", "r") as json_file:
    majors = json.load(json_file)

# Initialize a dictionary to store all data
all_data = {}

# Process each major's webpage, extract data, and save it to a JSON file
for major in majors:
    print(f'Scraping major: {major}')
    # Navigate to the target URL for the current major
    url = f"https://www.csus.edu/class-schedule/fall-2024/{major}"
    driver.get(url)

    # Wait for the page to fully load (adjust the delay as needed)
    time.sleep(2)

    # Get the HTML content of the page
    html_content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all <div> elements with class 'table'
    table_divs = soup.find_all('div', class_='table')

    # Initialize data dictionary for the current major
    data = {}

    # Process each table div to extract data
    for table_div in table_divs:
        h2_element = table_div.find('h2')

        # If an <h2> element is found
        if h2_element:
            h2_text = h2_element.text.strip()
            class_name = h2_text.split(' - ')[0]  # Extract the class name
            data[class_name] = []

        # Find all <div> elements with role='row' within the table div
        row_divs = table_div.find_all('div', role='row')
        row_divs = row_divs[1:]  # Drop the header

        # Iterate over each row div
        for row_div in row_divs:
            # Find all child elements within the row div (assuming these represent cells)
            cells = row_div.find_all(recursive=False)
            if len(cells) >= 3:
                days = cells[3].text.strip()
                start_time = cells[5].text.strip()
                end_time = cells[6].text.strip()

                row_data = {
                    'days': days,
                    'startTime': start_time,
                    'endTime': end_time
                }

                if class_name in data:
                    data[class_name].append(row_data)

    # Add the data for the current major to the all_data dictionary
    all_data[major] = data

output_directory = './schedules/'

# Save all data to a single JSON file
output_filename = os.path.join(output_directory, "fall-2024.json")
with open(output_filename, "w", encoding="utf-8") as json_file:
    json.dump(all_data, json_file, indent=4)

# Quit the webdriver
driver.quit()

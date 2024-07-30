import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import schedule


from selenium.common.exceptions import NoSuchElementException

def close_popups(driver):
    try:
        # Example: Closing a specific popup by its class name or id
        popup = driver.find_element(By.CSS_SELECTOR, ".popup-class-name")
        popup_close_button = popup.find_element(By.CSS_SELECTOR, ".close-button-class-name")
        popup_close_button.click()
    except NoSuchElementException:
        pass

def scrape_website():
    # Set up options for headless mode and realistic User-Agent
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--enable-javascript")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Disable popups and notifications
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Disable notifications
        "profile.default_content_setting_values.popups": 2,         # Disable popups
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    data = {}

    try:
        url = 'https://trends.khbrny.com/'

        try:
            # Open the webpage
            driver.get(url)

            close_popups(driver)

            # Wait for the post-title elements to be present
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, '.post-title'))
            )

            # List to hold articles for this URL
            articles = []

            for element in elements:
                try:
                    # Get the title text
                    title = element.text

                    # Click on the element
                    element.click()

                    # Wait for the entry-content element to be present
                    entry_content = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, '.entry-content'))
                    )

                    # Collect article data
                    article = {
                        'name': title,
                        'content': entry_content.text,
                    }

                    articles.append(article)

                    # Go back to the previous page
                    driver.back()

                    # Re-fetch the post-title elements
                    elements = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, '.post-thumb'))
                    )

                    # Throttle requests by adding a delay
                    time.sleep(2)

                except Exception as e:
                    print(f"Error processing element: {e}")
                    continue

            # Add the URL and its articles to the data dictionary
            if articles:
                data[url] = articles

        except Exception as e:
            print(f"Error processing URL {url}: {e}")

    finally:
        driver.quit()

    # Write data to a JSON file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data successfully written to data.json")


# Schedule the scrape_website function to run every 15 minutes
schedule.every(0.01).minutes.do(scrape_website)

print("Scheduler started. Scraping every 15 minutes...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

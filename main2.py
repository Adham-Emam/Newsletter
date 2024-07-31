import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def close_popups():
    try:
        driver.execute_script("""
            var popups = document.querySelectorAll('[class*="popup"], [class*="modal"], [id*="popup"], [id*="modal"]');
            popups.forEach(popup => popup.parentNode.removeChild(popup));
            """)
    except Exception as e:
        print("No close buttons found or clickable:", e)


# Configure Selenium WebDriver
options = Options()
# options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument("--disable-notifications")

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Open the webpage
url = 'https://trends.khbrny.com/'
driver.get(url)

close_popups()

try:
    # Wait for the specific element to load
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.post-thumb'))
    )
except Exception as e:
    print("TimeoutException:", e)
    driver.save_screenshot('error_screenshot.png')
    driver.quit()
    exit()

for element in elements:
    # Click on the element
    element.click()

    # Wait for the title and content to load (if necessary)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.entry-title'))
        )
    except Exception as e:
        print("Error waiting for entry-title:", e)
        continue

    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the title
    entry_title = soup.find('h1', class_='entry-title')
    if entry_title:
        title = entry_title.get_text(strip=True)
        print(f"Title: {title}")
    else:
        print("Title not found.")

    # Extract the image URL
    entry_img = soup.find('img', class_='attachment-full')
    if entry_img:
        img_url = entry_img.get('src')
        print(f"Image URL: {img_url}")
    else:
        print("Image not found.")

    # Extract the content
    entry_content = soup.find('div', class_='entry-content')
    if entry_content:
        content = entry_content.get_text(strip=True)
        print(f"Content: {content}")
    else:
        print("Content not found.")

    print()

    driver.back()


driver.quit()

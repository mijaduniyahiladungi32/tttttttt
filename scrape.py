from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options for headless mode (suitable for GitHub Actions)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the target URL
    target_url = "https://daddylivehd1.my/live/stream-341.php"
    driver.get(target_url)
    print(f"Successfully opened {target_url}")

    # Wait for the page to load (adjust timeout as needed)
    wait = WebDriverWait(driver, 10)

    # Example: Wait for a specific element to be present (modify based on page structure)
    # Replace 'some_element_id' with the actual ID, class, or XPath of an element
    try:
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Page body loaded successfully")
    except Exception as e:
        print(f"Error waiting for element: {e}")

    # Example: Extract the page title
    page_title = driver.title
    print(f"Page Title: {page_title}")

    # Example: Extract specific elements (modify based on your needs)
    # For instance, if you want to extract a stream link or channel name
    try:
        # Replace with actual selector based on inspecting the page
        stream_info = driver.find_element(By.TAG_NAME, "h1").text
        print(f"Stream Info: {stream_info}")
    except Exception as e:
        print(f"Error extracting stream info: {e}")

    # Add more interactions as needed (e.g., clicking buttons, filling forms)
    # Example: driver.find_element(By.ID, "some_button_id").click()

    # Wait briefly to ensure all actions are completed
    time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")

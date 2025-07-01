from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('perfLoggingPrefs', {
    'enableNetwork': True,
    'enablePage': True
})
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Initialize the WebDriver
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    logger.info("WebDriver initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize WebDriver: {str(e)}")
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump({"error": f"WebDriver initialization failed: {str(e)}", "data": []}, f, indent=4)
    exit(1)

# Data structure to store network requests
network_data = []

try:
    # Enable Network domain in Chrome DevTools Protocol
    driver.execute_cdp_cmd('Network.enable', {})
    logger.info("Network domain enabled")

    # Navigate to the target URL
    target_url = "https://daddylivehd1.my/live/stream-341.php"
    driver.get(target_url)
    logger.info(f"Successfully opened {target_url}")

    # Wait for the page to fully load
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    logger.info("Page body loaded successfully")

    # Wait additional time to capture all network requests
    time.sleep(10)  # Increased to ensure more network requests are captured

    # Retrieve performance logs
    logs = driver.get_log('performance')
    logger.info(f"Captured {len(logs)} performance logs")

    # Process network logs
    for log in logs:
        try:
            message = json.loads(log['message'])
            event = message['message']
            # Only process Network.requestWillBeSent and Network.responseReceived events
            if event['method'] in ['Network.requestWillBeSent', 'Network.responseReceived']:
                network_data.append(event)
            else:
                logger.debug(f"Skipping event

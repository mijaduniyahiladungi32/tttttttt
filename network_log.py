from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    requests = []

    def log_request(request):
        requests.append({
            'url': request.url,
            'method': request.method,
            'resource_type': request.resource_type,
            'headers': dict(request.headers)
        })

    page.on('request', log_request)

    page.goto('https://daddylivehd1.my/live/stream-341.php')
    page.wait_for_timeout(5000)

    browser.close()

    with open('network_log.json', 'w', encoding='utf-8') as f:
        json.dump(requests, f, indent=2)

print("✅ Network log saved to network_log.json")

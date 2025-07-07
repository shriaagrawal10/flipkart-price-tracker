# Flipkart Price Tracker

A simple Flask app that tracks the price of a Flipkart product and alerts you if the price drops below your target.  
**Note:** Flipkart frequently changes its site structure and blocks scraping. This project demonstrates the logic, but price scraping may break unless selectors are updated.

## How it works

- Enter a Flipkart product URL, target price, and your email.
- The app attempts to fetch the product title and current price using Selenium.
- If the price is at or below your target, you'll see a success message.

## Limitations

- Flipkart's HTML structure and bot protection change often, so scraping may not always work.
- For demonstration/portfolio purposes.

## To run locally

1. Install dependencies:
    ```
    pip install flask selenium
    ```
2. Download and place [ChromeDriver](https://chromedriver.chromium.org/) in your PATH.
3. Run:
    ```
    python app.py
    ```
---

### 6. **Push README.md**
```bash
git add README.md
git commit -m "Add README"
git push

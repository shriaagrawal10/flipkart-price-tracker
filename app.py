from flask import Flask, render_template, request, redirect, url_for, flash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

# --- Price Scraper Function ---
def check_flipkart_price(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(product_url)
    time.sleep(3)  # Wait for JS to load

    try:
        price = driver.find_element(By.CLASS_NAME, "_16Jk6d").text
        price_value = float(price.replace("₹", "").replace(",", "").strip())
        title = driver.find_element(By.CLASS_NAME, "B_NuCI").text
    except NoSuchElementException:
        price_value = None
        title = "Product Not Found"
    driver.quit()
    return price_value, title

# --- Flask Routes ---
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    url = request.form.get('product_url')
    price_limit = float(request.form.get('price_limit'))
    email = request.form.get('email')

    # Call the scraper
    current_price, product_title = check_flipkart_price(url)
    print(f"User wants to track: {product_title} | Current Price: {current_price} | Target: {price_limit} | Email: {email}")

    if current_price is None:
        flash("Could not find product or price. Please check the URL.", "error")
    elif current_price <= price_limit:
        flash(f"Good news! {product_title} is now ₹{current_price} (at or below your target of ₹{price_limit}).", "success")
        # TODO: Email logic here
    else:
        flash(f"Current price for {product_title} is ₹{current_price}. Still above your target of ₹{price_limit}.", "info")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

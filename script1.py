from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pdb
driver =  webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver.get("http://demostore.supersqa.com/")

#por ID
search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys("beanie")
search_field.send_keys(Keys.ENTER)

#por CSS selector
add_to_cart = driver.find_element(By.CSS_SELECTOR, "#main > ul > li.product.type-product.post-16.status-publish.instock.product_cat-accessories.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
add_to_cart.click()

pdb.set_trace()
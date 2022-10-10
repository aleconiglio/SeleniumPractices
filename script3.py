from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

primero = int(input("primer numero: "))
segundo = int(input("segundo numero: "))
operacion = input("'A' para suma, 'S' para resta, 'M' para multiplicacion, 'D' para division ")
if operacion == "A":
    resultado = primero + segundo
    formula = "sumar"
elif operacion == "S":
    resultado = primero - segundo
    formula = "restar"
elif operacion == "M":
    resultado = primero * segundo
    formula = "multiplicar"
elif operacion == "D":
    resultado = primero / segundo
    formula = "dividir"

driver =  webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://testsheepnz.github.io/BasicCalculator.html")

search_field = driver.find_element(By.ID, "selectBuild")
search_field.send_keys("1")
search_field.send_keys(Keys.ENTER)
first_number = driver.find_element(By.ID, "number1Field")
first_number.send_keys(primero)
second_number = driver.find_element(By.ID, "number2Field")
second_number.send_keys(segundo)
operation = driver.find_element(By.ID, "selectOperationDropdown")
operation.send_keys(operacion)
operation.send_keys(Keys.ENTER)
calculate = driver.find_element(By.ID, "calculateButton")
calculate.click()
answer = float(driver.find_element(By.ID, "numberAnswerField").get_attribute("value"))
assert answer == resultado , f"The answer is not 3, is: {answer}"
print("Test satisfactorio, el resultado de {} los numeros {} y {} es de {}".format(formula, primero, segundo, resultado))

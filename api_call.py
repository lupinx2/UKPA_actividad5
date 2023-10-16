import requests
#Para utilizar este script, el archivo api_sum.php debe estar hosteado en un servidor local
#que este corriendo en el puerto 6660, yo lo probe con Apache2
url = 'http://127.0.0.1:6660//api_sum.php'
params = {'num1': 1, 'num2': 2}
url_with_params = url + "?num1=" + str(params['num1']) + "&num2=" + str(params['num2'])
response = requests.get(url, params=params)
print("BEGIN RESULT")
print(response.text)
print("END RESULT")
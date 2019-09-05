from flask import Flask, render_template
import pandas as pd
import time

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods = ['GET'])
def formulario():
    tiempo_actual = time.strftime("%c")
    data = {'fecha':[tiempo_actual], 'tiempo': [2.22], 'temperatura': [22.7], 'humedad': [33.2]}
    df = pd.DataFrame(data, columns= ['fecha', 'tiempo', 'temperatura', 'humedad'])
    df.to_csv("09052019.csv")
    return render_template('index.html')

if __name__=="__main__":
    app.run(host= "0.0.0.0", port = 4000, debug=True)
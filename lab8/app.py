import flask
import pandas as pd

app = flask.Flask(__name__)
app.debug = True

@app.route('/')
def index():
    with open('./data.txt', 'r', encoding='utf-8') as f:
        dataframe = pd.read_csv(f, sep='\t', names=['number', 'country', '2014', '2013', '2012'])
        print(dataframe)
    return flask.render_template('index.html', data = dataframe.iterrows())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)
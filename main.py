from flask import Flask, render_template, request
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = pd.DataFrame()

    if request.method == 'POST':
        file = request.files['csv_file']
        if file:
            data = pd.read_csv(file)
            data.head()
            data.isnull().any()

            label_encoder = preprocessing.LabelEncoder()
            cols = ['G1', 'G2', 'G3', 'Final Result']
            data[cols] = data[cols].apply(label_encoder.fit_transform)

            # Modify final result based on G4 value
            data['Final Result'] = data.apply(lambda row: 'Pass' if row['G4'] > 20 else 'Fail', axis=1)

            x = data.iloc[:, :-1]
            y = data.iloc[:, -1]

            X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.20, shuffle=True)

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

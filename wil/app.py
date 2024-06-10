from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def preview_data(self):
        return self.data.head(10)

    def calculate_statistics(self):
        return self.data.describe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file_path = f"uploads/{file.filename}"
        file.save(file_path)
        data_handler = DataHandler(file_path)
        data_handler.load_data()
        return render_template('result.html', preview=data_handler.preview_data(), statistics=data_handler.calculate_statistics())
    else:
        return "No se ha seleccionado ningún archivo."

if __name__ == "__main__":
    app.run(debug=True)

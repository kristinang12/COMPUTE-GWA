from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        grades = list(map(float, request.form.getlist('grade')))
        units = list(map(float, request.form.getlist('unit')))
        
        if len(grades) != len(units) or not grades:
            return "Invalid input, please ensure all fields are filled and correct."

        total_units = sum(units)
        weighted_sum = sum(g * u for g, u in zip(grades, units))
        gwa = weighted_sum / total_units

        return f'<p>Computed GWA is: {gwa:.2f}</p>'
    except ValueError:
        return "Invalid input, please enter numerical values."

if __name__ == '__main__':
    # Use the PORT environment variable if available, otherwise default to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)


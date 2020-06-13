__author__ = 'maheshwickramasinghe'


#import sys
#sys.path.append('./server')
import util
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/predict_prob', methods=['GET', 'POST'])
def predict_prob_compliance():

    fine = float(request.form['fine'])
    discount = float(request.form['discount'])
    judgment_amount = float(request.form['judgment_amount'])
    late_fee = float(request.form['late_fee'])

    response = jsonify({
        'probability': util.predict_prob_compliance(fine, discount, judgment_amount, late_fee)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python Flask server")
    app.run(debug=True)
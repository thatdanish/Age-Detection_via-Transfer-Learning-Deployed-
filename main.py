from flask import Flask,request,jsonify
from processing import call_model,preprocess
import io
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/deploy',methods=['POST'])
def prediction():
    data = {'success':False}

    if request.method == 'POST':
        if request.files.get('image'):
            image = request.files['image'].read()
            image = Image.open(io.BytesIO(image))

            image = preprocess(image,target=(64,64))
            preds = model.predict(image)
            preds = [np.argmax(i) for i in preds]

            data['prediction'] = preds
            data['success'] = True

    return jsonify(data)  


if __name__ == '__main__':
    model = call_model()
    app.run(debug=True)

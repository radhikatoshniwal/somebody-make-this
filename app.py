from flask import Flask, render_template
import random

from firebase_admin import credentials, firestore, initialize_app
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
app = Flask(__name__)

@app.route('/')
def hello():
    r=random.randint(0,1998)
    result=db.collection(u'ideas').document(str(r)).get().to_dict()
    if (result['description']=='[removed]' or result['description']=='[deleted]'):
        result["description"]='' 

    return render_template("onepager.html", result = result)

if __name__ == '__main__':
    app.run()
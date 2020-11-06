import flask
from utils import *
import tensorflow as tf
# Use pickle to load in the pre-trained model
# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route

l=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
@app.route('/', methods=['GET', 'POST'])
def main():
    return(flask.render_template('main.html'))


@app.route('/draw')
def draw1():
    try: 
        a1 = flask.request.args.get('Tweet')
        model=tf.keras.models.load_model('Model1.h5')
        
        img=toImage(str(a1))
        
        prediction=model.predict_classes(img)[0]
        return flask.render_template('main.html',
                                         result=l[prediction]
                                         )
    except Exception:
        return flask.render_template('main.html',
                                         result='Something went wrong please try again :)'
                                         )


if __name__ == '__main__':
    app.run()

'''Emotion Detector deployment on the server so that the customers can access it over.
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package.

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app.
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions along with dominant emotion.
    '''
    # GET request.
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass response to emotion detector.
    response = emotion_detector(text_to_analyze)

    # Error handling for dominant_emotion is None.
    """if response['dominant_emotion'] is None:
        return (f"<b>Invalid text! Please try again!<b>")"""

    # The response.
    return (
        f"For the given statement, the system reponse is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy: {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}<b>."
    )

    
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Render HTML page.
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
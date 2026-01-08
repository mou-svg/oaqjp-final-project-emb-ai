#importing libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Flask initiation
app = Flask("Emotion Detector")

#adding routes
@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emot_detector function and store the response
    response = emotion_detector(text_to_analyze)
    #response parsing
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    #error handling
    if dominant_emotion is None:
        return "Invalid input! Try again."

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}." .format(anger, disgust,fear, joy, sadness, dominant_emotion)   

#rendermodule
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

my_app = Flask('Final Project')


@my_app.route('/emotionDetector')
def sent_emotion():
    text_to_check = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_check)
    return f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, \
    'joy': {response['joy']} and 'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

@my_app.route("/") 
def render_index_page(): 
    return render_template('index.html')

if __name__ == '__main__':
    my_app.run(host='localhost', port=5000)
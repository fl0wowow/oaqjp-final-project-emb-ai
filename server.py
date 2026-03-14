'''
Module created in order to define emotions based on provided text
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

my_app = Flask('Final Project')


@my_app.route('/emotionDetector')
def sent_emotion():
    '''
    Sending request to existing AI model to get 
    emotion description based on text provided
    '''
    text_to_check = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_check)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, 'fear': {response['fear']}, \
    'joy': {response['joy']} and 'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

@my_app.route("/")
def render_index_page():
    '''
    Render template index.html
    '''
    return render_template('index.html')

if __name__ == '__main__':
    my_app.run(host='localhost', port=5000)

''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask
from EmotionDetection import emotion_detector

app = Flask('Emotion Predictor')

@app.route('/<textToAnalyze>')
def emotion_predictor(text_to_analyze):
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and its confidence 
        score for the provided text.
    '''
    emotions = emotion_detector(text_to_analyze)
    print('emotions', emotions)
    if emotions is None:
        return '<b>Invalid text! Please try again!</b>'

    return f"For the given statement, the system response is 'anger': {emotions['anger']}, " + \
           f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, " + \
           f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. " + \
           f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>."

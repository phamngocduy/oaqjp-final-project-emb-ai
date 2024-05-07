import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    body = { 'raw_document': { 'text': text_to_analyze }}
    header = { 'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock' }
    response = requests.post(url, json=body, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotion_score = 0
        emotion_name = None
        for emotion in emotions.keys():
            if emotions[emotion] > emotion_score:
                emotion_score = emotions[emotion]
                emotion_name = emotion
        emotions['dominant_emotion'] = emotion_name
        return emotions
    return None
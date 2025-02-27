import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inp = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=inp)
    
    if response.status_code == 200:
        predictions = response.json().get('emotionPredictions', [{}])[0].get('emotion',{})

        return {
            'anger': predictions.get('anger', 0),
            'disgust': predictions.get('disgust', 0),
            'fear': predictions.get('fear', 0),
            'joy': predictions.get('joy', 0),
            'dominant_emotion': max(predictions, key=predictions.get)
        }
    else:
        return {"error": f"Error {response.status_code}"}

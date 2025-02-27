from emotion_detection import emotion_detector

def emotion_test():
    result = emotion_detector("I am glad this happened")
    if result['dominant_emotion'] != 'joy':
        return {"error": "Emotion detector doesn't work properly (joy)"}

    result = emotion_detector("I am really mad about this")
    if result['dominant_emotion'] != 'anger':
        return {"error": "Emotion detector doesn't work properly (anger)"}

    result = emotion_detector("I feel disgusted just hearing about this")
    if result['dominant_emotion'] != 'disgust':
        return {"error": "Emotion detector doesn't work properly (disgust)"}

    result = emotion_detector("I am so sad about this")
    if result['dominant_emotion'] != 'sadness':
        return {"error": "Emotion detector doesn't work properly (sadness)"}

    result = emotion_detector("I am really afraid that this will happen")
    if result['dominant_emotion'] != 'fear':
        return {"error": "Emotion detector doesn't work properly (fear)"}
    
    return "Everything works!"
from EmotionDetection import emotion_detector
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid input. Please provide a text field."}), 400

    text_to_analyze = data['text']
    emotions = emotion_detector(text_to_analyze)

    return jsonify({"response": json.dumps(emotions), "raw_output": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

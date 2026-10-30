from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('EmotionDetector')

@app.route("/emotionDetector")
def sent_analyzer():
    text_input = request.args.get('Text_to_Analysis')
    if not text_input:
        return jsonify({'error':'not text input'}), 400
    try:
        response = emotion_detector(text_input)
    except Exception:
        app.logger.exception("Emotion detection service failed")
        return jsonify({'error': 'Emotion detection service is unavailable.'}), 502
    
    if response.get('dominant_emotion') is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400
    
    return jsonify(response)

@app.route('/')
def render_page():
    return render_template('index.html')

if __name__ == "__main__": 
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
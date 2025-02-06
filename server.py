from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector



app = Flask("emotion detector")
@app.route("/emotionDetector")
def sent_analyzer():
    # Récupérer le texte à analyser depuis la requête
    text_to_analyze = request.args.get('textToAnalyze')

    # Vérifier si le texte est fourni
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Appeler la fonction emotion_detector
    emotions, dominant_emotion = emotion_detector(text_to_analyze)

    # Construire la réponse formatée
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return response_text



@app.route("/")
def render_index_page():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
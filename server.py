"""
Flask Server for Emotion Detection API.
This server provides an API endpoint to analyze emotions in a given text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    API endpoint to analyze emotions in the provided text.

    Returns:
        - A formatted string with detected emotions and the dominant emotion.
        - If no text is provided, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detection function
    emotions, status_code = emotion_detector(text_to_analyze)

    # If the input is invalid, return an error message
    if status_code == 400 or emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400

    # Construct the formatted response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_text, 200

@app.route("/")
def render_index_page():
    """
    Renders the homepage for the emotion detector application.

    Returns:
        HTML page for user interaction.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # You can change port if needed

#end

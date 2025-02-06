import requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json=myobj, headers=header)  
    
    # Vérification de la réponse HTTP
    if response.status_code != 200:
        return {"error": f"Erreur de requête: {response.status_code}", "details": response.text}
    
    # Parsing du JSON
    formatted_response = json.loads(response.text)

    # Vérifier si 'emotionPredictions' existe et contient des éléments
    if "emotionPredictions" not in formatted_response or not formatted_response["emotionPredictions"]:
        return {"error": "Données d'émotion manquantes dans la réponse"}

    # Extraire les émotions du premier élément de la liste
    emotions_data = formatted_response["emotionPredictions"][0].get("emotion", {})

    # Vérification que toutes les émotions sont présentes
    required_emotions = ["anger", "disgust", "fear", "joy", "sadness"]
    emotions = {emotion: emotions_data.get(emotion, 0.0) for emotion in required_emotions}

    # Trouver l'émotion dominante
    dominant_emotion = max(emotions, key=emotions.get)

    return emotions, dominant_emotion
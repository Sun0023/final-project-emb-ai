"""This module is about detecting the emotion from a customer
feedback on a e-commerce site."""

# Import libraries.
import json
import requests

# Define function emotion_detector.
def emotion_detector(text_to_analyse):
    """This function uses text to detect emotion of customers."""
    # Input: text_to_analyse variable.
    # Output: The emotion of a customer from the text.

    # Get the URL to fetch the emotion detection from Watson NLP Library.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # The headers of the request for the above url.
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # The input is in the format of json.
    myobject = { "raw_document": { "text": text_to_analyse } }

    # Use the post method
    response = requests.post(url, json = myobject, headers = headers)

    # Return the respons in the text format.
    # Formatting the text to json.
    formatted_response = json.loads(response.text)

    # Extrating emotion.
    # "formatted_response" has two key values, with nested list and dictionaries inside. 
    # Use get('key') method to extract the values of dictionary from a list inside a dictionary.
    emotions = formatted_response['emotionPredictions'][0].get('emotion')

    # Extract dominant emotion with max(data, key=data.get) method.
    dominant_emotion = max(emotions, key = emotions.get)

    # Add the dominant emotion to the dictionary(=emotions) back.
    emotions['dominant_emotion'] = dominant_emotion 

    # Error handling for 400 status code.
    """if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }"""
    
    # Now get the emotions. Really?
    return emotions 

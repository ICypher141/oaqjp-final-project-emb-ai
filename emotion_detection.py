import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request to Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Return the text attribute of the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to analyze the text"}

# Test function (optional for debugging)
if __name__ == "__main__":
    result = emotion_detector("I love this new technology.")
    print(result)

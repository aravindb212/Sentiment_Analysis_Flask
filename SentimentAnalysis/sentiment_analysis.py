import requests
import json
def sentiment_analyzer(text_to_analyse):
    URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    Headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url= URL, json = myobj, headers=Headers)
    format_response = json.loads(response.text)

    if response.status_code == 200:
        label = format_response['documentSentiment']['label']
        score = format_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    return {'label' : label , 'score': score}

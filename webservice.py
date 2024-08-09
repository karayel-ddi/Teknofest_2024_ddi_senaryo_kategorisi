from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForTokenClassification, BertTokenizerFast
from absa import ABSAModel

app = Flask(__name__)

ner_model_path = r"\bert_model"

finetuned_model = AutoModelForTokenClassification.from_pretrained(ner_model_path)
tokenizer = BertTokenizerFast.from_pretrained(ner_model_path)

@app.route('/predict/', methods=['POST'])
def response_dondur(finetuned_model=finetuned_model, tokenizer=tokenizer):
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": "Geçersiz JSON verisi veya veri okunamıyor."}), 400

    sentence = data.get('text', '').lower()
    
    ner = pipeline("ner", model=finetuned_model, tokenizer=tokenizer, device=-1)
    result = ner(sentence)

    entities = [i for i in result if i['entity'] == 'B-ORG']

    modelABSA = ABSAModel(tokenizer, adapter=False)
    absa_model_path = r".\model_lr1e-05_epochs3_batch8.pkl"

    entity_list = [i['word'] for i in entities]
    sentiment_results = []

    for i in entities:
        x, y, z = modelABSA.predict(sentence, i['word'], load_model=absa_model_path)
    
        if y == 1:
            sentiment_results.append({'entity': i['word'], 'sentiment': 'olumlu'})
        elif y == 0:
            sentiment_results.append({'entity': i['word'], 'sentiment': 'nötr'})
        else:
            sentiment_results.append({'entity': i['word'], 'sentiment': 'olumsuz'})

    result = {
        "entity_list": entity_list,
        "results": sentiment_results
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5523, debug=False)

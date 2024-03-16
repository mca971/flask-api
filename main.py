from flask import Flask, request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'mp3', 'wav'}


def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route("/ping", methods=['GET'])
def ping():
    print("9999999999999999999999999999999999999999999999999")
    return "Ok"

@app.route("/voice/analyze", methods=['GET', 'POST'])
def get_score():
    req_data = request.get_json()
    audio_path = req_data['sample']
    if audio_path[-3:].lower() in ALLOWED_EXTENSIONS:
        responseObject = {
            "status": "success",
            "analysis": {
                "detectedVoice": True,
                "voiceType": "human",
                "confidenceScore": {
                    "aiProbability": 5,
                    "humanProbability": 95
                },
                "additionalinfo": {
                    "emotionalTone": "neutral",
                    "backgroundNoiselevel": "low"
                }},
            "responseTime": 200}

        return responseObject
    else:
        return "Invalid audio file extension"


if __name__ == '__main__':
    app.run(port=8080, debug=True)

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench"/<textToTranslate>/french_text)
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.english_to_french(textToTranslate)
    # Write your code here
    return english_text

@app.route("/frenchToEnglish"/<textToTranslate>/english_text)
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    french_text= translator.french_to_english(textToTranslate)
    return french_text

@app.route("/index.html")
def renderIndexPage():
    return render_template('index.html')

 if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

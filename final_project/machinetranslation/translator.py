"""This Directory provides logic to
the translator service
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# Creates an instance of Translator Service
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    translation= language_translator.translate(text= english_text, model_id= 'en-fr').get_result()
    # Result from english input
    french_text = translation['translations'][0]['translation']

    return french_text

#This method converts French into English
def french_to_english(french_text):
    translation = language_translator.translate(
        text = french_text, model_id='fr-en' ).get_result()
# Result from french input
    english_text = translation['translations'][0]['translation']
    return english_text

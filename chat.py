"""
file: chat.py
------------------
Illustrates using cohere.ai to create a chatbot. 
Inspired by https://github.com/harish-garg/cohereai-chat-commandline. 
"""

import os
import pdb
import cohere

cohere_client = cohere.Client(os.environ.get('COHERE_API_KEY'))

while True:
    user_prompt = input("Enter prompt: ")
    
    if user_prompt == "quit":
        break

    response = cohere_client.chat(user_prompt).reply

    print("Cohere chatbot: ", response)
    print("------------------")

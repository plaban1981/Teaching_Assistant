from PIL import Image
import os
import openai
from random import choice
import json

def preprocess_function(text_path,content_type = None ):
    print(text_path)
    with open(text_path,"r",encoding='utf-8') as f:
        data = f.read()
    print(data)
    #data = text_path.read().decode('utf-8')
    return data
#
# 
def predict_function(context,model_path): 
    file_path = os.path.join(model_path,"api.txt")
    with open(file_path,"r",encoding='utf-8') as f:
        api = f.read()
    openai.api_key = api
    #
    response = openai.Completion.create(
               model="text-davinci-003",
               prompt=context,
               temperature=0.7,#randomness of the answer
               max_tokens=1024,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
               )

    answer = response.choices[0].text
    return answer

   
#
def model_load_function(model_path):
    return model_path

#
def postprocess_function(predictions,content_type = None ):
    return json.dumps({"response":predictions})

## Test the script
"""
if __name__ == '__main__':
    txt_path = "./model_files/test.txt"
    data = preprocess_function(txt_path)
    model_path = "./model_files"
    path = model_load_function(model_path)
    predictions = predict_function(data,path)
    out = postprocess_function(predictions)
    print(out)
    
"""

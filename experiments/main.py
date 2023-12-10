import json
import os

def make_few_shot_context(data):
    text = data['text'] 

    examples = [] 
    for item in data['properties']:
        examples.append(  f"type: {item['type']}\ntext: {item['text']}\n")

    examples_str = "\n".join(examples)

    few_shot_context = f"""
        EXAMPLE
        source_text: {text}

        contained_information:
        {examples_str}
    """
    return few_shot_context

directory = "./data/msnotesannotator_audition_certificates_data-master/"
json_data = []

for filename in os.listdir(directory)[:5]:
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f) as file:
            data = json.load(file)
            json_data.append(data)

for data in json_data:
    print(make_few_shot_context(data))




        



    

    
    
    

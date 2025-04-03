import yaml
from yaml import load, load_all

stream = open('sample.yaml', 'r')
documents = load_all(stream, Loader = yaml.FullLoader)

print('Type of the yaml document: ', type(documents))

for doc in documents:
    print('Type of the items in the yaml document: ', '\b',  type(doc), '\n')
    print("The 'layer_config' object is: ", '\n', doc['layer_config'], '\n')
    print("The second item in 'input_shape' object is: ",doc['layer_config'][1])


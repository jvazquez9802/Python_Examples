import json

mensaje_dict = {'Luisa': 'Juan Luis', 'Contenido': 'Hola', 'Receptor': 'Pedro'}

with open("json.json", "r+") as json_file:
    info = json.load(json_file)
    print(info)
    for mensaje in info["Mensajes"]:
        print(f"{mensaje.get('Emisor')}")
    
    info["Mensajes"].append(mensaje_dict)
    
    nuevo = json.dump(info)
    print(nuevo.__class__)
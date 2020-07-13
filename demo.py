from explode_json.explode_json import explode_json

explode_json(
    open("./example/notebook.ipynb").read(),
    "example/notebook"
)
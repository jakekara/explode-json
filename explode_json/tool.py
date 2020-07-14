import argparse
from .explode_json import explode_json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="a valid JSON file")
    parser.add_argument("dest_dir", help="a NONEXISTENT path to store the resulting directory")

    options = parser.parse_args()

    try:
        explode_json(
            open(options.json_file).read(), 
            options.dest_dir
        )
    except Exception as e:
        print("\n:( Something went wrong while exploding: " + str(e) + "\n")


import yaml
import json

yaml_file = yaml.safe_load(open('config.yaml'))

def get_letters():
    return yaml_file['letters']

def get_max_trials():
    return yaml_file['max_trials']

def get_max_swaps():
    return yaml_file['max_swaps']

def open_matrix(matrix_path = 'matrix.json'):
    with open(matrix_path, "r") as f:
        return json.loads(f.read())
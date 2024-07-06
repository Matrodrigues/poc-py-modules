import yaml
import re

class YamlFunctions:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_yaml()

    def load_yaml(self):
        with open(self.file_path, 'r') as file:
            return yaml.safe_load(file)

    def save_yaml(self, file_path):
        with open(file_path, 'w') as file:
            yaml.safe_dump(self.data, file)

    def replace_in_yaml(self, data, pattern, replacement):
        if isinstance(data, dict):
            return {key: self.replace_in_yaml(value, pattern, replacement) for key, value in data.items()}
        elif isinstance(data, list):
            return [self.replace_in_yaml(element, pattern, replacement) for element in data]
        elif isinstance(data, str):
            return re.sub(pattern, replacement, data)
        else:
            return data

    def process_yaml_replacement(self, pattern, replacement):
        return self.replace_in_yaml(self.data, pattern, replacement)
import json

def load_profile(path='config/profile.json'):
    with open(path, 'r') as file:
        return json.load(file)

class Identity:
    def __init__(self, profile):
        self.name = profile["name"]
        self.mode = profile["default_mode"]
        self.traits = profile["core_traits"]
        self.available_modes = profile["modes"]

    def switch_mode(self, new_mode):
        if new_mode in self.available_modes:
            self.mode = new_mode
            return f"Modo alterado para {new_mode}"
        else:
            return "Modo inválido"

class SoundGenerator:
    def __init__(self):
        pass

    def generate_soundscape(self, type_of_sound: str) -> str:
        if type_of_sound == "ocean":
            return self._generate_ocean_soundscape()
        elif type_of_sound == "forest":
            return self._generate_forest_soundscape()
        elif type_of_sound == "rain":
            return self._generate_rain_soundscape()
        else:
            raise ValueError("Unknown sound type")

    def _generate_ocean_soundscape(self) -> str:
        # Logic to generate ocean soundscape
        return "Ocean soundscape generated"

    def _generate_forest_soundscape(self) -> str:
        # Logic to generate forest soundscape
        return "Forest soundscape generated"

    def _generate_rain_soundscape(self) -> str:
        # Logic to generate rain soundscape
        return "Rain soundscape generated"
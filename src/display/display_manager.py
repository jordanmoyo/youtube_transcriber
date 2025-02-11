# Handles displaying transcriptions
        
class DisplayManager:
    def __init__(self):
        self.transcriptions = []

    def update_display(self, text):
        self.transcriptions.append(text)
        print("\n".join(self.transcriptions))

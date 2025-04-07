from abc import ABC

class GeneralFlow(ABC):

    def __init__(self):
        super().__init__()
    pass



class Diagnosis(GeneralFlow): # maybe I gonna have an intermediate class not directly inherit from general flow?
    pass
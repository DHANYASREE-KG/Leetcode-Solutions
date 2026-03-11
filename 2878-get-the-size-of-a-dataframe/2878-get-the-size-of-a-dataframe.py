import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
           s=list(players.shape)
           return s
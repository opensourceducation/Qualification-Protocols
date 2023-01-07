import smartpy as sp
import pandas as pd


class Ar_Fielts(sp.Contract):

    def __init__(self, data):
        self.init(data=data)

    @sp.entry_point
    def average(self, params):
        df = pd.DataFrame(self.data.data)
        avg = df[params.column].mean()
        return avg

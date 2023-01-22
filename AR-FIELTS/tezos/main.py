import smartpy as sp
import pandas as pd
from fake_identity_protocol import Identity_Protocol


class Ar_Fielts:
    def __init__(self, uuid, skill):
        self.uuid = uuid
        self.skill = skill
        self.data = ''

    def __get_user_data(self):
        user_data = Identity_Protocol(self.uuid)
        self.data = user_data.search_data()

    def get_skill(self):
        self.__get_user_data()
        df = pd.read_csv(self.data, sep=';')
        df.sort_values("timestamp", ascending=True, inplace=True)
        my_query = f"topics.str.contains('{self.skill}')"
        print(my_query)
        print(df.query(my_query))


# class Ar_Fielts(sp.Contract):

#     def __init__(self, data):
#         self.init(data=data)

#     @sp.entry_point
#     def average(self, params):
#         # df = pd.DataFrame(self.data.data)
#         print(self.data)
#         # avg = df[params.column].mean()
#         # return avg

import smartpy as sp
import pandas as pd

# print("sp")
# print(sp)


class Ar_Fielts:
    def __init__(self, data, skill):
        self.data = data
        self.skill = skill

    def average(self):
        print("mi data")
        df = pd.read_csv('../fake_oscar_dataset.csv', sep=';')
        df.sort_values("timestamp", ascending=True, inplace=True)
        my_query = f"topics.str.contains('{self.skill}')"
        print(my_query)
        print(df.query("topics.str.contains('react')"))

        # class Ar_Fielts(sp.Contract):

        #     def __init__(self, data):
        #         self.init(data=data)

        #     @sp.entry_point
        #     def average(self, params):
        #         # df = pd.DataFrame(self.data.data)
        #         print(self.data)
        #         # avg = df[params.column].mean()
        #         # return avg

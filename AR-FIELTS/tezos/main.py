import smartpy as sp
import pandas as pd
from datetime import datetime
from fake_identity_protocol import Identity_Protocol


class Ar_Fielts:
    def __init__(self, uuid, skill):
        self.uuid = uuid
        self.skill = skill
        self.data = ''

    def __get_user_data(self):
        user_data = Identity_Protocol(self.uuid)
        self.data = user_data.search_data()

    def __get_time_lapse(self, timestamp1, timestamp2):
        date1 = datetime.strptime(timestamp1, '%Y-%m-%d %H:%M:%S')
        date2 = datetime.strptime(timestamp2, '%Y-%m-%d %H:%M:%S')
        time_diff = date2 - date1
        return time_diff.days

    def __get_timelapse_between_dataframes(self, timestamps_list):
        result = []
        for i in range(len(timestamps_list) - 1):
            result.append(self.__get_time_lapse(
                timestamps_list[i], timestamps_list[i+1]))

        return result

    def get_skill(self):
        self.__get_user_data()
        df = pd.read_csv(self.data, sep=';')
        df.sort_values("timestamp", ascending=True, inplace=True)
        my_query = f"topics.str.contains('{self.skill}')"
        skill_to_measure = df.query(my_query)
        timestamps = list(skill_to_measure['timestamp'].values)
        timestamps.append(str(datetime.now().replace(microsecond=0)))
        df_amount = len(timestamps)
        knowledge_range = self.__get_time_lapse(timestamps[0], timestamps[-1])
        timelapse_between_dataframes = self.__get_timelapse_between_dataframes(
            timestamps)
        mean_timelapse = pd.DataFrame(timelapse_between_dataframes, columns=[
                                      'timelapse'])['timelapse'].mean()
        return {
            'knowledge_range': knowledge_range,
            'mean_timelapse': mean_timelapse,
            'df_amount': df_amount
        }


# class Ar_Fielts(sp.Contract):

#     def __init__(self, data):
#         self.init(data=data)

#     @sp.entry_point
#     def average(self, params):
#         # df = pd.DataFrame(self.data.data)
#         print(self.data)
#         # avg = df[params.column].mean()
#         # return avg

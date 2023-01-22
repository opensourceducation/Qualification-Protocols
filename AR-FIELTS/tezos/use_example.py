from main import Ar_Fielts

# The contracts receives 3 arguments:
# 1 The uuid key of Oscar for extract the data on another protocol
# 2 The skill to measure
contract = Ar_Fielts('b9f6b9c6-f8d2-4816-87a7-b9a2d1c8f8f3', 'python')

result = contract.get_skill()

# result = contract.get_skill(column="topics").export()

# assert result == 3.0

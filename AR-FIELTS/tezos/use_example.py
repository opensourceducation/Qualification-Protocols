from main import Ar_Fielts

# The contracts receives the uuid key for extract and decrypt the data of another protocol, and the skill to measure
contract = Ar_Fielts(fake_data, 'react')

result = contract.average()

# result = contract.average(column="topics").export()

# assert result == 3.0

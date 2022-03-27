import re

input1 = "This company is not poor at all."
print(re.sub("not.*at all", "good", input1))

# input2 = "I'm not at all happy about it."
# print(re.sub("not.*at all", "good", input2))

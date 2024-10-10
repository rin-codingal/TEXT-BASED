import pandas as pd
import numpy as np

exam_data  = {"name": ["Laura", "Jessica", "Jack", "Andrew", "Matthew", "Rachel", "Jeff", "Audrey", "Veronica", "Roger"],
        "score": [13.5, 11, 17.5, np.nan, 10, 21, 13.5, np.nan, 7, 19],
        "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"]}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(exam_data , index=labels)
print("Summary of the basic information about this DataFrame and its data:")

print()

print(df.info())
import pandas as pd
import numpy as np

exam_data  = {
        "name": ["Anna", "James", "Cathy", "Frank", "Audrey", "Jordan", "Andrew", "Jessica", "Riley", "Amber"],
        "score": [13.5, 9, 17.5, np.nan, 9, 23, 14.5, np.nan, 8, 17],
        "attempts": [1, 3, 2, 3, 2, 3, 2, 1, 2, 1],
        "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"]
            }

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(exam_data , index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())
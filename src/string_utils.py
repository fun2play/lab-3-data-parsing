# import pandas as pd
# import string
# def clean_strings(strings):
#     strings = strings.str.strip()
#     assert strings.str.contains(' ') == -1
#     strings = strings.str.lower()
#     assert strings.str.islower()
#     strings = strings.str.replace(f'[{string.punctuation}]','', regex=True)
#     assert strings.str.contains(string.punctuation) == -1
#     strings.dropna(inplace=True)
#     return strings
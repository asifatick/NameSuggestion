#import numpy as np
import pandas as pd
from symspellpy import SymSpell,Verbosity
from collections import Counter

names = pd.read_csv("bnames.csv")
print(names)
nsorted = names.sort_values(by = "Name")
nameind = nsorted["Name"].str.split(' ', expand=True)
new = pd.concat([nameind[0],nameind[1],nameind[2]],ignore_index=True)
new = new.dropna()
name_counts = Counter(new)
name_df = pd.DataFrame.from_dict(name_counts, orient='index').reset_index()
name_df = name_df.rename(columns={'index':'Name', 0 :'Count'})
name_df.to_csv("NameFrequency.csv",index=False)
print(name_df)



new = pd.unique(new)
#print(new)

sym_spell = SymSpell()
corpus_path = new
sym_spell.create_dictionary(corpus_path,encoding="utf-8")


#print(sym_spell.words)

# lookup suggestions for single-word input strings
input_term = "বক"  # misspelling of "members"
# max edit distance per lookup
# (max_edit_distance_lookup <= max_dictionary_edit_distance)
suggestions = sym_spell.lookup(input_term, Verbosity.CLOSEST,
                               max_edit_distance=2)
# display suggestion term, term frequency, and edit distance
for suggestion in suggestions:
    print(suggestion)

#nameind =nameind.sort_values(by =["0","1"]])

#print(new)
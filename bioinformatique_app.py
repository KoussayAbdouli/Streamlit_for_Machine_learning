import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


#####PAGE TITLE

image = Image.open('images/dna-logo.jpg')
st.image(image,use_column_width=True)

st.write(""" 
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of Query DNA!

""")


st.header('Enter DNA Sequence !')
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input" , sequence_input , height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

st.header('OUTPUT (DNA Nucleotide Count)')
### 1. Print Dictionnary

st.subheader('1. Print Dictionary')

def DNA_general_method(seq):
    d = {}
    for item in seq:
        if item in d:
            d[item] +=1
        else:
            d[item]=1
    return d
X = DNA_general_method(sequence)
X_label = list(X)
X_values = list(X.values())
X


#### Print Text
st.subheader('2. Print Text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')


### Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X , orient="index")
df.rename({0: 'count'} , axis ="columns" , inplace= True)
df.reset_index(inplace=True)
df = df.rename(columns= {"index" : 'Nucleotide'})
st.write(df)

### Display BarChart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='count'
)
p = p.properties(width = alt.Step(150))
st.write(p)



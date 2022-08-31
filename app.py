import streamlit as st
view = [100, 150,30]
st.write('# Youtube view')
st.write('## RAW')
st.write('## Bar-Chart')
view
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview
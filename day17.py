# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:36:58 2022

@author: Ricky
"""

import streamlit as st

st.title('st.secrets')

##The secret message was written in the .streamlit/secrets.toml file
st.write(st.secrets['message'])
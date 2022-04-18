# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:00:48 2022

@author: A549773
"""

import streamlit as st

st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
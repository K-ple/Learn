import requests
import streamlit as st
from PIL import Image

#st.set_option('deprecation.showfileUploaderEncoding', False)

st.title('Cat breed Classification API Test')

image = st.file_uploader('Choose an image')

if st.button('Prediction'):
    if image is not None:
        files = {'file': image.getvalue()}
        headers = {'Conetent-Type': 'multipart/form-data'}
        res = requests.post(f'http://127.0.0.1:8000/detect_labels', files=files)
        res = eval(res.text)
        bombay_prob = round(float(res['bombat']),2)
        burmese_prob = round(float(res['burmese']),2)
        st.write(f'{{Bombay: {bombay_prob}, Burmese: {burmese_prob}}}')
        st.image(image.getvalue(), width=240)
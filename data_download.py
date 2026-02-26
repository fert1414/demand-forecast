import os
import zipfile

os.makedirs('data', exist_ok=True)

data_zip_path = 'm5-forecasting-accuracy.zip'
extract_to = 'data/'

with zipfile.ZipFile(data_zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)
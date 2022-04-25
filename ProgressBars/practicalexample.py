"""Because what good is a progressbar if you can't have a practical use case"""
from tqdm import tqdm
import requests
import time

chunk_size = 1024      # bytes

url = 'https://researchtorevenue.files.wordpress.com/2015/04/1r41ai10801601_fong.pdf'

r = requests.get(url, stream=True)

total_size = int(r.headers['content-length'])  # need the overall size

with open('DummyPDF.pdf', 'wb') as f:
    for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size/chunk_size, unit= 'KB'):
        f.write(data)

    print('Download complete')

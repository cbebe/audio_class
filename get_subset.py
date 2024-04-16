from tqdm import tqdm
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

url = ('https://github.com/cbebe/audio_class/'
       'releases/download/data/google_speech_subset.zip')

with urlopen(url) as res:
    with ZipFile(BytesIO(res.read())) as zip_ref:
        for file in tqdm(iterable=zip_ref.namelist(),
                         total=len(zip_ref.namelist())):
            zip_ref.extract(member=file)

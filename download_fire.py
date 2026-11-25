from pathlib import Path
from urllib.request import Request, urlopen
url='https://upload.wikimedia.org/wikipedia/commons/9/9e/3_1_0_17_11933_1_1_32668_REICHSTAGSBRAND_Reichstag_Fire_German_Parliament_Berlin_1933-02-27_Burning_building._News_photo_February_1933._Narodowe_Archiwum_Cyfrowe_PDM.jpg'
p=Path(__file__).resolve().parent / "images" / "reichstag-fire.jpg"
p.parent.mkdir(exist_ok=True)
with urlopen(Request(url, headers={"User-Agent":"Educational visual essay (artwork download)"}), timeout=60) as r:
    data=r.read()
if not data.startswith(b"\xff\xd8"):
    raise ValueError("Response is not a JPEG")
p.write_bytes(data)
print("Saved", p)

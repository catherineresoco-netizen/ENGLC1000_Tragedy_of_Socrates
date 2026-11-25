import json, pathlib, urllib.request
root=pathlib.Path(__file__).resolve().parent
for a in json.loads((root/'artwork.json').read_text()):
    dest=root/a['local']; dest.parent.mkdir(exist_ok=True)
    try:
        req=urllib.request.Request(a['url'],headers={'User-Agent':'SocratesVisualEssay/1.0 (educational artwork download)'})
        with urllib.request.urlopen(req,timeout=60) as r: data=r.read()
        if not data.startswith(b'\xff\xd8'): raise ValueError('Not a JPEG')
        dest.write_bytes(data); print('Saved',dest.name)
    except Exception as e: print('Failed',dest.name,e,'Download manually:',a['source'])

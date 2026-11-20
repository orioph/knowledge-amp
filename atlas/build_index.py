# index.html = template.html + atlas.json + passages.json
import json,os
h=os.path.dirname(os.path.abspath(__file__))
t=open(h+'/template.html').read()
t=t.replace('__DATA__',open(h+'/atlas.json').read()).replace('__PASSAGES__',open(h+'/passages.json').read())
open(h+'/index.html','w').write(t); print('index.html',len(t))

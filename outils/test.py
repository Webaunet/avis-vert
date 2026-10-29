import sys,os,json
from playwright.sync_api import sync_playwright
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages=[p for p in sorted(os.listdir(R)) if p.endswith('.html')]
W=[360,414,768,980,1280,1920]+([821,981] if '--nav' in sys.argv else [])
bad=[]
JS="""()=>{const o=[],vw=document.documentElement.clientWidth;
if(document.documentElement.scrollWidth>vw)o.push('scrollX '+document.documentElement.scrollWidth);
document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e);if(s.display=='none'||s.visibility=='hidden')return;
const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());
if(t&&parseFloat(s.fontSize)<16)o.push('font '+parseFloat(s.fontSize)+' '+e.tagName+'.'+e.className+' '+e.textContent.trim().slice(0,20));
if((e.matches('a,button,input,select,textarea'))&&!e.closest('p,li:not(nav li)')||e.matches('nav a,.btn,button')){const r=e.getBoundingClientRect();if(r.width&&(r.height<44||r.width<44)&&getComputedStyle(e).display!='inline')o.push('cible '+Math.round(r.width)+'x'+Math.round(r.height)+' '+(e.textContent.trim().slice(0,15)||e.className))}
if(e.tagName=='IMG'){const r=e.getBoundingClientRect();if(e.naturalWidth&&r.width>e.naturalWidth+1)o.push('agrandie '+e.src.split('/').pop());}});
const h=document.querySelector('header').getBoundingClientRect(),m=document.querySelector('.logo').getBoundingClientRect(),n=document.querySelector('nav ul'),b=document.querySelector('.tel').getBoundingClientRect();
if(vw>980&&n){const q=n.getBoundingClientRect();if(m.right>q.left||q.right>b.left)o.push('nav chevauche');}
o.push('H1:'+document.querySelectorAll('h1').length);
o.push('secH:'+[...document.querySelectorAll('main>section')].map(s=>Math.round(s.getBoundingClientRect().height/innerHeight*100)).join(','));
o.push('footH:'+Math.round(document.querySelector('footer').getBoundingClientRect().height/innerHeight*100)+'%');
return o}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for pg in pages:
        for w in W:
            c=b.new_page(viewport={'width':w,'height':800 if w<900 else 900});c.goto('file://'+R+'/'+pg);c.wait_for_timeout(300)
            for x in c.evaluate(JS):
                if not x.startswith(('H1:1','secH','footH')) or '-v' in sys.argv: print(pg,w,x)
            c.close()
    # liens
    import re
    for pg in pages:
        for l in re.findall(r'(?:href|src)="([^"#:]+)"',open(R+'/'+pg,encoding='utf8').read()):
            if not os.path.exists(os.path.join(R,l)):print('LIEN MORT',pg,l)
    sz=[(f,os.path.getsize(R+'/images/'+f)//1024) for f in os.listdir(R+'/images')]
    print('images>250Ko:',[s for s in sz if s[1]>250])

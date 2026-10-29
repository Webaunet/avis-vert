import re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h=open(R+'/index.html',encoding='utf8').read()
head_a=h[:h.index('<title>')]
hdr=h[h.index('<header>'):h.index('<main>')]
ftr=h[h.index('</main>'):]
def page(f,title,desc,body):
    nav=hdr.replace(' aria-current="page"','').replace('href="%s">'%f,'href="%s" aria-current="page">'%f)
    t=head_a+'<title>%s</title>\n<meta name="description" content="%s">'%(title,desc)+h[h.index('\n<meta name="robots"'):h.index('<header>')]+nav+'<main>\n'+body+'\n'+ftr
    open(R+'/'+f,'w',encoding='utf8').write(t)
def band(t,p,cls=''):
    return '<section class="bloc vert" style="padding-bottom:72px"><div class="wrap" style="text-align:center"><h2>%s</h2><p style="max-width:34em;margin:14px auto 26px">%s</p><div class="btns" style="justify-content:center"><a class="btn ocre" href="tel:+33633543930">Appeler le 06 33 54 39 30</a><a class="btn clair" style="color:#fff;border-color:#fff" href="contact.html">Écrire à Avis Vert</a></div></div></section>'%(t,p)
# PRESTATIONS
b='''<section class="entete"><div class="wrap">
<div><span class="sur">Prestations</span><h1>Des conseils et un suivi pour chaque projet de jardin</h1>
<p>Particuliers, architectes paysagistes, entreprises d’espaces verts ou collectivités : Avis Vert accompagne vos projets avec un regard de professionnel du végétal.</p>
<div class="btns"><a class="btn ocre" href="tel:+33633543930">Appeler Avis Vert</a><a class="btn clair" href="contact.html">Demander conseil</a></div></div>
<div class="mosaique"><img src="images/conseil-jardin.jpg" width="1000" height="545" alt="Étude d’un projet de jardin sur une tablette, posée sur une table en bois"><img src="images/plantation.jpg" width="1000" height="546" alt="Jardinier plantant un arbuste dans un massif de vivaces"><img src="images/terrasse-bois.jpg" width="1000" height="545" alt="Pose d’une terrasse en bois devant une maison en pierre"></div>
</div></section>
<section class="bloc"><div class="wrap deux"><div><span class="sur">Pour les particuliers</span><h2>Réussir votre jardin, à votre rythme</h2>
<ul class="liste"><li><strong>Conseil et accompagnement</strong>Aménager votre jardin vous-même, avec l’appui d’un professionnel : le « faire soi-même » accompagné.</li><li><strong>Végétaux et fournitures</strong>Une recherche de végétaux et de fournitures de qualité professionnelle.</li><li><strong>Suivi technique et financier</strong>Un regard sur les projets paysagers que vous confiez à une entreprise.</li></ul></div>
<div class="photo-r"><img loading="lazy" src="images/muret-pierre.jpg" width="1000" height="545" alt="Maçon montant un muret en pierre avec escalier dans un jardin"></div></div></section>
<section class="bloc sable"><div class="wrap"><span class="sur">Pour les architectes paysagistes et maîtrises d’œuvre</span><h2>Un relais sur vos chantiers</h2>
<div class="tuiles"><div class="tuile"><h3>Suivi de travaux</h3><p>Une présence technique pour faire avancer le chantier selon le projet.</p></div><div class="tuile"><h3>Contrôle des réalisations</h3><p>Vérification du respect des exigences architecturales.</p></div><div class="tuile"><h3>Solutions techniques</h3><p>Conseils et propositions pour lever les points techniques du projet.</p></div></div></div></section>
<section class="bloc vert"><div class="wrap deux"><div><span class="sur" style="color:#fff">Pour les entreprises d’espaces verts et les collectivités</span><h2>Un renfort quand l’activité s’intensifie</h2></div>
<div class="tuiles" style="grid-template-columns:1fr;margin-top:0"><div class="tuile"><h3>Conduite de travaux</h3><p>Pour absorber les surcroîts d’activité.</p></div><div class="tuile"><h3>Apport de technicité</h3><p>Un savoir-faire de terrain mis au service de vos équipes.</p></div></div></div></section>
'''+band('Un projet à discuter ?','Dites-nous en quelques mots ce que vous avez en tête : Avis Vert vous répond.')
page('prestations.html','Prestations, Avis Vert à Beynes (78)','Prestations d’Avis Vert, à Beynes (78) : conseil et accompagnement, végétaux, suivi de travaux pour particuliers, architectes et entreprises d’espaces verts.',b)
# A PROPOS
ic='fill="none" stroke="#18220f" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
b='''<section class="entete"><div class="wrap">
<div><span class="sur">À propos</span><h1>Une vie autour du végétal</h1>
<p>Avis Vert met au service des jardins un parcours de terrain, de la pépinière à la direction de la production.</p>
<div class="btns"><a class="btn ocre" href="contact.html">Parler de mon projet</a></div></div>
<div class="photo-r"><img src="images/jardin-moderne.jpg" width="1000" height="%d" alt="Jardin récent avec pelouse, massifs et allée sinueuse devant une maison moderne"></div>
</div></section>
<section class="bloc"><div class="wrap deux" style="align-items:start"><div><span class="sur">Le parcours</span><h2>Du pépiniériste au directeur adjoint</h2>
<ul class="parcours"><li>Une formation de pépiniériste, puis la découverte du monde des jardins.</li><li>Plusieurs années de terrain, avec la conduite de travaux de projets majeurs et haut de gamme en région parisienne.</li><li>Le poste de directeur adjoint en charge de la production, dans une équipe d’une cinquantaine de collaborateurs.</li></ul></div>
<div class="carte-a"><h3>Ce que cela change pour vous</h3><ul><li>Les techniques paysagères maîtrisées sur le terrain</li><li>L’organisation des travaux : économie, qualité, aspects humains</li><li>L’amour du travail bien fait, que Avis Vert partage avec vous</li></ul></div></div></section>
<section class="bloc sable"><div class="wrap"><span class="sur">Valeurs fondatrices</span><h2>Le jardin, un lien avec le vivant</h2>
<div class="long">
<div class="sai pr"><svg viewBox="0 0 52 52" aria-hidden="true"><path d="M26 44V24M26 24c-8 0-12-5-12-12 8 0 12 4 12 12zm0 6c7 0 11-4 11-10-7 0-11 3-11 10z" %s/></svg><div><h3>Aimer le vivant</h3><p>Au-delà de l’esthétique, le jardin nous relie au vivant.</p></div></div>
<div class="sai et"><svg viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="9" %s/><path d="M26 6v6M26 40v6M6 26h6M40 26h6" %s/></svg><div><h3>Observer et comprendre</h3><p>Éveiller son regard sur les systèmes vivants du jardin, pour être acteur de son évolution.</p></div></div>
<div class="sai au"><svg viewBox="0 0 52 52" aria-hidden="true"><path d="M26 8c10 6 14 16 0 34C12 24 16 14 26 8zM26 18v26" %s/></svg><div><h3>Réfléchir à l’impact</h3><p>Avant tout aménagement : échanger sur les méthodes les moins intrusives et choisir les matériaux les mieux adaptés.</p></div></div>
<div class="sai hi"><svg viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="17" %s/><path d="M26 14v12l8 5" %s/></svg><div><h3>Prendre le temps long</h3><p>Le temps long et la résilience permettent au jardin de s’exprimer pleinement et d’y construire une relation sereine.</p></div></div>
</div></div></section>
'''%(round(1000*0.545),ic,ic,ic,ic,ic,ic)+band('Faisons connaissance','Un projet de jardin ou un chantier à suivre ? Appelez ou écrivez à Avis Vert.')
page('a-propos.html','À propos, Avis Vert à Beynes (78)','À propos d’Avis Vert, à Beynes (78) : un parcours de pépiniériste puis de directeur adjoint de production, et des valeurs tournées vers le vivant.',b)
# CONTACT
c=open('/home/claude/sq/contact.html',encoding='utf8').read()
form=c[c.index('<div class="formcarte">'):c.index('</div></section>\n</main>')]
form=form.replace('Commune du chantier','Commune du projet')
form=re.sub(r'<option>Conception.*?</select>','<option>Conseil pour aménager mon jardin</option><option>Végétaux et fournitures</option><option>Suivi de mon projet paysager</option><option>Suivi de travaux (architecte, maîtrise d’œuvre)</option><option>Conduite de travaux ou technicité (entreprise, collectivité)</option><option>Autre demande</option></select>',form,flags=re.S)
form=form.replace('+33610208133','+33633543930').replace('+33160819255','+33633543930')
b='''<section class="entete" style="padding-bottom:96px"><div class="wrap" style="grid-template-columns:1fr">
<div><span class="sur">Contact</span><h1>Parlons de votre projet</h1>
<p>Appelez ou remplissez le formulaire : en quelques lignes, Avis Vert peut comprendre votre besoin.</p></div></div></section>
<section class="bloc" style="padding-bottom:84px"><div class="wrap deux" style="align-items:start">
<div><span class="sur">Coordonnées</span><h2>Une question, un projet ?</h2><p style="margin-top:12px">Avis Vert est basé à Beynes (78).</p>
<div class="coord"><a href="tel:+33633543930">&#9990;<span><small>Téléphone</small>06 33 54 39 30</span></a></div></div>
'''+form+'</div></section>'
page('contact.html','Contact, Avis Vert à Beynes (78)','Contactez Avis Vert à Beynes (78) : appelez le 06 33 54 39 30 ou préparez votre demande avec le formulaire.',b)

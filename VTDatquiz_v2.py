import sys
import random

sources_of_error = []

class Question:
    def __init__(self, titlo, correctos, wrongos, source):
        self.titlo = titlo
        self.correctos = []
        for c in correctos:
            self.correctos.append((1,c))
        self.wrongos = []
        for w in wrongos:
            self.wrongos.append((0, w))
        self.source = source
    
    def perform_q(self):
        random.shuffle(self.correctos)
        random.shuffle(self.wrongos)
        qs = [self.correctos[0]] + self.wrongos[:3]
        random.shuffle(qs)
        print(self.titlo)
        numero = 1
        for q in qs:
            print(str(numero)+". "+q[1])
            numero += 1
        responso = sys.stdin.readline()
        if qs[int(responso)-1][0] == 1:
            print("correct")
            return 1
        else:
            print("wrong")
            print("Kilde: "+self.source)
            sources_of_error.append(self.source)
            return 0

qs = []
qs.append(Question("Hvad var det nye i det samarbejde, som i 2017 blev offentliggjort mellem KU og Microsoft",
["En privat virksomhed skulle placere et stort antal medarbejdere på universitetet"],
["Aftalen mellem virksomheden og universitetet var hemmelig",
"Microsoft fik indflydelse på formålet med projektet",
"Kvantecomputere kunne nu udføre parallelle beregninger"], 
"Zieler: Det store kvantegamble på KU"))

qs.append(Question("Hvilket af følgende er IKKE et kendetegn ved >>computational thinking<< som defineret af Jeannette M. Wing",
["Computational thinking indebærer at enhver problemstilling kan reduceres til et computerprogram"],
["Computational thinking bygger på koncepter, ikke programmer",
"Computational thinking er ikke kun for programmører",
"Computational thinking er for mennesker og ikke for computere",
"Computational thinking kombinerer matematik og ingeniørkunst"],
"Wing: Computational Thinking"))

cc_list = ["I commit to ensure the trustworthiness of research and be honest when reporting objectives, methods, data, analysis, results, conclusions, etc",
"I commit to To ensure the credibility of scientific reasoning.",
"I am accountable for the research carried out and accept responsibility for that research"]

tp_list = ["I commit to take responsibility for what I create",
"I commit to only help create things I would want my loved ones to use",
"I commit to pause to consider all consequences of my work, intended as well as unintended",
"I commit to invite and act on criticism, even when it is painful",
"I commit to ask for help when I am uncertain if my work serves my community",
"I commit to always put humans before business, and to stand up against pressure to do otherwise, even at my own risk.",
"I commit to never tolerate design for addiction, deception or control",
"I commit to help others understand and discuss the challenges of technology",
"I commit to participate in the democratic process of regulating technology, even though it is difficult",
"I commit to fight for democracy and human rights, and to improve the institutions that protect them",
"I commit to work towards a more inclusive and sustainable future for us all, following the United Nations global goals",
"I commit to always take care of what I start, and to fix what we break"]

qs.append(Question("Hvilket af følgende løfter indgår IKKE i The Tech Pledge",
cc_list,
tp_list,
"The Tech Pledge"))

def_of_as = ["Broad patterns of meaning and practice that can be engaged with empirically",
"Manifold consequences of a variety of human practices",
"Algorithms are enacted by practices which do not heed a strong distinction between technical and non-technical concerns",
"Unstable objects, culturally enacted by the practices people use to engage with them"]

def_of_in = ["A computer scientists definition of algorithms",
"Software engineers use algorithms to make sense of the world and their work",
"An algorithm is code that can be patented",
"Algorithms are discrete objects that may be located within cultural contexts",
"The relationship between algorithms and culture is like the relationship between a rock and the stream it is sitting in",
"Algorithms may shape culture and vice versa because the two are distinct"]

seaver_title = "Seaver: Algorithms as Culture"

qs.append(Question("Hvilken sætning er en definition på Nick Seavers >>Algorithms AS culture<<",
def_of_as, 
def_of_in, 
seaver_title
))

qs.append(Question("Hvilken sætning udtrykker Nick Seavers begreb >>Algorithms IN culture<<?",
def_of_in,
def_of_as,
seaver_title))

qs.append(Question("Seaver beskriver en case hvor brugerne af et datingsite ændrede adfærd for at optimere deres match, og algoritmen derfor måtte opdateres",
["Casen nævnes som et eksempel på Algorithms AS culture"],
["Casen nævnes som et eksempel på Algorithms IN culture"],
seaver_title))

qs.append(Question("Hvad kom først",
["DASK"],
["GIER", "DAIMI", "DIKU"],
"Kragh kapitel 1"))

newell_list = ["Computere forekommer ikke i naturen", 
"Computer er ikke et veldefineret eller konstant begreb",
"Genstandsfeltet for computer science er algoritmer, ikke computere",
"Computere er instrumenter, ikke fænomener",
"Computer science er gren af en anden videnskab, ikke en selvstændig videnskab",
"Computer science er ingeniørkunst, ikke videnskab"]

qs.append(Question("I 1967 oplistede Newell et. al. seks mulige indvendinger mod at betragte computer science som videnskab. Hvad er IKKE en af de 6 mulige indvendinger?",
["Data, ikke computere, er det vigtige"],
newell_list,
"Newell et al.: Computer Science"))

qs.append(Question("I 1966 skrev Peter Naur til ACM og foreslog at anerkende tre nye begreber. Udover >>Datalogy<<, hvad var de to andre begreber?",
["Datum&tics and datamaton"],
["Data science and datamaton",
"Programming psychology and data ethics",
"Data science and functional programming"],
"Naur: The Science of Datalogy"))

Naur_1985_title = "Naur: Programming as Theory Building"

qs.append(Question("Ifølge Naur 1985 er programmering: ",
["An activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand"],
["Production of a program "],
Naur_1985_title))

Naur_1985_list = ["Programmers brug afhang af specifik viden som kun de oprindelige udviklere havde. Denne viden omfattede mere end bare selve koden og havde reelt karakter af videnskabelig teori som defineret af Ryle"]

qs.append(Question("Naur skrev Programming as Theory Building i 1985 på baggrund af software-krisen. Hvad var problemet:",
Naur_1985_list,
["IT brugte mere og mere strøm",
"Sovjetunionen havde bedre computere",
"Der manglede uddannede softwareudviklere"],
Naur_1985_title))

miller_title = "Miller, Howe, Sonnenberg: Explainable AI: Beware of Inmates Running the Asylum"

qs.append(Question("Da Miller, Howe og Sonnenberg sagde at >>Inmates are running the asylum<< hvad mente de så?",
["AI-forskere brugte deres egne metoder til at forklare AI"],
["Kunstig intelligens ville snart tage magten",
"EU-Kommissionen fik gennem GDPR alt for stor indflydelse",
"Store virksomheder fik for stor indflydelse på grundforskning"],
miller_title))

miller_correct = ["Metoder fra samfundsvidenskab og behavioral science"]
miller_wrong = ["Metoder fra naturvidenskab",
"Metoder fra datalogi",
"Pædagogiske metoder",
"Metoder fra Institut for Naturvidenskabernes Didaktik på KU"]

qs.append(Question("Hvad nævner Miller, Howe og Sonnenberg som redskaber, der vil skabe gøre AI nemmere at forklare?",
miller_correct,
miller_wrong,
miller_title))

qs.append(Question("Hvorfor mener Miller, Howe og Sonnenberg ikke, at >>explainable AI<< kan udvikles af AI-forskere?",
["AI-forskere forstår allerede AI og kan derfor ikke afgøre, hvad der er en god forklaring på AI"],
["AI-forskere har en interesse i at hemmeligholde deres metoder",
"AI-forskere har for travlt i forvejen",
"AI-forskere forstår ikke de etiske og samfundsmæssige aspekter af AI"],
miller_title))

qs.append(Question("Da Millard-Ball skulle analysere samspillet mellem selvkørende biler og fodgængere inddrog han dette nye perspektiv:",
["Spilteori"],
miller_correct + miller_wrong,
"Millard-Ball: Pedestrians, Autonomous vehicles and cities"))

qs.append(Question("Limoncelli nævner 10 ting, som alle direktører bør vide om software. Hvad er ikke på listen?",
["Code should always be well documented", 
"Open-source software can be just as good as licensed software", 
"Software will run on ever more powerful computers", 
"Recruitment of programmers must be a priority"],
["Software is not magic",
"Software is never >>done<<",
"Software is a team effort, nobody can do it all",
"Design isnt how something looks it is how something works",
"Security is everyones responsibility",
"Feature size does not predict developer time",
"Greatness comes from thousands of small improvements",
"Technical debt is bad but unavoidable",
"Software doesnt run itself",
"Complex systems need DevOps to run well"],
"Limoncelli: 10 Things Executives Should Know About Software"
))

qs.append(Question("I artiklen af Troels Kølln fremhæves to mulige problemer ved den hemmelige aftale mellem KU og Microsoft. Hvilke?",
["Vi ved ikke hvad aftalen betyder for forskningsfriheden på KU eller hvor meget KU ender med at skulle betale"],
["Vi ved ikke hvad aftalen betyder for forskningsfriheden på KU eller om andre IT-virksomheder vil kunne sagsøge KU",
"Vi ved ikke om aftalen betyder, at Microsoft vil ansætte dygtige KU-forskere eller hvor meget KU ender med at skulle betale",
"Vi ved ikke om KU kan holde sin del af aftalen eller om aftalen vil være i strid med Danish Code of Conduct for Research Integrity"],
"Troels Kølln (2017). KU’s millionaftale med Microsoft er blevet mørkelagt."))

qs.append(Question("En forsker, kaldet >>fornyeren<< har fundet resultater, der strider mod anerkendte teorier på området. Hvad er i følge Kuhn det allerbedste, de etablerede forskere kan gøre?",
["De etablerede forskere skal besøge fornyeren, snakke med ham og iagttage ham og hans elever under arbejdet"],
["De etablerede forskere skal forsøge at gentage eksperimentet og måle resultatet med metoder, der allerede er anerkendte",
"De etablerede forskere må det samme forkaste deres anerkendte teorier på området",
"De etablerede forskere skal undersøge, om de nye resultater er nøjagtige, konsistente, bredt perspektiverende, enkle, dvs de bringer orden i ny viden, og givtige, det vil sige de resulterer i nye forudsigelser"],
"Thomas S. Kuhn (1995). Objektivitet, værdidom og valg af teori."))

kruse_title = "Christian Kruse, Pia Eiken og Peter Vestergaard (2017). Machine Learning Principles Can Improve Hip Fracture Prediction"

qs.append(Question("Kruse et.al, Eiken og Vestergaard nævner, at en model baseret på lineær regression af et polynomium af høj grad kan være en dårlig idé. Hvorfor?",
["Det kan være udtryk for overfit på træningsdata og generalisere dårligt til testdata"],
["Modellen vil bruge for meget cpu og memory i forhold til den ekstra performance, der opnås",
"Lineær regression anvendes sjældent på hoftedata",
"Selvom polynomiet har en høj, men endelig grad kan modellen udvise underfit, det vil sige at den ikke udnytter al tilgængelig information i træningsdata"],
kruse_title))

qs.append(Question("Hvad er ifølge Kruse et. al. fordele ved at bruge ML fremfor lineær regression til forudsigelse af risiko for hoftefraktur?",
["Forudsigelserne for den enkelte patient kan opdateres løbende hvis patientens situation ændrer sig"],
["ML er billigere end lineær regression",
"ML er bedre til at sikre privatlivshensyn",
"Hvor lineær regression er et relativt entydigt begreb findes der mange forskellige ML-modeller at vælge imellem"],
kruse_title))

qs.append(Question("Hvilket ord mangler i dette citat fra Jacobson et. al.: What is needed instead is a new software _______ built on the experience of software craftsmen, capturing their understanding in a foundation that can then be used to educate and support a new generation of practitioners.",
["engineering"],
["science",
"agility",
"culture"],
"Ivar Jacobson og Ed Seidewitz (dec. 2014). A New Software Engineering"))

mike_title = "Koby Mike og Orit Hazzan (2023). What Is Data Science?"

qs.append(Question("Mike et. al. skriver, at det er vanskeligt at definere data science fordi data science kan være mange ting. Hvad er IKKE en af de 6 mulige definitionstyper?",
["Data science as the development of ever more precise algorithms",
"Data science as culture",
"Data science in culture"],
["Data science as a science",
"Data science as a research paradigm",
"Data science as a research method",
"Data science as a discipline",
"Data science as a workflow",
"Data science as a profession"],
mike_title))

qs.append(Question("Mike et. al. opstiller et Venn-diagram over data science. Hvad er de fire overlappende cirkler, der har data science som fællesmængde",
["Computer science, machine learning, mathematics and statistics, application domain"],
["Honesty, transparency, accountability",
"Research planning and conduct, data management, publication and communication",
"Research integrity teaching, training, and supervision",
"Authorship, collaborative research, conflicts of interest"],
mike_title))

qs.append(Question("Gigerenzer beskriver en model, der kunne forudsige cancer med 0.1 true positive og 0.0001 false positives. Forekomsten af cancer i populationen var 0.0001. Hvorfor mener Gigerenzer ikke, at modellen var god?",
["Det var meget mere sandsynligt for en testperson at blive fejlagtigt diagnosticeret med cancer end at have cancer og få en korrekt diagnose"],
["0.1 true positive er for lidt, det er uetisk at lade 90 procent af alle syge gå uden diagnose",
"Det er uetisk at basere et så alvorligt emne som cancer på internetsøgehistorik",
"Modellen kunne opdage cancer tidligt men det førte ikke til flere helbredelser"],
"Gerd Gigerenzer (2017).Can search engine data predict pancreatic cancer?"))

qs.append(Question("Duhigg beskriver forsøg med rotter, der viser at vaner etableres ved tre skridt. Hvilke?",
["Stikord, vane, belønning"],
["Tese, antitese, syntese",
"Redegør, analyser, diskuter",
"Problem, løsning, konsekvens"],
"Charles Duhigg (16. feb. 2012). How Companies Learn Your Secrets"))

qs.append(Question("I 2013 argumenterede Denning for, at computer science kan betragtes som videnskab, begrundet i nogle kendetegn. Hvad var ikke et af disse kendetegn?",
["Computer science er en måde at tænke på", 
"Computer science vedrører ikke bare computere men også de data der behandles", 
"Computer science påvirker andre discipliner fremfor at andre discipliner påvirker computer science"],
["Computer science vedrører et generelt (pervasive) emne",
"Computer science omfatter både naturlige og kunstigt frembragte processer",
"Computer science har en kodificeret mængde viden",
"Computer science anvender eksperimenter",
"Computer science lægger vægt på at resultater skal kunne reproduceres",
"Computer science lægger vægt på at hypoteser skal kunne falsificeres",
"Computer science frembringer forudsigelser hvoraf nogle er overraskende"],
"Peter J. Denning (maj 2013). The Science in Computer Science"))

denning_2001_title = "Peter J. Denning (feb. 2001). The Profession of IT: Who Are We?"

qs.append(Question("I 2001 argumenterede Denning for, at computer science ikke bare var en disciplin men en profession. Hvad er IKKE en af de fire ting, som Denning mener kendetegner en profession?",
["Bold, verifiable conjectures"],
["A durable domain of human concerns",
"A codified body of principles conceptual knowledge",
"A codified body of practices embodied knowledge including competence",
"Standards for competence, ethics, and practice."],
denning_2001_title))

qs.append(Question("I 2001 mente Denning, at ud af de fire kriterier for at være en profession var der 2, som IT ikke opfyldte fuldt ud. Hvad er et af disse to kriterier?",
["A codified body of practices embodied knowledge including competence", 
"Standards for competence, ethics, and practice."],
["A durable domain of human concerns",
"A codified body of principles conceptual knowledge"],
denning_2001_title))

qs.append(Question("Da Denning i 2001 diskuterede, om IT kunne kaldes en profession, nævnte han følgende aktuelle kontekst:",
["Stadigt mere IT-innovation skete i brancher, der brugte IT (for eksempel sundheds- eller finanssektoren), fremfor i IT-firmaerne selv (IBM, Microsoft, andre)"],
["IT-firmaerne (IBM, Microsoft, andre) var de eneste, der kunne foretage IT-innovation, og derfor havde de et ansvar for andre brancher (for eksempel sundheds- eller finanssektoren)",
"År 2000-problemet havde vist sig overvurderet og derfor Turings og von Neumanns paradigmer endegyldigt rigtige",
"IT-boblen var bristet og derfor måtte IT acceptere at være en profession på linie med alle andre"],
denning_2001_title))

corbett_title = "Sam Corbett-Davies m.fl. (17. okt. 2016). A computer program used for bail and sentencing decisions was labeled biased against blacks"
angwin_title = "Julia Angwin m.fl. (23. maj 2016). Machine Bias"

qs.append(Question("Hvad er IKKE et af de eksempler, som Corbett-Davies og Angwin nævner som udtryk for at COMPASS-algoritmen kan anses for at være unfair?",
["Algoritmen benyttede race som en af sine feature-variable"],
["Målte man alene på den gruppe, der aldrig efterfølgende begik ny kriminalitet, havde algoritmen givet sorte en højere risikoscore end hvide",
"Der var flere eksempler hvor sorte med en høj risikoscore begik mindre alvorlig kriminalitet mens hvide med en lav risikoscore begik alvorlig kriminalitet",
"Algoritmen var ikke udviklet til at blive brugt til strafudmåling, men kun til efterfølgende sagsbehandling herunder prøveløsladelse"],
corbett_title +" "+angwin_title))

qs.append(Question("Hvilket er et udtryk for, at COMPASS-algoritmen kan anses for at være fair?",
["For en given risikoscore viser sorte og hvide sig at have samme faktiske tendens til at begå ny krimialitet"],
["Race indgår ikke som en af algoritmens feature-variable",
"Den er et forsøg på at løse generelle problemer i det amerikanske retsvæsen",
"Den er baseret på faktiske oplysninger såsom tidligere anholdelser og tidligere domme, ikke subjektive parametre som spørgeskemaer og terapisamtaler"],
corbett_title + angwin_title))

kragh_1_title = "Kragh og Johansen kap. 1"

qs.append(Question("Hvilket begreb indgår IKKE i CUDOS?",
["Constructive criticism",
"University",
"Development",
"Open Science"],
["Communalism", 
"Universality", 
"Disinterestedness", 
"Organized Scepticism"],
kragh_1_title))

qs.append(Question("Hvilket begreb indgår ikke i PLACE",
["Precise",
"Liberty",
"All-round",
"Communalism",
"Expectation"],
["Proprietary",
"Local",
"Authoritarian",
"Commissioned",
"Expert"],
kragh_1_title))

qs.append(Question("Hvad forstås ved begreberne Authoritarian og Expert i PLACE?",
["Forskeren er en ekspert, der ledes af en chef på universitetet"],
["Formålet med forskningen er at fremme demokrati, og universiteternes demokratiske tradition gør forskeren til ekspert i dette",
"Forskeren er som ekspert en autoritet på sit område og har derfor et særligt ansvar",
"Forskeren skal prøve at blive så dygtig til sit felt som overhovedet muligt"],
kragh_1_title))

qs.append(Question("Hvad indebærer begreberne Local og Commissioned i PLACE?",
["Forskningen rettes mod et afgrænset formål og den er bestilt at en ekstern aktør, enten staten eller en virksomhed"],
["Det er de enkelte universiteter, der lokalt bestemmer hvem de ansætter",
"Det enkelte land må lokalt bestemme, hvilken forskning staten skal bestille",
"Det enkelte land må lokalt bestemme, hvilke forskningskommissioner, der skal nedsættes"],
kragh_1_title))

qs.append(Question("Hvad indebar universitetsloven fra 2003?",
["Der indførtes et ledelsesstyret universitet med mulighed for pålægge forskere specifikke opgaver"],
["Der kom fælles regler for god videnskabelig praksis på alle universiteter",
"Danmark skulle bruge to procent af BNP på forskning",
"Lovens centrale princip er videnskabens autonomi og det akademiske samfunds evne til at regulerede sig selv"],
kragh_1_title))

qs.append(Question("Din ven siger til dig >>Jeg ønsker deduktivt at afprøve en teori om, at solen står op kl. 4.25 i morgen<<. Du vil gerne påpege induktionsproblemet i din vens udsagn. Hvad siger du?",
["Den teori er baseret på tidligere erfaringer, og det du laver er derfor induktion, ikke deduktion"],
["Det bliver formentlig bekræftet, og det skaber ikke ny viden at bekræfte en eksisterende teori",
"Du kan ALDRIG bevise dette, enhver observation er foreløbig",
"Du kan ikke lave interesseløs observation af data. Solen står kun op på et bestemt tidspunkt, fordi du er dig og bor i Danmark",
"De fleste videnskabsfolk forstår i dag begrebet >>solopgang<< på en bestemt måde, og kun hvis du anvender du den definition giver dine observationer mening"],
kragh_1_title))

metode_dict = {"Popper": "Poppers hypotetisk-deduktive metode", 
"Wiener": "Wiener-skolens logiske positivisme", 
"Kuhn": "Kuhns teori om videnskabelige revolutioner", 
"Lakatos": "En hård kerne af et forskningsprogram som beskrevet af Lakatos"}

open_spg = "Din ven fortæller dig, at han arbejder med sin bacheloropgave på følgende måde: "
wiener_spg =  "Jeg vil gerne have facts på bordet, så jeg afleverer nogle empiriske resultater, så er der ikke så meget at diskutere."
close_spg = " Din vens arbejdsform er mest udtryk for:"

qs.append(Question(open_spg+wiener_spg+close_spg,
[metode_dict["Wiener"]],
[metode_dict["Popper"],
metode_dict["Kuhn"],
metode_dict["Lakatos"]],
kragh_1_title))

popper_spg = " Få en god idé, opstil en teori, udfør forsøg, hvis teorien afkræftes opstil da en ny teori."
qs.append(Question(open_spg + popper_spg+close_spg,
[metode_dict["Popper"]],
[metode_dict["Wiener"],
metode_dict["Kuhn"],
metode_dict["Lakatos"]],
kragh_1_title))

kuhn_spg = "AI ændrer ALT, jeg kan ikke bruge noget af det jeg har lært på DIKU. Jeg starter derfor med at beskrive en række eksempler på, at AI-modeller ikke er normale computermodeller, og diskuterer hvorfor datalogien må laves om."
qs.append(Question(open_spg + kuhn_spg + close_spg,
[metode_dict["Kuhn"]],
[metode_dict["Popper"],
metode_dict["Wiener"],
metode_dict["Lakatos"]],
kragh_1_title))

lakatos_spg = "Der er nogle grundlæggende ting jeg har lært på DIKU som jeg ikke vil stille spørgsmålstegn ved, men andre ting i forbindelse med implementering vil jeg undersøge."
qs.append(Question(open_spg+lakatos_spg+close_spg,
[metode_dict["Lakatos"]],
[metode_dict["Wiener"],
metode_dict["Kuhn"],
metode_dict["Popper"]],
kragh_1_title))

qs.append(Question(open_spg+" Mine resultater er faktisk revolutionerende, men jeg ved ikke om jeg har afkræftet teorien eller om måleapparatet bare er i stykker"+close_spg,
["Duhem-Quine tesen"],
[metode_dict["Wiener"],
metode_dict["Popper"],
metode_dict["Kuhn"],
metode_dict["Lakatos"]],
kragh_1_title))

ontologi_def = "Læren om det værende, bl.a. læren om genstandsfeltet for vores erkendelse"
epistemologi_def = "Læren om, hvordan vi opnår erkendelse og hvilken form, den erkendelse har"
real_def = "Videnskab, der handler om en ekstern virkelighed, som kan være fysisk eller social"
formal_def = "Videnskab, der handler om formelle systemer postuleret af os"

qs.append(Question("Hvad betyder ontologi?",
[ontologi_def],
[epistemologi_def,
real_def,
formal_def],
kragh_1_title))

qs.append(Question("Hvad betyder epistemologi?",
[epistemologi_def],
[ontologi_def,
real_def,
formal_def],
kragh_1_title))

score = 0
n = 0

random.shuffle(qs)

print("Velkommen til VT-Dat multiple choice.")
print()

for q in qs:
    print(str(score)+" ud af "+str(n))
    score += q.perform_q()
    n += 1
    print()

sources_of_error = list(set(sources_of_error))

print("Din score er "+str(score)+ " ud af "+str(len(qs)))
if len(sources_of_error)>0:
    print("Your errors relate to the following sources:")
    for s in sources_of_error:
        print(s)


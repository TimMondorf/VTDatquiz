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

score = 0
n = 0

random.shuffle(qs)

print("Velkommen til VT-Dat multiple choice.\n")

for q in qs:
    print(str(score)+" ud af "+str(n))
    score += q.perform_q()
    n += 1
    print()

print("Din score er "+str(score)+ " ud af "+str(len(qs)))
if len(sources_of_error)>0:
    print("Your errors relate to the following sources:")
    for s in sources_of_error:
        print(s)


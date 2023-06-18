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
        while True:
            responso = sys.stdin.readline()
            if responso in ["0\n", "1\n", "2\n", "3\n", "4\n"]: 
                break
            else:
                print("Input må kun være 1, 2, 3 eller 4")
        if int(responso) == 0:
            quit()
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
["Datamatics and datamaton"],
["Data science and datamaton",
"Programming psychology and data ethics",
"Data science and functional programming"],
"Naur: The Science of Datalogy"))

Naur_1985_title = "Naur: Programming as Theory Building"

qs.append(Question("Ifølge Naur 1985 er programmering: ",
["An activity by which the programmers form or achieve a certain kind of insight, a theory, of the matters at hand"],
["Production of a program "],
Naur_1985_title))

Naur_1985_list = ["Programmers brug afhang af specifik viden som kun de oprindelige udviklere havde. Denne viden omfattede mere end bare selve koden og havde reelt karakter af videnskabelig teori"]

qs.append(Question("Naur skrev Programming as Theory Building i 1985 på baggrund af, at række store software-projekter var løbet ind i problemer. Hvori bestod problemerne?",
Naur_1985_list,
["IT brugte mere og mere strøm",
"Det militære kapløb med Sovjetunionen krævede stadigt bedre software",
"Der manglede uddannede softwareudviklere"],
Naur_1985_title))

miller_title = "Miller, Howe, Sonnenberg: Explainable AI: Beware of Inmates Running the Asylum"

qs.append(Question("Da Miller, Howe og Sonnenberg sagde at >>Inmates are running the asylum<< hvad mente de så?",
["AI-forskere brugte deres egne metoder til at forklare AI"],
["Kunstig intelligens ville snart tage magten",
"EU-Kommissionen fik gennem GDPR alt for stor indflydelse",
"Store virksomheder havde for stor indflydelse på grundforskningen"],
miller_title))

miller_correct = ["Metoder fra samfundsvidenskab og behavioral science"]
miller_wrong = ["Metoder fra naturvidenskab",
"Metoder fra datalogi",
"Pædagogiske metoder",
"Metoder fra Institut for Naturvidenskabernes Didaktik på KU"]

qs.append(Question("Hvad nævner Miller, Howe og Sonnenberg som redskaber, der vil gøre AI nemmere at forklare?",
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
"De etablerede forskere må med det samme forkaste deres anerkendte teorier på området",
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

qs.append(Question("Mike et. al. opstiller et Venn-diagram over data science. Hvad er de overlappende cirkler i diagrammet, der har data science som fællesmængde",
["Computer science, machine learning, mathematics and statistics, application domain"],
["Honesty, transparency, accountability",
"Research planning and conduct, data management, publication and communication",
"Research integrity teaching, training, and supervision",
"Authorship, collaborative research, conflicts of interest"],
mike_title))

qs.append(Question("Gigerenzer beskriver en model, der kunne forudsige cancer med andelen 0.1 true positive og 0.0001 false positives. Frekvensen af cancer i populationen var 0.0001. Hvorfor mener Gigerenzer ikke, at modellen var god?",
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

qs.append(Question("I 2013 argumenterede Denning for, at computer science kunne betragtes som videnskab fordi computer science havde en række af videnskabens kendetegn. Hvad er IKKE et af de kendetegn, som Denning nævner?",
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
"A codified body of principles and conceptual knowledge",
"A codified body of practices embodied knowledge including competence",
"Standards for competence, ethics, and practice."],
denning_2001_title))

qs.append(Question("I 2001 mente Denning, at ud af de fire kriterier for at være en profession var der 2, som IT ikke opfyldte fuldt ud. Hvad er et af disse to kriterier?",
["A codified body of practices embodied knowledge including competence", 
"Standards for competence, ethics, and practice."],
["A durable domain of human concerns",
"A codified body of principles and conceptual knowledge"],
denning_2001_title))

qs.append(Question("Da Denning i 2001 diskuterede, om IT kunne kaldes en profession, nævnte han følgende aktuelle kontekst:",
["Stadigt mere IT-innovation skete i brancher, der brugte IT (for eksempel sundheds- eller finanssektoren), fremfor i IT-firmaerne selv (IBM, Microsoft, andre)"],
["IT-firmaerne (IBM, Microsoft, andre) var de eneste, der kunne foretage IT-innovation, og derfor havde de et ansvar for andre brancher (for eksempel sundheds- eller finanssektoren)",
"År 2000-problemet havde vist sig overvurderet og derfor var Turings og von Neumanns paradigmer nu endegyldigt rigtige",
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

qs.append(Question("Hvad er i Corbett-Davies det primære argument for, at COMPASS-algoritmen kan anses for at være fair?",
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
"Lovens centrale princip er videnskabens autonomi og det akademiske samfunds evne til at regulere sig selv",
"Byggeriet af Niels Bohr-bygningen på Jagtvej blev sat i gang"],
kragh_1_title))

qs.append(Question("Din ven siger til dig >>Jeg ønsker deduktivt at afprøve en teori om, at solen står op kl. 4.25 i morgen<<. Du vil gerne påpege induktionsproblemet i din vens udsagn. Hvad siger du?",
["Den teori er baseret på tidligere erfaringer, og det du laver er derfor induktion, ikke deduktion"],
["Det bliver formentlig bekræftet, og det skaber ikke ny viden at bekræfte en eksisterende teori",
"Du kan ALDRIG bevise dette, enhver observation er foreløbig",
"Du kan ikke lave interesseløs observation af data. Solen står kun op på et bestemt tidspunkt, fordi du er dig og bor i Danmark",
"De fleste videnskabsfolk forstår i dag begrebet >>solopgang<< på en bestemt måde, og kun hvis du anvender den definition giver dine observationer mening"],
kragh_1_title))

metode_dict = {"Popper": "Poppers hypotetisk-deduktive metode", 
"Wiener": "Wiener-skolens logiske positivisme", 
"Kuhn": "Kuhns teori om videnskabelige revolutioner", 
"Lakatos": "Et forskningsprogram med en hård kerne og et beskyttende bælte som beskrevet af Lakatos",
"Duhem-Quine": "Duhem-Quine tesen om, at enhver teori gør brug af et netværk af andre hypoteser"}

open_spg = "Din ven fortæller dig, at han arbejder med sin bacheloropgave på følgende måde: "
wiener_spg =  "Jeg vil gerne have facts på bordet, så jeg afleverer nogle empiriske resultater, så er der ikke så meget at diskutere."
close_spg = " Din vens arbejdsform er mest udtryk for:"

qs.append(Question(open_spg+wiener_spg+close_spg,
[metode_dict["Wiener"]],
[metode_dict["Popper"],
metode_dict["Kuhn"],
metode_dict["Lakatos"],
metode_dict["Duhem-Quine"]],
kragh_1_title))

popper_spg = " Få en god idé, opstil en teori, udfør forsøg, hvis teorien afkræftes opstil da en ny teori."
qs.append(Question(open_spg + popper_spg+close_spg,
[metode_dict["Popper"]],
[metode_dict["Wiener"],
metode_dict["Kuhn"],
metode_dict["Lakatos"],
metode_dict["Duhem-Quine"]],
kragh_1_title))

kuhn_spg = "AI ændrer ALT, jeg kan ikke bruge noget af det jeg har lært på DIKU. Jeg starter derfor med at beskrive en række eksempler på, at AI-modeller ikke er normale computermodeller, og diskuterer hvorfor datalogien må laves om."
qs.append(Question(open_spg + kuhn_spg + close_spg,
[metode_dict["Kuhn"]],
[metode_dict["Popper"],
metode_dict["Wiener"],
metode_dict["Lakatos"],
metode_dict["Duhem-Quine"]],
kragh_1_title))

lakatos_spg = "Der er nogle grundlæggende ting jeg har lært på DIKU som jeg ikke vil stille spørgsmålstegn ved, men andre ting i forbindelse med implementering vil jeg undersøge."
qs.append(Question(open_spg+lakatos_spg+close_spg,
[metode_dict["Lakatos"]],
[metode_dict["Wiener"],
metode_dict["Kuhn"],
metode_dict["Popper"],
metode_dict["Duhem-Quine"]],
kragh_1_title))

test_q = Question(open_spg+lakatos_spg+close_spg,
[metode_dict["Lakatos"]],
[metode_dict["Wiener"],
metode_dict["Kuhn"],
metode_dict["Popper"],
metode_dict["Duhem-Quine"]],
kragh_1_title)

##test_q.perform_q()

qs.append(Question(open_spg+" Mine resultater er faktisk revolutionerende, men jeg ved ikke om jeg har afkræftet teorien eller om måleapparatet bare er i stykker."+close_spg,
[metode_dict["Duhem-Quine"]],
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

formal_list = ["Matematik",
"Grammatik",
"Logik"]

real_list = ["Sociologi", 
"Biokemi",
"Medievidenskab",
"Geologi",
"Fonetik"]

qs.append(Question("Hvilken af disse er en formalvidenskab?",
formal_list,
real_list,
kragh_1_title))

qs.append(Question("Hvilken af disse er en realvidenskab",
real_list,
formal_list,
kragh_1_title))

helge_kragh_list = ["Videnskabelig viden er offentlig",
"Videnskabelig viden er fejlbarlig",
"Videnskabelig viden er korrigerbar",
"Videnskabelig viden er testbar"]

qs.append(Question("Hvilken en af disse indgår i Helge Kraghs definition af videnskabelig viden?",
helge_kragh_list,
["Videnskabelig viden er proprietær",
"Videnskabelig viden har karakter af ekspertviden",
"Videnskabelig viden er viden, der løser et konkret problem",
"Videnskabelig viden er viden, der er bestilt af staten eller en virksomhed"],
kragh_1_title))

qs.append(Question("Hvilken en af disse indgår i Helge Kraghs definition af videnskabelig viden men ikke i hans brutto-liste over mulige definitioner på videnskab?",
helge_kragh_list,
["Videnskabelig viden repræsenterer er en forfinelse af dagliglivets erfaringer",
"Videnskabelig viden er teoretisk, i modsætning til praktisk viden",
"Videnskab resulterer i udsagn, der er matematisk formulerede og hævdes at være universelt gyldige",
"Videnskabelig viden er frembragt ved ved bestemte metoder og procedurer, fx eksperimenter",
"Videnskabelig viden er objektiv og baseret på sociale mekanismer til sikring af dens offentlige karakter",
"Videnskab resulterer i offentlig tilgængelig viden i form af bøger og artikler",
"Videnskab er, hvad videnskabsmænd laver"],
kragh_1_title))

kragh_2_title = "Kragh og Johansen kap. 2"

turing_list = ["Maskinen kan skrive et symbol i et tomt kvadrat",
"Maskinen kan slette et symbol i et kvadrat",
"Maskinen kan ændre det kvadrat, der scannes, men kun ved at flytte en plads til højre eller venstre",
"Maskinen har endeligt mange tilstande og kan ændre, hvilken een af disse tilstande, den befinder sig i"]

neumann_list = ["Maskinen har hukommelse",
"Maskinen har en kontrolenhed",
"Maskinen har en aritmetikenhed",
"Maskinen modtager input",
"Maskinen afgiver output"]

qs.append(Question("Hvilken en af disse ting kendetegner IKKE Turing-paradigmet",
neumann_list,
turing_list,
kragh_2_title))

qs.append(Question("Hvilken en af disse ting kendetegner IKKE von Neumann-paradigmet",
turing_list,
neumann_list,
kragh_2_title))

qs.append(Question("Kragh og Johansen starter med fire kandidater til datalogiske paradigmer. Hvad er IKKE en af de fire?",
["Computer science som profession baseret på fælles normer og værdier",
"Diskret matematik",
"Logik"],
["Centrale antagelser om computerens arkitektur",
"Centrale antagelser om beregningers kompleksitet",
"Teorier om metoder for softwareudvikling",
"Teorier om programmeringssprog"],
kragh_2_title))

qs.append(Question("Hvad indebærer den lineære model, også kaldet samlebåndsmodellen",
["Forskning er en automatisk og fremadskridende proces, hvor grundforskning omsættes til faktiske produkter i markedet"],
["Enhver funktion kan lineært approximeres i et strengt positivt interval",
"Grundforskning blev sidestillet med industriel produktion og skulle leve op til fastsatte produktionsmål",
"Entreprenørskab er vigtigere end akademisk arbejde"],
kragh_2_title))

qs.append(Question("Din ven er forsker på KU og er blevet træt af PLACE. Han siger >>Bare vi dog kunne komme tilbage til efterkrigstiden, hvor folk som Vannevar Bush fastslog, at hvis man lod os forskere arbejde i fred, så skulle der nok komme samfundsnyttig innovation ud af det<<. Hvad skal du IKKE sige til ham?",
["Bare tag til USA, der gælder Bushs tanker stadigvæk"],
["Partnerskaber mellem universiteter og virksomheder betyder, at der samlet kommer flere penge til KU, end der ellers ville gøre",
"Bushs tanker relaterede sig til industrisamfundet, sammenhængen mellem grundforskning og produktinnovation betragtes i dag som mere uforudsigelig",
"Der er også i dag plads til fri forskning på højt niveau, KU har for eksempel lige fået en Nobelpris",
"Bush så teknologi som artefakter, altså separate >>ting<<, og idag ved vi, at teknologi kun virker hvis den indgår i et teknologisk system som beskrevet af Hughes. Derfor er PLACE nødvendigt"],
kragh_2_title))

qs.append(Question("Følgende spørgsmål er lidt svært. De fire svarmuligheder er henholdsvis Hughes definition på et teknologisk system, citat fra Bushs rapport om den lineære model, Michael Porters definition på en virksomheds værdikæde og konsulentvirksomheden Gartners definition på et økosystem. Du skal vælge den sætning, der udtrykker Hughes definition på et teknologisk system:",
["Messy, complex, problem-solving components .. that are socially constructed and society shaping"],
["Nye produkter, nye industrier og flere jobs kræver vedvarende tilføjelser til vores viden om naturens love og anvendelsen af denne viden til praktiske formål. Denne essentielle nye viden kan kun opnås gennem videnskabelig grundforskning.",
"A set of activities that an organization carries out to create value for its customers",
"An interdependent group of actors (enterprises, people, things) sharing standardized digital platforms to achieve a mutually beneficial purpose"],
kragh_2_title))

qs.append(Question("Hvad forstås ved experimenters regress?",
["Ethvert eksperiment tester ikke en enkelt hypotese men et netværk af hypoteser"],
["Ethvert eksperiment bygger i sidste ende på matematiske antagelser og da matematik er en formalvidenskab har eksperimentet ikke realvidenskabelig gyldighed",
"Jo flere gange eksperimentet gentages, jo tættere kan den estimerede værdi komme på den sande værdi",
"Gennemsnittet af et stort antal parametre, der følger hver deres uafhængige sandsynlighedsfordeling, men som ikke nødvendigvis er identisk fordelt, vil være normalfordelt"],
kragh_2_title))

qs.append(Question("Hvilken sætning refererer IKKE til den epistemologiske dimension af forskellen mellem grundforskning og anvendelsesorienteret forskning som defineret i Kragh og Johansen 2.1?",
["Grundforskning kommer før anvendt forskning",
"Grundforskning er en forudsætning for anvendt forskning",
"Grundforskere og anvendelsesorienterede forskere har forskellige motiver for deres arbejde"],
["Grundforskning og anvendt forskning kan gøre forskellige former for erkendelser",
"Grundforskningen svarer på >>Hvad<< og >>Hvorfor<<, den anvendelsesorienterede forskning svarer på >>Hvordan<<",
"Grundforskning skal være testbar og korrigerbar, anvendelsesorienteret forskning skal være anvendelig i markedet",
"Grundforskning er sandhedssøgende, anvendelsesorienteret forskning er pragmatisk"],
kragh_2_title))

tek_sys_list = ["Fysiske artefakter som apparater og installationer",
"Organisationer som firmaer, forsyningssystemer og finansieringskilder",
"Videnskabelige elementer som artikler med viden og universiteter med forskere og studerende",
"Juridiske og regulerende komponenter, som love og traktater",
"Naturressourcer"]

disc_mat_list = ["Symbolske generaliseringer“, dvs. basale udsagn, som ligner naturlove, men egentlig (også) er definitioner",
"Metafysiske elementer i form af delte overbevisninger, herunder metaforer og analogier",
"Værdier",
"Eksemplarer i form af problemer, løsninger, klassiske værker, lærebøger"]

qs.append(Question("Hvad indgår IKKE i et teknologisk system som beskrevet af Hughes?",
disc_mat_list,
tek_sys_list,
kragh_2_title))

qs.append(Question("Hvad indgår IKKE i et paradigmes disciplinære matrix som defineret af Kuhn?",
tek_sys_list,
disc_mat_list,
kragh_2_title))

qs.append(Question("Du prøver at retfærdiggøre overfor dig selv, at du bruger for meget tid på at arrangere hyttetur. Hvilken undskyldning er mindst dårlig?",
["Hytteturen er et eksemplar, der indgår i den disciplinære matrix, og som socialiserer nye studerende socialiseres til datalogiens paradigme",
"Hytteturen indgår i datalogiens teknologisystem, da der kommer en virksomhed og holder oplæg"],
["Staten er vogter af moralen, og hytteture er ikke ulovlige",
"Hytteture er udtryk for grundforskning og vil derfor med sikkerhed føre til relevant innovation",
"Hvis ikke jeg gør det vil andre tage min plads",
"De studerende vælger selv at deltage, jeg gør det bare muligt"],
kragh_2_title))

formal_arg_list = ["Diskret matematik betyder meget i datalogi, og matematik er en formalvidenskab",
"Nuller og ettaller i en computers hukommelse har i sidste ende kun den betydning, vi tillægger dem",
"Hvorvidt en algoritme afvikles korrekt afhænger af det definerede formål med algoritmen"]

real_arg_list = ["Det kan testes i virkeligheden, hvorvidt en algoritme har den teoretisk forventede afviklingstid",
"Computerprogrammer anvender som input store mængder data, der hentes i virkeligheden",
"Computere og programmer udvikles på grundlag af menneskers erfaring med at bruge disse"]

from_real_intro = "Det er ifølge Kragh og Johansen ikke entydigt, om datalogi er en formalvidenskab eller en realvidenskab. Hvilket af nedenstående er et argument for, at datalogi er en "

qs.append(Question(from_real_intro+"formalvidenskab?",
formal_arg_list,
real_arg_list,
kragh_2_title))

qs.append(Question(from_real_intro+"realvidenskab?",
real_arg_list,
formal_arg_list,
kragh_2_title))

qs.append(Question("Da von Neumann i 1945 skrev sin rapport om EDVAC-computeren var det nye:",
["Computerens hukommelse rummede ikke bare data, men også instruktioner"],
["Det var første gang Moores lov blev iagttaget i praksis",
"EDVAC havde et endeligt antal tilstande men kunne beregne alt, hvad der kunne siges at være beregneligt",
"EDVAC var udviklet til millitært brug men skulle nu anvendes af private virksomheder"],
kragh_2_title))

kragh_3_title = kragh_2_title.replace("2","3")

qs.append(Question("Hvilken sætning refererer til Bell-LaPadula-modellen?",
["No write down, no read up"],
["No write up, no read down",
"Participants are free to use the information received, but neither the identity nor the affiliation of the speaker(s), nor that of any other participant, may be revealed",
"Express the meaning of (something written or spoken) using different words, especially to achieve greater clarity"],
kragh_3_title))

qs.append(Question("En IT-medarbejder i forsvaret er sikkerhedsgodkendt til >>HEMMELIGT<< og koder et program, der klassificeres >>YDERST HEMMELIGT<<. Er Bell-LaPadula-modellen overholdt?",
["Ja"],
["Nej"],
kragh_3_title))

qs.append(Question("Hvad er IKKE et eksempel på en covert channel, som Bell LaPadula-modellen gerne vil forebygge?",
["En spion skaffer sig en hemmelig kommunikationskanal ind til det danske forsvars netværk",
"Kvantecomputere bryder kryptering ved at beregne et stort antal primtal",
"En fremmed efterretningstjeneste aflytter en radiokanal, der anvendes til fortroligt materiale"],
["Den samme printer kan udskrive både fortrolige og ikke-fortrolige dokumenter",
"Den samme computer afvikler både fortrolige og ikke-fortrolige programmer",
"Det samme netværksudstyr transmitterer både fortrolig og ikke-fortrolig kommunikation"],
kragh_3_title))

testq3 = Question("Hvad er IKKE et eksempel på en covert channel, som Bell LaPadula-modellen gerne vil forebygge?",
["En spion skaffer sig en hemmelig kommunikationskanal ind til det danske forsvars netværk",
"Kvantecomputere bryder kryptering ved at beregne et stort antal primtal",
"En fremmed efterretningstjeneste aflytter en radiokanal, der anvendes til fortroligt materiale"],
["Den samme printer kan udskrive både fortrolige og ikke-fortrolige dokumenter",
"Den samme computer afvikler både fortrolige og ikke-fortrolige programmer",
"Det samme netværksudstyr transmitterer både fortrolig og ikke-fortrolig kommunikation"],
kragh_3_title)

##testq3.perform_q()

qs.append(Question("Kragh og Johansen kap. 3.4 diskuterer hvad det vil sige at bevise, at computerkode er korrekt. Hvad er det bedste udtryk for dette?",
["Et niveau af software-stakken er en korrekt implementaton af en specifikation på et højere niveau"],
["Alle tænkelige use cases er blevet testet uden at computeren gik ned, og hver gang returnerede algoritmen det korrekte resultat",
"Koden kan afvikles på den tid, der må forventes ud fra algoritmens teoretiske afviklingstid som udtrykt i store O-notation",
"Ifølge Turing-modellen har computeren et endeligt antal tilstande, og hvis alle disse tilstande er blevet afprøvet med succes, så er koden korrekt",
"Koden placeres i et adversarial network, hvor en AI prøver at lære, hvordan den får koden til at give en fejlmeddelelse. Sker dette ikke, konkluderes det, at koden er korrekt"],
kragh_3_title))

qs.append(Question("Hvilket begreb indgår IKKE i Hills definition af en algoritme?",
["En algoritme er kode",
"En algoritme er et diskret objekt i en kulturel kontekst",
"En algoritme er adskilt fra kulturen",
"En algoritme er en manifold konsekvens af en menneskelig praksis. (Hvis B er en manifold konsekvens af A så udtrykker B noget af A men i færre dimensioner)"],
["En algoritme er en endelig kontrolstruktur", 
"En algoritme er en abstrakt kontrolstruktur", 
"En algoritme er en effektiv kontrolstruktur",
"En algoritme er en sammensat kontrolstruktur",
"En algoritme er givet imperativt",
"En algoritme opnår et givet formål under givne forhold",],
kragh_3_title))

qs.append(Question("Er bubble sort en effektiv algoritme ifølge Hills definition?",
["Ja, den tager usorterede data som input og har ikke brug for yderligere brugerinput for at kunne returnere sorterede data som output"],
["Nej, den kører meget langsommere end de bedst kendte sorteringsalgoritmer og er derfor ikke effektiv"],
kragh_3_title))

qs.append(Question("Hvad er modsætningen til analytisk?",
["Syntetisk"],
["Semantisk",
"Syntaktisk",
"Didaktisk",
"Pædagogisk"],
kragh_3_title))

qs.append(Question("Hvad er modsætningen til syntaktisk?",
["Semantisk"],
["Syntetisk",
"Analytisk",
"Didaktisk",
"Pædagogisk"],
kragh_3_title))

qs.append(Question("Hvad kunne Turing-maskinen fra 1936?",
["Vise teoretisk hvordan tal blev beregnet"],
["Håndtere både data og instruktioner i hukommelsen",
"Bryde militære koder",
"Implementere en endelig, abstrakt, effektiv og sammensat kontrolstruktur",
"Opnå et givet formål under givne forhold"],
kragh_3_title))

qs.append(Question("Hvilken sætning beskriver bedst Turing-maskinen fra 1936?",
["It is possible to invent a single machine which can be used to compute any computable sequence"],
["It is possible to implement any know algoritm",
"No read up, no write down",
"This machine is founded on new principles and new conceptions, which in turn are painstakingly developed by research in the purest realms of science"],
kragh_3_title))

qs.append(Question("Kan den generelle Turing-maskine afgøre, om enhver anden Turing-maskine på et tidspunk terminerer sit program?",
["Nej, dette kaldes halting-problemet eller Entscheidungsproblemet"],
["Ja, den generelle Turing-maskine er netop generel og kan beregne enhver beregnelig sekvens"],
kragh_3_title))

kragh_4_title = kragh_3_title.replace("3","4")

qs.append(Question("Da NASA i 2011 skulle undersøge problemer med Toyota-biler fandt de ikke noget bevis på, at fejl i bilernes software havde forårsaget de mange ulykker. Hvad konkluderede NASA?",
["Softwaren var så kompleks, at selvom NASA ikke havde fundet noget bevis, kunne det ikke konkluderes, at der ikke var nogen sammenhæng mellem software og ulykkesfrekvens"],
["Softwaren var ikke skyld i ulykkerne",
"Det var nødvendigt med flere test før der kunne konkluderes noget",
"Toyota burde have udført flere test før bilerne blev sat i produktion",
"Toyota havde bevist korrektheden af softwaren igennenm formel verifikation før bilerne blev sat i produktion"],
kragh_4_title))

qs.append(Question("Hvad er i følge Kragh og Johansen den mest realistiske løsning på problemer med at teste store, moderne softwaresystemer?",
["Tænke korrekthed og afprøvning ind i hele udviklingsforløbet"],
["Bevise korrektheden af systemerne igennenm formel verifikation",
"Gennemføre omfattende, systematisk og teoridreven afprøvning",
"Udelukkende anvende open source-software"],
kragh_4_title))

qs.append(Question("Kragh kap. 4 beskriver, at computere både kan studeres ved at bruge formalvidenskab og realvidenskab, og både ved at bruge induktion og deduktion. 3 af de følgende områder kan studeres ved formalvidenskab og deduktion, vælg det sidste der kan studeres ved brug af realvidenskab og induktion:",
["Kørsel af programmet og fysisk afvikling"],
["Algoritme",
"Oversættelse af algoritme til kildekode",
"Oversættelse af kildekode til maskinkode"],
kragh_4_title))

qs.append(Question("Hvilket udsagn er forkert?",
["Objektorienterede sprog og funktionelle sprog er delmængder af mængden af imperative sprog"],
["Procedurelle sprog og objektorienterede sprog er delmængder af mængden af imperative sprogr",
"Funktionelle sprog og logiske sprog er delmængder af mængden af deklarative sprog",
"Procedurelle sprog er en delmængde af mængden af von Neumann-sprog",
"von Neumann-sprog er en delmængde af mængden af imperative sprog"],
kragh_4_title))

qs.append(Question("Din ven har lige lært at kode i Python og siger til dig >>Objekt-orienteret programmering er et paradigme i Kuhnsk forstand<<. Hvad skal du IKKE sige til ham?",
["Ja, introduktionen af Python i 1991 var en videnskabelig revolution i Kuhnsk forstand"],
["Ja, hvis man har en hammer ligner alle problemer søm, og sådan har mange det med Python",
"Vil det sige, at begreber som store O-notation kun giver mening for dig, hvis det handler om algoritmer, der er kodet i Python?",
"Ja, objekt-orienteret programmering er jo en måde at strukturere arbejdet med programmering på, og derfor kan det godt minde lidt om et videnskabeligt paradigme"],
kragh_4_title))

qs.append(Question("Hvordan beskriver Wirth et programmeringssprog?",
["A language represents an abstract computer whose objects and constructs lie closer to, and reflect more directly, the problem to be represented than the concrete machine"],
["A language represents an abstract computer which can be used to compute any computable sequence",
"A language represents an abstract computer that can implement any know algoritm",
"A language is defined by no read up and no write down",
"A language is founded on new principles and new conceptions, which in turn are painstakingly developed by research in the purest realms of science"],
kragh_4_title))

qs.append(Question("Hvilken type programmeringssprog giver programmøren mest kontrol?",
["Et lavniveausprog"],
["Et højniveausprog"],
kragh_4_title))

qs.append(Question("Hvor forekommer garbage collection?",
["I et højniveausprog"],
["I et lavniveausprog"],
kragh_4_title))

qs.append(Question("Hvad kendetegner ikke nødvendigvis et godt programmeringssprog?",
["Nemt at foretage rekursion",
"Nemt at håndtere stakke",
"God adgang til statiske typer",
"Avancerede regler for syntaks",
"Avancerede regler for typehåndtering",
"Garbage collection er indbygget"],
["Nemt at lære",
"Nemt at udtrykke instruktioner",
"Nemt at implementere",
"Nemt at omdanne til maskinkode",
"Stor udbredelse i IT-branchen",
"Stor udbredelse blandt nye programmører under uddannelse"],
kragh_4_title))

qs.append(Question("Hvad var en del af løsningen på softwarekrisen i 1968?",
["Indførelse af struktureret programmering", 
"Mindre brug af go to-kommandoen",
"Øget modularisering af programkode"],
["Indførelse af read down, write up",
"Indførelse af PLACE-samarbejde mellem stat og universiteter",
"Øget fokus på uddannelse og rekruttering"],
kragh_4_title))

kragh_5_title = kragh_4_title.replace("4","5")

qs.append(Question("Hvad er IKKE en læring fra Therac-casen, hvor kræftpatienter blev fejlbehandlet",
["Problemet kunne have været undgået, hvis algoritmen havde været en endelig, effektiv, sammensat, abstrakt kontrolstruktur",
"Programmørerne havde lavet den rigtige kode, den blev bare anvendt forkert",
"Havde udvikleren fulgt Bell-LaPadula-modellen var problemet ikke opstået"],
["Det er svært at teste mod uforudset brug af et system",
"Modularisering kan beskytte mod fejl",
"Det er vigtigt at dokumentere software",
"Programmører har et professionelt ansvar, der ligger ud over det at producere koden",
"Der knytter sig særlige risici til små, specialiserede software-udviklere",
"Det er, ligesom i Toyota-casen, umuligt at teste alle teoretisk mulige use cases for et system",
"Naur havde ret, når han i 1985 sagde at programmørers forståelse af deres eget program er så kompleks, at den ligner forståelse af en videnskabelig teori"],
kragh_5_title))

qs.append(Question("Hvad er IKKE en af de grunde, som Erik Frøkjær nævner, til at store software-projekter ofte fejler?",
["Projekterne afvikles ikke agilt",
"Projekterne identificerer ikke på forhånd samtlige mulige problemer"],
["Utidig indblanding fra kundens side",
"Der sættes ikke tid nok af til udvikling, indførelse og indkøring",
"Projektlederne  har ikke detailkendskab til softwareudvikling som proces"],
kragh_5_title))

qs.append(Question("Hvad er de tre gyldne regler, som Theo Mandel nævner for udvikling af en god brugergrænseflade?",
["Place users in control, reduce users memory load, make the interface consistent"],
["Place users in control, implement any known algorithm, compute any computable sequence",
"Read down, write up, make the interface consistent",
"Place users in control, reduce users memory load by performing garbage collection, make the interface consistent"],
kragh_5_title))

agil_intro = "Du laver gruppearbejde på DIKU, og dine gruppefæller siger: "
agil_end = "Deres arbejdsform er mest udtryk for "
wf = ["Vandfaldsmodellen"]
am = ["Agile metoder"]

qs.append(Question(agil_intro+" Vi lægger en plan og følger den, een ting ad gangen, dokumentation er vigtig. "+agil_end,
wf,
am,
kragh_5_title))

qs.append(Question(agil_intro+" mennesker frem for processer, det vigtigste er at det virker, opstår der problemer tilpasser vi planen. "+agil_end,
am,
wf,
kragh_5_title))

testq_1 = Question(agil_intro+" mennesker frem for processer, det vigtigste er at det virker, opstår der problemer tilpasser vi planen. "+agil_end,
am,
wf,
kragh_5_title)
##testq_1.perform_q()

qs.append(Question(agil_intro+" Vi havde et godt projekt og fik hurtigt produceret noget kode, der demonstrerede de vigtigste dele af vores løsning "+agil_end,
am,
wf,
kragh_5_title))

qs.append(Question(agil_intro+" Vi havde et godt projekt, vi vidste præcis hvad vi ville lave, før vi gik igang. "+agil_end,
wf,
am,
kragh_5_title))

qs.append(Question("Vælg den ting, som er almindeligt anerkendt i datalogi men som ikke har den højeste prioritet i agile metoder",
["Dokumentation af software"],
["Modularisering",
"Test",
"Det imperative programmeringsparadigme",
"Det deklarative programmeringsparadigme"],
kragh_5_title))

waterfall_list = ["System requirements before software requirements",
"Analysis before programme design",
"Code before testing"]

agile_list = ["Individuals and interactions before processes and tools",
"Working software before comprehensive documentation",
"Customer collaboration before contract negotiation",
"Responding to change before following a plan"]

qs.append(Question("Hvad kendetegner IKKE vandfaldsmodellen?",
agile_list,
waterfall_list,
kragh_5_title))

qs.append(Question("Hvad kendetegner IKKE agile metoder?",
waterfall_list,
agile_list,
kragh_5_title))

qs.append(Question("Hvad var den svaghed ved Royces oprindelige vandfaldsmodel, der blev søgt udbedret i den mere generelle modelbaserede udvikling (MBD)?",
["Test lå til sidst og var voldsomt fordyrende og forsinkende, MBD indførte verifikation tidligere i processen"],
["Programmørerne fokuserede på at kode og anerkendte ikke deres bredere ansvar for det endelige produkt",
"Dokumentation af kode var ikke et selvstændigt element",
"Processer og redskaber var vigtigere end samspillet mellem enkeltpersoner"],
kragh_5_title))

qs.append(Question("Modeller + transformationer =",
["Software"],
["Resultater",
"Nye modeller",
"Systemkrav",
"Algoritmer",
"Datastrukturer"],
kragh_5_title))

qs.append(Question("Hvad er hverken en af de tre overordnede kategorier eller 11 underkategorier som opstillet af Mcall og Pressmann som kriterier for god software?",
["Falsifiability",
"Product testing",
"Product documentation"],
["Maintainability",
"Flexibility",
"Testability",
"Portability",
"Reusability",
"Interoperability",
"Correctness",
"Usability",
"Reliability",
"Integrity",
"Efficiency",
"Product revision",
"Product transition",
"Product operation"],
kragh_5_title))

qs.append(Question("Hvad er >>Second system effect<< som Brooks nævner som en mulig kilde til problemer i store softwareprojekter?",
["Programmet udvider sig i retning af hvad der er teknisk muligt fremfor hvad der oprindeligt var bestilt"],
["Datidens computere kunne ikke som i dag afvikle flere programmer samtidig",
"Flere dele af det samme program prøvede at skrive til den samme plads i hukommelsen",
"De oprindelige systemer blev udviklet på en måde, der ikke var koordineret eller veldokumenteret"],
kragh_5_title))

qs.append(Question("Hvad er de fire fejlkilder til problemer i store softwareprojekter, som Brooks nævner?",
["No mythical man month, no silver bullit, second system effect, irreducible number of errors"],
["No mythical man month, no silver bullit, second system effect, no read up no write down",
"No maintainability, no flexibility, no testability, no portability",
"No reusability, no interoperability, no correctness, no usability"],
kragh_5_title))

qs.append(Question("Hvad er IKKE en af de tre måder, som Gruner i 2011 mente man kunne se softwareudvikling på?",
["Hardware-centreret: god software er baseret på stadig bedre hardware"],
["Formalistisk: god software er baseret på matematiske objekter og kan verificeres formelt",
"Ingeniør-centreret: god software er baseret på gode processer og workflow",
"Humanistisk: god software er baseret på god interaktion mellem dem der koder indbyrdes og mellem dem der koder og dem der bruger koden"],
kragh_5_title))

kragh_6a_title = kragh_5_title.replace("5","6a")

qs.append(Question("Kragh kap. 6a figur 4 viser nogle led i en modelleringsproces, herunder virkeligheden, verbal (konceptuel) model, matematisk model og kørsel. Figuren rummer yderligere eet led, nemlig hvilket?",
["Diskretiseret model"],
["Empirisk model",
"Falsificerbar model",
"Algoritmisk model"],
kragh_6a_title))

qs.append(Question("Hvilket et af disse udsagn er forkert?",
["Hvis jeg er interesseret i, hvad jeg kan lære af en model, kan man sige at jeg lægger vægt på modellens ontologiske funktion",
"Da Bohr modellerede atomet som et solssystem anvendte han en ikonisk model"],
["Da Bohr modellerede atomet som et solsystem anvendte han en analogimodel",
"Hvis jeg er interesseret i, hvad jeg kan lære af en model, kan man sige at jeg lægger vægt på modellens epistemiske funktion",
"Hvis lægen viser mig en detaljeret tegning af en lunge anvender han en ikonisk model",
"Hvis lægen beregner mit BMI anvender han en matematisk model",
"Hvis lægen opfordrer mig til at forbedre mit BMI, anvender han BMI som proxy for min helbredstilstand",
"Sundhedssektoren fokuserer så meget på BMI, at BMI er blevet en kanonisk proxy for helbredstilstand"],
kragh_6a_title))

kragh_6b_title = kragh_6a_title.replace("6a","6b")

qs.append(Question("Hvad nævnes ikke i "+kragh_6b_title+" som noget, der kan kendetegne en god forklaring?",
["At der allerede i den oprindelige model er gjort overvejelser om, hvordan modellen kunne forklares"],
["At forklaringen er svar på et hvorfor-spørgsmål",
"At forklaringen er udledt deduktivt fra en lovmæssighed",
"At det, der forklares er en kausal virkning af en årsag",
"At forklaringen relaterer sig til en egenskab, der er statistisk relevant for det, der skal forklares"],
kragh_6b_title))

qs.append(Question("Du bliver bedt om at forklare, hvorfor nogle individer i en population har egenskaben A. Hvilken forklaring er en SR-forklaring?",
["At et individ har egenskaben A skyldes ofte, at de også har egenskaben B. Det kan ses ved, at P(A|B) er meget større end P(A)"],
["Den generelle teori om B fastslår, at B forårsager A, så når vi iagttager A i populationen må det skyldes B",
"Den generelle teori om A fastslår, at A ofte forårsages af B, så når vi iagttager A i population må det skyldes B"
"A skyldes B, men den nærmere sammenhæng er en black box",
"Hvis B er forårsaget af A behøver vi ikke at inddrage andre elementer i forklaringer, så B er den bedste forklaring"],
kragh_6b_title))

qs.append(Question("Hvad indgår ikke i en datakurateringsproces?",
["Falsifikation af data",
"Verifikation af, at de oprindelige data er teorifrie og værdifrie"],
["Afgrænsning af genstandsfeltet",
"Måling af data i form af proxies",
"Annotering af data med metadata",
"Filtrering af data i form af fjernelse af outliers",
"Filtrering af data i form af stratificering og identifikation af andre systematiske forskelle i data",
"Data holdes opdateret"],
kragh_6b_title))

qs.append(Question("Hvad mentes med The End of Theory i 2008?",
["Big data gjorde det muligt at udlede teorier direkte ved induktion fra store datamængder"],
["Finanskrisen havde karakter af en videnskablig revolution",
"Problemer med store IT-projekter gjorde det nødvendigt at udvikle software på en ny måde",
"Alle eksisterende teorier kunne nu med det samme falsificeres ved hjælp af Big Data"],
kragh_6b_title))

qs.append(Question("Anvend følgende forkortelser: T = True, F = False, P= Positive, N = Negative, n = antal observationer. Hvilket udsagn er forkert?",
["F1 = (Precision*Recall)/(Precision + Recall)"],
["Accuracy = (TP+ TN) / n",
"Precision = TP / (TP+FP)",
"Specificity= TN / (TN+FP)",
"Recall = TP / (TP+FN)"],
kragh_6b_title))

qs.append(Question("En model forudsiger individer i en population som værende enten positive eller negative. Hvilket udsagn er forkert?",
["Hvis specificity er 57 pct. så er 57 pct. af de individer, der faktisk var positive, blevet forudsagt korrekt"],
["Hvis accuracy er 57 pct., så er 57 pct. af individerne blevet forudsagt korrekt",
"Hvis precision er 57 pct. så er 57 pct. af de individer, der blev forudsagt til at være positive blevet forudsagt korrekt",
"Hvis specificity er 57 pct. så er 57 pct. af de individer, der faktisk var negative, blevet forudsagt korrekt",
"Hvis recall er 57 pct. så er 57 pct. af de invidider, der faktisk var positive, blevet forudsagt korrekt"],
kragh_6b_title))

ku_title = "KUs ordensregler af 1. marts 2023"

qs.append(Question("Hvad er IKKE eksamenssnyd som defineret i "+ku_title,
["Chikanerende, truende eller voldelig adfærd",
"Dokumentfalsk",
"Forstyrrelse af undervisningen og støjende adfærd",
"Hærværk",
"Krænkelse af immaterielle rettigheder",
"Krænkende handlinger som f.eks. mobning, nedværdigelse, seksuel chikane",
"Manglende efterlevelse af en studienævnsafgørelse",
"Misbrug af data/datahackning",
"Overtrædelse af normerne for patient/klient-kontakt",
"Overtrædelse af rygeforbud",
"Tyveri",
"Ulovlig besiddelse af euforiserende stoffer"],
["Plagiat",
"Selvplagiat (genbrug af egen tekst uden henvisning)",
"Ikke-tilladt samarbejde",
"Brug af fællesnoter uden henvisning",
"Modtagelse af hjælp under eksamen eller hjælp til andre, når der ikke er tale om en gruppeeksamen",
"Ikke-tilladte hjælpemidler",
"Forfalskning",
"Fabrikering",
"Forudgående kendskab til eksamensopgaven",
"Omgåelse, deaktivering eller på anden vis hindring af universitetets eventuelle anvendelse af elektroniske overvågningsprogrammer",
"Urigtige fremmødeoplysninger"],
ku_title))

kragh_10_title = kragh_2_title.replace("2","10")

qs.append(Question("For at en forsker skal kunne stå som medforfatter til en videnskabelig artikel kræver Vancouver-protokollen, at forskeren skal have ydet",
["SUBSTANTIAL contributions to 1) conception and design, or analysis and interpretation of data AND to 2) drafting the article or revising it critically for important intellectual content AND 3) final approval of the version to be published"],
["SUBSTANTIAL contributions to 1) conception and design, or analysis and interpretation of data OR to 2) drafting the article or revising it critically for important intellectual content OR 3) final approval of the version to be published",
"CONTRIBUTIONS to 1) conception and design, or analysis and interpretation of data OR to 2) drafting the article or revising it critically for important intellectual content OR 3) final approval of the version to be published",
"contributions of substantial academic importance"],
kragh_10_title))

qs.append(Question(kragh_10_title+" nævner et eksempel, hvor studerende faktisk er underlagt strengere regler end forskere. Hvilket?",
["Urigtige oplysninger om forfatterskab betragtes som eksamenssnyd, når det begås af studerende, men som tvivlsom forskningspraksis, når det begås af forskere"],
["Urigtige oplysninger om forfatterskab betragtes som eksamenssnyd, når det begås af studerende, men som videnskabelig uredelighed, når det begås af forskere",
"Plagiat er afgrænset til tekstplagiat i gymnasiet mens der på universiteterne anvendes en bredere definition",
"Studerende behøver ikke at spørge deres vejleder før de beslutter, at misvisende forsøgsresultater ikke skal medtages i den endelige rapport"],
kragh_10_title))

qs.append(Question("Hvad er den naturalistiske fejlslutning?",
["Den handling, som de fleste udviser i en given situation, er også den rigtige handling"],
["Computational thinking kan anvendes på alle videnskabelige områder som beskrevet af Wing",
"Data er værdifrie og interessefrie",
"At bekræfte en i forvejen kendt hypotese skaber ikke ny viden"],
kragh_10_title))

qs.append(Question("Hvad udtrykker IKKE en af Jesper Rybergs 4 undskyldninger?",
["Jeg gjorde bare mit bedste",
"Jeg gjorde bare som alle andre ville have gjort"],
["Staten er vogter af moralen, er det ikke ulovligt er det tilladt",
"Vi kan ikke forudsige konsekvenserne af innovation",
"Jeg gjorde det bare muligt",
"Hvis ikke mig så en anden"],
kragh_10_title))



source_list = []
for q in qs:
    source_list.append(q.source)

source_list = list(set(source_list))

score = 0
n = 0

random.shuffle(qs)

print("Velkommen til VT-Dat multiple choice.")
print("Af Tim Mondorf (DIKU), cjk681@alumni.ku.dk")
print("Der er "+str(len(qs))+" spørgsmål")
print("Kilder er Kragh og Johansen Invitation til de datalogiske fags videnskabsteori og øvrig obligatorisk litteratur i VT-Dat 2023, jf. kursusrummet på Absalon")
print("Testen er udviklet som eksamensforberedelse til multiple choice-prøve. Tast 1, 2, 3 eller 4 for den ønskede svarmulighed eller 0 for afslutning.")
print()

for q in qs:
    n += 1
    print("Spørgsmål "+str(n)+" ud af "+str(len(qs)))
    score += q.perform_q()
    print("Antal rigtige indtil nu: "+str(score)+" ud af "+str(n) )
    print()
print("Din score er "+str(score)+ " ud af "+str(len(qs)))

if len(sources_of_error)>0:
    error_source_dict = {}
    for source in source_list:
        error_source_dict[source] = sources_of_error.count(source)
    sources = sorted(error_source_dict)
    sources.sort(reverse=True)
    print("Fordeling af fejl på kilder:")
    for source in sources:
        if error_source_dict[source] != 0:
            print(source + ": "+str(error_source_dict[source]))


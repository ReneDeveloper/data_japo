#verbos_curso_rena_100.py

#url
#https://youtu.be/AaTxGs5wnjQ?si=EMHw0nPIDmpEV0XL
#https://www.youtube.com/watch?v=AaTxGs5wnjQ&ab_channel=Japon%C3%A9sconRena

#ulr música
#https://www.youtube.com/watch?v=04csWHRyReo&ab_channel=RKVC-Topic


#url de rena
#https://www.italki.com/es/teacher/6823291/japanese



from data_verbos import verbos

# Ahora puedes utilizar el arreglo `verbos` en tu código
#print(verbos)


import pyttsx3

class Verbo:
    def __init__(self, id, kanji, hiragana, romaji, es, en):
        self.id = id
        self.kanji = kanji
        self.hiragana = hiragana
        self.romaji = romaji
        self.es = es
        self.en = en

    def speak(self, language='es'):
        engine = pyttsx3.init()
        if language == 'es':
            engine.say(self.es)
        elif language == 'en':
            engine.say(self.en)
        elif language == 'jp':
            engine.say(self.romaji)
        engine.runAndWait()

# Crear lista de objetos Verbo
verbos_objetos = [Verbo(id+1, verbo["kanji"], verbo["hiragana"], verbo["romaji"], verbo["es"], verbo["en"]) for id, verbo in enumerate(verbos)]

# Ejemplo de uso
verbo_ejemplo = verbos_objetos[0]
print(f"Verbo: {verbo_ejemplo.kanji} ({verbo_ejemplo.romaji}) - Español: {verbo_ejemplo.es}, Inglés: {verbo_ejemplo.en}")



for verbo in verbos_objetos:
    #print(verbo["romaji"])
    print(f"Verbo: {verbo.kanji} ({verbo.romaji}) - Español: {verbo.es}, Inglés: {verbo.en}")
    
    verbo.speak('jp')
    verbo.speak('es')





"""
#VERBOS DE RENA
taberu
miru
miseru
hanasu
kiku
akeru
shimeru
nomu
hataraku
yasumu
yomu
kaku
wasureru
wakaru
oshieru
narau
iku
kuru
kaeru
neru
okiru
owaru
hajimeru
aru
iru
agemasu
morau
kau
uru
shashin o toru
tsukau
au
matsu
tsukuru
hashiru
oyogu
utau
odoru
asobu
noru
oriru
kesu
tsukeru
shinu
ikiru
sumu
suwaru
tatsu
suu
tasukeru
tetsudau
hairu
ireru
deru
dekakeru
dasu
motsu
kaesu
kariru
kazu
watasu
omou
iu
kiru
warau
shikaru
okoru
naku
kakaru
isogu
hiku
onakagasuku
nodokawaku
shawaaoabiru
denwaokakeru
tariru
suru
benkyosuru
shokuyishimasu
renshusuru
fukushuusuru
kekkonsuru
soujisuru
tsutomeru
kiru
haku
nugo
kotaeru
shiru
umareru
oboeru
tobu
arau
migaku
ryourisuru
ryokousuru
sentakusuru
shitsumonsuru
sanposuru
denwasuru






"""
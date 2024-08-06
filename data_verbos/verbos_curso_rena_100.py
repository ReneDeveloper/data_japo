#verbos_curso_rena_100.py

#url
#https://youtu.be/AaTxGs5wnjQ?si=EMHw0nPIDmpEV0XL
#https://www.youtube.com/watch?v=AaTxGs5wnjQ&ab_channel=Japon%C3%A9sconRena

#ulr música
#https://www.youtube.com/watch?v=04csWHRyReo&ab_channel=RKVC-Topic


#url de rena
#https://www.italki.com/es/teacher/6823291/japanese























































































verbos = [
    {"kanji": "食べる", "hiragana": "たべる", "romaji": "taberu", "es": "comer", "en": "eat"},
    {"kanji": "見る", "hiragana": "みる", "romaji": "miru", "es": "ver", "en": "see"},
    {"kanji": "見せる", "hiragana": "みせる", "romaji": "miseru", "es": "mostrar", "en": "show"},
    {"kanji": "話す", "hiragana": "はなす", "romaji": "hanasu", "es": "hablar", "en": "speak"},
    {"kanji": "聞く", "hiragana": "きく", "romaji": "kiku", "es": "escuchar", "en": "listen"},
    {"kanji": "開ける", "hiragana": "あける", "romaji": "akeru", "es": "abrir", "en": "open"},
    {"kanji": "閉める", "hiragana": "しめる", "romaji": "shimeru", "es": "cerrar", "en": "close"},
    {"kanji": "飲む", "hiragana": "のむ", "romaji": "nomu", "es": "beber", "en": "drink"},
    {"kanji": "働く", "hiragana": "はたらく", "romaji": "hataraku", "es": "trabajar", "en": "work"},
    {"kanji": "休む", "hiragana": "やすむ", "romaji": "yasumu", "es": "descansar", "en": "rest"},
    {"kanji": "読む", "hiragana": "よむ", "romaji": "yomu", "es": "leer", "en": "read"},
    {"kanji": "書く", "hiragana": "かく", "romaji": "kaku", "es": "escribir", "en": "write"},
    {"kanji": "忘れる", "hiragana": "わすれる", "romaji": "wasureru", "es": "olvidar", "en": "forget"},
    {"kanji": "分かる", "hiragana": "わかる", "romaji": "wakaru", "es": "entender", "en": "understand"},
    {"kanji": "教える", "hiragana": "おしえる", "romaji": "oshieru", "es": "enseñar", "en": "teach"},
    {"kanji": "習う", "hiragana": "ならう", "romaji": "narau", "es": "aprender", "en": "learn"},
    {"kanji": "行く", "hiragana": "いく", "romaji": "iku", "es": "ir", "en": "go"},
    {"kanji": "来る", "hiragana": "くる", "romaji": "kuru", "es": "venir", "en": "come"},
    {"kanji": "帰る", "hiragana": "かえる", "romaji": "kaeru", "es": "volver", "en": "return"},
    {"kanji": "寝る", "hiragana": "ねる", "romaji": "neru", "es": "dormir", "en": "sleep"},
    {"kanji": "起きる", "hiragana": "おきる", "romaji": "okiru", "es": "despertar", "en": "wake up"},
    {"kanji": "終わる", "hiragana": "おわる", "romaji": "owaru", "es": "terminar", "en": "end"},
    {"kanji": "始める", "hiragana": "はじめる", "romaji": "hajimeru", "es": "comenzar", "en": "begin"},
    {"kanji": "ある", "hiragana": "ある", "romaji": "aru", "es": "haber (inanimado)", "en": "exist (inanimate)"},
    {"kanji": "いる", "hiragana": "いる", "romaji": "iru", "es": "haber (animado)", "en": "exist (animate)"},
    {"kanji": "あげます", "hiragana": "あげます", "romaji": "agemasu", "es": "dar", "en": "give"},
    {"kanji": "もらう", "hiragana": "もらう", "romaji": "morau", "es": "recibir", "en": "receive"},
    {"kanji": "買う", "hiragana": "かう", "romaji": "kau", "es": "comprar", "en": "buy"},
    {"kanji": "売る", "hiragana": "うる", "romaji": "uru", "es": "vender", "en": "sell"},
    {"kanji": "写真を撮る", "hiragana": "しゃしんをとる", "romaji": "shashin o toru", "es": "tomar una foto", "en": "take a photo"},
    {"kanji": "使う", "hiragana": "つかう", "romaji": "tsukau", "es": "usar", "en": "use"},
    {"kanji": "会う", "hiragana": "あう", "romaji": "au", "es": "encontrarse", "en": "meet"},
    {"kanji": "待つ", "hiragana": "まつ", "romaji": "matsu", "es": "esperar", "en": "wait"},
    {"kanji": "作る", "hiragana": "つくる", "romaji": "tsukuru", "es": "hacer", "en": "make"},
    {"kanji": "走る", "hiragana": "はしる", "romaji": "hashiru", "es": "correr", "en": "run"},
    {"kanji": "泳ぐ", "hiragana": "およぐ", "romaji": "oyogu", "es": "nadar", "en": "swim"},
    {"kanji": "歌う", "hiragana": "うたう", "romaji": "utau", "es": "cantar", "en": "sing"},
    {"kanji": "踊る", "hiragana": "おどる", "romaji": "odoru", "es": "bailar", "en": "dance"},
    {"kanji": "遊ぶ", "hiragana": "あそぶ", "romaji": "asobu", "es": "jugar", "en": "play"},
    {"kanji": "乗る", "hiragana": "のる", "romaji": "noru", "es": "montar", "en": "ride"},
    {"kanji": "降りる", "hiragana": "おりる", "romaji": "oriru", "es": "bajar", "en": "get off"},
    {"kanji": "消す", "hiragana": "けす", "romaji": "kesu", "es": "apagar", "en": "turn off"},
    {"kanji": "つける", "hiragana": "つける", "romaji": "tsukeru", "es": "encender", "en": "turn on"},
    {"kanji": "死ぬ", "hiragana": "しぬ", "romaji": "shinu", "es": "morir", "en": "die"},
    {"kanji": "生きる", "hiragana": "いきる", "romaji": "ikiru", "es": "vivir", "en": "live"},
    {"kanji": "住む", "hiragana": "すむ", "romaji": "sumu", "es": "residir", "en": "reside"},
    {"kanji": "座る", "hiragana": "すわる", "romaji": "suwaru", "es": "sentarse", "en": "sit"},
    {"kanji": "立つ", "hiragana": "たつ", "romaji": "tatsu", "es": "levantarse", "en": "stand"},
    {"kanji": "吸う", "hiragana": "すう", "romaji": "suu", "es": "fumar/inhalar", "en": "smoke/inhale"},
    {"kanji": "助ける", "hiragana": "たすける", "romaji": "tasukeru", "es": "ayudar", "en": "help"},
    {"kanji": "手伝う", "hiragana": "てつだう", "romaji": "tetsudau", "es": "asistir", "en": "assist"},
    {"kanji": "入る", "hiragana": "はいる", "romaji": "hairu", "es": "entrar", "en": "enter"},
    {"kanji": "入れる", "hiragana": "いれる", "romaji": "ireru", "es": "meter", "en": "put in"},
    {"kanji": "出る", "hiragana": "でる", "romaji": "deru", "es": "salir", "en": "exit"},
    {"kanji": "出かける", "hiragana": "でかける", "romaji": "dekakeru", "es": "salir (para)", "en": "go out"},
    {"kanji": "出す", "hiragana": "だす", "romaji": "dasu", "es": "sacar", "en": "take out"},
    {"kanji": "持つ", "hiragana": "もつ", "romaji": "motsu", "es": "tener", "en": "have/hold"},
    {"kanji": "返す", "hiragana": "かえす", "romaji": "kaesu", "es": "devolver", "en": "return (an item)"},
    {"kanji": "借りる", "hiragana": "かりる", "romaji": "kariru", "es": "tomar prestado", "en": "borrow"},
    {"kanji": "数える", "hiragana": "かぞえる", "romaji": "kazu", "es": "contar", "en": "count"},
    {"kanji": "渡す", "hiragana": "わたす", "romaji": "watasu", "es": "entregar", "en": "hand over"},
    {"kanji": "思う", "hiragana": "おもう", "romaji": "omou", "es": "pensar", "en": "think"},
    {"kanji": "言う", "hiragana": "いう", "romaji": "iu", "es": "decir", "en": "say"},
    {"kanji": "着る", "hiragana": "きる", "romaji": "kiru", "es": "vestir", "en": "wear"},
    {"kanji": "笑う", "hiragana": "わらう", "romaji": "warau", "es": "reír", "en": "laugh"},
    {"kanji": "叱る", "hiragana": "しかる", "romaji": "shikaru", "es": "regañar", "en": "scold"},
    {"kanji": "怒る", "hiragana": "おこる", "romaji": "okoru", "es": "enojarse", "en": "get angry"},
    {"kanji": "泣く", "hiragana": "なく", "romaji": "naku", "es": "llorar", "en": "cry"},
    {"kanji": "かかる", "hiragana": "かかる", "romaji": "kakaru", "es": "tardar", "en": "take (time/money)"},
    {"kanji": "急ぐ", "hiragana": "いそぐ", "romaji": "isogu", "es": "apresurarse", "en": "hurry"},
    {"kanji": "引く", "hiragana": "ひく", "romaji": "hiku", "es": "tirar", "en": "pull"},
    {"kanji": "お腹が空く", "hiragana": "おなかがすく", "romaji": "onakagasuku", "es": "tener hambre", "en": "be hungry"},
    {"kanji": "喉が渇く", "hiragana": "のどがかわく", "romaji": "nodokawaku", "es": "tener sed", "en": "be thirsty"},
    {"kanji": "シャワーを浴びる", "hiragana": "しゃわーをあびる", "romaji": "shawaa o abiru", "es": "ducharse", "en": "take a shower"},
    {"kanji": "電話をかける", "hiragana": "でんわをかける", "romaji": "denwa o kakeru", "es": "hacer una llamada", "en": "make a call"},
    {"kanji": "足りる", "hiragana": "たりる", "romaji": "tariru", "es": "ser suficiente", "en": "be enough"},
    {"kanji": "する", "hiragana": "する", "romaji": "suru", "es": "hacer", "en": "do"},
    {"kanji": "勉強する", "hiragana": "べんきょうする", "romaji": "benkyou suru", "es": "estudiar", "en": "study"},
    {"kanji": "食事します", "hiragana": "しょくじします", "romaji": "shokuji shimasu", "es": "comer (formal)", "en": "have a meal"},
    {"kanji": "練習する", "hiragana": "れんしゅうする", "romaji": "renshuu suru", "es": "practicar", "en": "practice"},
    {"kanji": "復習する", "hiragana": "ふくしゅうする", "romaji": "fukushuu suru", "es": "repasar", "en": "review"},
    {"kanji": "結婚する", "hiragana": "けっこんする", "romaji": "kekkon suru", "es": "casarse", "en": "marry"},
    {"kanji": "掃除する", "hiragana": "そうじする", "romaji": "souji suru", "es": "limpiar", "en": "clean"},
    {"kanji": "務める", "hiragana": "つとめる", "romaji": "tsutomeru", "es": "trabajar (formal)", "en": "work (formal)"},
    {"kanji": "着る", "hiragana": "きる", "romaji": "kiru", "es": "ponerse", "en": "put on"},
    {"kanji": "履く", "hiragana": "はく", "romaji": "haku", "es": "ponerse (calzado)", "en": "put on (shoes)"},
    {"kanji": "脱ぐ", "hiragana": "ぬぐ", "romaji": "nugu", "es": "quitarse (ropa)", "en": "take off (clothes)"},
    {"kanji": "答える", "hiragana": "こたえる", "romaji": "kotaeru", "es": "responder", "en": "answer"},
    {"kanji": "知る", "hiragana": "しる", "romaji": "shiru", "es": "saber", "en": "know"},
    {"kanji": "生まれる", "hiragana": "うまれる", "romaji": "umareru", "es": "nacer", "en": "be born"},
    {"kanji": "覚える", "hiragana": "おぼえる", "romaji": "oboeru", "es": "recordar", "en": "remember"},
    {"kanji": "飛ぶ", "hiragana": "とぶ", "romaji": "tobu", "es": "volar", "en": "fly"},
    {"kanji": "洗う", "hiragana": "あらう", "romaji": "arau", "es": "lavar", "en": "wash"},
    {"kanji": "磨く", "hiragana": "みがく", "romaji": "migaku", "es": "cepillar", "en": "brush"},
    {"kanji": "料理する", "hiragana": "りょうりする", "romaji": "ryouri suru", "es": "cocinar", "en": "cook"},
    {"kanji": "旅行する", "hiragana": "りょこうする", "romaji": "ryokou suru", "es": "viajar", "en": "travel"},
    {"kanji": "洗濯する", "hiragana": "せんたくする", "romaji": "sentaku suru", "es": "lavar ropa", "en": "do laundry"},
    {"kanji": "質問する", "hiragana": "しつもんする", "romaji": "shitsumon suru", "es": "preguntar", "en": "ask"},
    {"kanji": "散歩する", "hiragana": "さんぽする", "romaji": "sanpo suru", "es": "pasear", "en": "walk"},
    {"kanji": "電話する", "hiragana": "でんわする", "romaji": "denwa suru", "es": "llamar", "en": "call"},
]




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





verbo_ejemplo.speak('es')


verbo_ejemplo.speak('jp')
































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
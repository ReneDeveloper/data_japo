data_adjetivos_jp.py

# data_adjetivos.py

# 1. Dimensión Tamaño
dimension_tamaño = {
    1: {"es": "diminuto", "jp_kanji": "微小", "romaji": "bishō"},
    2: {"es": "minúsculo", "jp_kanji": "極小", "romaji": "kyokushō"},
    3: {"es": "pequeño", "jp_kanji": "小さい", "romaji": "chiisai"},
    4: {"es": "corto", "jp_kanji": "短い", "romaji": "mijikai"},
    5: {"es": "estrecho", "jp_kanji": "狭い", "romaji": "semai"},
    6: {"es": "bajo", "jp_kanji": "低い", "romaji": "hikui"},
    7: {"es": "largo", "jp_kanji": "長い", "romaji": "nagai"},
    8: {"es": "alto", "jp_kanji": "高い", "romaji": "takai"},
    9: {"es": "ancho", "jp_kanji": "広い", "romaji": "hiroi"},
    10: {"es": "grande", "jp_kanji": "大きい", "romaji": "ōkii"},
    11: {"es": "voluminoso", "jp_kanji": "かさばる", "romaji": "kasabaru"},
    12: {"es": "enorme", "jp_kanji": "巨大", "romaji": "kyodai"},
    13: {"es": "colosal", "jp_kanji": "巨大", "romaji": "kyodai"},
    14: {"es": "gigante", "jp_kanji": "巨大", "romaji": "kyodai"},
    15: {"es": "masivo", "jp_kanji": "大規模", "romaji": "daikibo"},
    16: {"es": "monstruoso", "jp_kanji": "怪物のような", "romaji": "kaibutsu no yō na"}
}

# 2. Dimensión Peso
dimension_peso = {
    1: {"es": "ligero", "jp_kanji": "軽い", "romaji": "karui"},
    2: {"es": "liviano", "jp_kanji": "軽量", "romaji": "keiryō"},
    3: {"es": "compacto", "jp_kanji": "コンパクト", "romaji": "konpakuto"},
    4: {"es": "denso", "jp_kanji": "密度の高い", "romaji": "mitsudo no takai"},
    5: {"es": "pesado", "jp_kanji": "重い", "romaji": "omoi"},
    6: {"es": "colosal", "jp_kanji": "巨大な", "romaji": "kyodai na"},
    7: {"es": "masivo", "jp_kanji": "大規模な", "romaji": "daikibo na"},
    8: {"es": "opulento", "jp_kanji": "豪華な", "romaji": "gōka na"}
}

# 3. Dimensión Edad
dimension_edad = {
    1: {"es": "nuevo", "jp_kanji": "新しい", "romaji": "atarashii"},
    2: {"es": "joven", "jp_kanji": "若い", "romaji": "wakai"},
    3: {"es": "reciente", "jp_kanji": "最近の", "romaji": "saikin no"},
    4: {"es": "moderno", "jp_kanji": "現代的な", "romaji": "gendaiteki na"},
    5: {"es": "actual", "jp_kanji": "現在の", "romaji": "genzai no"},
    6: {"es": "vigente", "jp_kanji": "有効な", "romaji": "yūkō na"},
    7: {"es": "viejo", "jp_kanji": "古い", "romaji": "furui"},
    8: {"es": "antiguo", "jp_kanji": "昔の", "romaji": "mukashi no"},
    9: {"es": "pasado", "jp_kanji": "過去の", "romaji": "kako no"},
    10: {"es": "histórico", "jp_kanji": "歴史的な", "romaji": "rekishiteki na"},
    11: {"es": "perenne", "jp_kanji": "永続的な", "romaji": "eizokuteki na"},
    12: {"es": "eterno", "jp_kanji": "永遠の", "romaji": "eien no"},
    13: {"es": "anacrónico", "jp_kanji": "時代遅れの", "romaji": "jidaiokure no"},
    14: {"es": "obsoleto", "jp_kanji": "廃れた", "romaji": "sutareta"},
    15: {"es": "desfasado", "jp_kanji": "時代遅れの", "romaji": "jidaiokure no"},
    16: {"es": "caducado", "jp_kanji": "期限切れの", "romaji": "kigen gire no"}
}

# 4. Dimensión Velocidad
dimension_velocidad = {
    1: {"es": "lento", "jp_kanji": "遅い", "romaji": "osoi"},
    2: {"es": "perezoso", "jp_kanji": "怠惰な", "romaji": "taida na"},
    3: {"es": "torpe", "jp_kanji": "不器用な", "romaji": "bukiyō na"},
    4: {"es": "tardo", "jp_kanji": "遅い", "romaji": "osoi"},
    5: {"es": "despacio", "jp_kanji": "ゆっくり", "romaji": "yukkuri"},
    6: {"es": "pausado", "jp_kanji": "ゆったりした", "romaji": "yuttari shita"},
    7: {"es": "tranquilo", "jp_kanji": "穏やかな", "romaji": "odayaka na"},
    8: {"es": "estático", "jp_kanji": "静止した", "romaji": "seishi shita"},
    9: {"es": "constante", "jp_kanji": "一定の", "romaji": "ittei no"},
    10: {"es": "rápido", "jp_kanji": "速い", "romaji": "hayai"},
    11: {"es": "ágil", "jp_kanji": "敏捷な", "romaji": "binshō na"},
    12: {"es": "dinámico", "jp_kanji": "動的な", "romaji": "dōteki na"},
    13: {"es": "acelerado", "jp_kanji": "加速した", "romaji": "kasoku shita"},
    14: {"es": "implacable", "jp_kanji": "容赦ない", "romaji": "yōsha nai"},
    15: {"es": "inmóvil", "jp_kanji": "動かない", "romaji": "ugokanai"},
    16: {"es": "retardado", "jp_kanji": "遅れた", "romaji": "okureta"}
}

# 5. Dimensión Estado
dimension_estado = {
    1: {"es": "sano", "jp_kanji": "健康な", "romaji": "kenkō na"},
    2: {"es": "limpio", "jp_kanji": "清潔な", "romaji": "seiketsu na"},
    3: {"es": "fresco", "jp_kanji": "新鮮な", "romaji": "shinsen na"},
    4: {"es": "intacto", "jp_kanji": "無傷の", "romaji": "mukizu no"},
    5: {"es": "robusto", "jp_kanji": "頑丈な", "romaji": "ganjō na"},
    6: {"es": "vacío", "jp_kanji": "空の", "romaji": "kara no"},
    7: {"es": "lleno", "jp_kanji": "満たされた", "romaji": "mitasareta"},
    8: {"es": "caliente", "jp_kanji": "熱い", "romaji": "atsui"},
    9: {"es": "frío", "jp_kanji": "冷たい", "romaji": "tsumetai"},
    10: {"es": "sucio", "jp_kanji": "汚い", "romaji": "kitanai"},
    11: {"es": "enfermo", "jp_kanji": "病気の", "romaji": "byōki no"},
    12: {"es": "vivo", "jp_kanji": "生きている", "romaji": "ikite iru"},
    13: {"es": "muerto", "jp_kanji": "死んだ", "romaji": "shinda"},
    14: {"es": "frágil", "jp_kanji": "壊れやすい", "romaji": "kowareyasui"},
    15: {"es": "dañado", "jp_kanji": "損傷した", "romaji": "sonshō shita"},
    16: {"es": "perjudicado", "jp_kanji": "害された", "romaji": "gai sareta"}
}

# 6. Dimensión Belleza Estética
dimension_belleza_estetica = {
    1: {"es": "repulsivo", "jp_kanji": "嫌悪感を引き起こす", "romaji": "ken'okan o hikiokosu"},
    2: {"es": "tétrico", "jp_kanji": "陰気な", "romaji": "inki na"},
    3: {"es": "horrible", "jp_kanji": "恐ろしい", "romaji": "osoroshii"},
    4: {"es": "feo", "jp_kanji": "醜い", "romaji": "minikui"},
    5: {"es": "desagradable", "jp_kanji": "不快な", "romaji": "fukai na"},
    6: {"es": "vulgar", "jp_kanji": "下品な", "romaji": "gehin na"},
    7: {"es": "apagado", "jp_kanji": "鈍い", "romaji": "nibui"},
    8: {"es": "neutro", "jp_kanji": "中立的な", "romaji": "chūritsuteki na"},
    9: {"es": "sutil", "jp_kanji": "微妙な", "romaji": "bimyō na"},
    10: {"es": "brillante", "jp_kanji": "輝く", "romaji": "kagayaku"},
    11: {"es": "bonito", "jp_kanji": "かわいい", "romaji": "kawaii"},
    12: {"es": "lindo", "jp_kanji": "可愛らしい", "romaji": "kawairashii"},
    13: {"es": "atractivo", "jp_kanji": "魅力的な", "romaji": "miryokuteki na"},
    14: {"es": "elegante", "jp_kanji": "優雅な", "romaji": "yūga na"},
    15: {"es": "hermoso", "jp_kanji": "美しい", "romaji": "utsukushii"},
    16: {"es": "espléndido", "jp_kanji": "素晴らしい", "romaji": "subarashii"}
}

# 7. Dimensión Personalidad
dimension_personalidad = {
    1: {"es": "sincero", "jp_kanji": "誠実な", "romaji": "seijitsu na"},
    2: {"es": "amable", "jp_kanji": "親切な", "romaji": "shinsetsu na"},
    3: {"es": "entusiasta", "jp_kanji": "熱心な", "romaji": "nesshin na"},
    4: {"es": "prudente", "jp_kanji": "慎重な", "romaji": "shinchō na"},
    5: {"es": "respetuoso", "jp_kanji": "敬意を払う", "romaji": "keii o harau"},
    6: {"es": "generoso", "jp_kanji": "寛大な", "romaji": "kandai na"},
    7: {"es": "curioso", "jp_kanji": "好奇心旺盛な", "romaji": "kōkishin ōseina"},
    8: {"es": "sociable", "jp_kanji": "社交的な", "romaji": "shakōteki na"},
    9: {"es": "tímido", "jp_kanji": "内気な", "romaji": "uchiki na"},
    10: {"es": "imprudente", "jp_kanji": "軽率な", "romaji": "keisotsu na"},
    11: {"es": "falso", "jp_kanji": "偽りの", "romaji": "itsuwari no"},
    12: {"es": "arrogante", "jp_kanji": "傲慢な", "romaji": "gōman na"},
    13: {"es": "presumido", "jp_kanji": "うぬぼれた", "romaji": "unuboreta"},
    14: {"es": "egoísta", "jp_kanji": "利己的な", "romaji": "rikoteki na"},
    15: {"es": "tranquilo", "jp_kanji": "落ち着いた", "romaji": "ochitsuita"},
    16: {"es": "apático", "jp_kanji": "無関心な", "romaji": "mukanshin na"}
}

# 8. Dimensión Facilidad-Dificultad
dimension_facilidad_dificultad = {
    1: {"es": "imposible", "jp_kanji": "不可能な", "romaji": "fukanō na"},
    2: {"es": "arduo", "jp_kanji": "骨の折れる", "romaji": "hone no oreru"},
    3: {"es": "complicado", "jp_kanji": "複雑な", "romaji": "fukuzatsu na"},
    4: {"es": "difícil", "jp_kanji": "難しい", "romaji": "muzukashii"},
    5: {"es": "problemático", "jp_kanji": "問題のある", "romaji": "mondai no aru"},
    6: {"es": "tedioso", "jp_kanji": "退屈な", "romaji": "taikutsu na"},
    7: {"es": "engorroso", "jp_kanji": "面倒な", "romaji": "mendō na"},
    8: {"es": "manejable", "jp_kanji": "扱いやすい", "romaji": "atsukai yasui"},
    9: {"es": "accesible", "jp_kanji": "アクセス可能な", "romaji": "akusesu kanō na"},
    10: {"es": "simple", "jp_kanji": "簡単な", "romaji": "kantan na"},
    11: {"es": "fácil", "jp_kanji": "易しい", "romaji": "yasashii"},
    12: {"es": "claro", "jp_kanji": "明確な", "romaji": "meikaku na"},
    13: {"es": "ligero", "jp_kanji": "軽い", "romaji": "karui"},
    14: {"es": "sencillo", "jp_kanji": "単純な", "romaji": "tanjun na"},
    15: {"es": "rápido", "jp_kanji": "速い", "romaji": "hayai"},
    16: {"es": "evidente", "jp_kanji": "明白な", "romaji": "meihaku na"}
}

# 9. Dimensión Emoción-Sentimiento
dimension_emocion_sentimiento = {
    1: {"es": "devastado", "jp_kanji": "打ちひしがれた", "romaji": "uchihishigareta"},
    2: {"es": "deprimido", "jp_kanji": "落ち込んだ", "romaji": "ochikonda"},
    3: {"es": "triste", "jp_kanji": "悲しい", "romaji": "kanashii"},
    4: {"es": "pesimista", "jp_kanji": "悲観的な", "romaji": "hikanteki na"},
    5: {"es": "ansioso", "jp_kanji": "不安な", "romaji": "fuan na"},
    6: {"es": "nervioso", "jp_kanji": "緊張した", "romaji": "kinchō shita"},
    7: {"es": "preocupado", "jp_kanji": "心配した", "romaji": "shinpai shita"},
    8: {"es": "neutral", "jp_kanji": "中立的な", "romaji": "chūritsuteki na"},
    9: {"es": "contento", "jp_kanji": "満足した", "romaji": "manzoku shita"},
    10: {"es": "tranquilo", "jp_kanji": "落ち着いた", "romaji": "ochitsuita"},
    11: {"es": "positivo", "jp_kanji": "前向きな", "romaji": "maemuki na"},
    12: {"es": "relajado", "jp_kanji": "リラックスした", "romaji": "rirakkusu shita"},
    13: {"es": "feliz", "jp_kanji": "幸せな", "romaji": "shiawase na"},
    14: {"es": "entusiasmado", "jp_kanji": "熱狂的な", "romaji": "nekkyōteki na"},
    15: {"es": "emocionado", "jp_kanji": "興奮した", "romaji": "kōfun shita"},
    16: {"es": "extasiado", "jp_kanji": "恍惚とした", "romaji": "kōkotsu to shita"}
}

# 10. Dimensión Justicia-Moral
dimension_justicia_moral = {
    1: {"es": "cruel", "jp_kanji": "残酷な", "romaji": "zankoku na"},
    2: {"es": "injusto", "jp_kanji": "不公平な", "romaji": "fukōhei na"},
    3: {"es": "infiel", "jp_kanji": "不誠実な", "romaji": "fuseijitsu na"},
    4: {"es": "deshonesto", "jp_kanji": "不正直な", "romaji": "fushōjiki na"},
    5: {"es": "irresponsable", "jp_kanji": "無責任な", "romaji": "musekinin na"},
    6: {"es": "incorrecto", "jp_kanji": "不適切な", "romaji": "futekisetsu na"},
    7: {"es": "deshonroso", "jp_kanji": "不名誉な", "romaji": "fumeiyo na"},
    8: {"es": "neutral", "jp_kanji": "中立的な", "romaji": "chūritsuteki na"},
    9: {"es": "responsable", "jp_kanji": "責任感のある", "romaji": "sekininkan no aru"},
    10: {"es": "fiel", "jp_kanji": "忠実な", "romaji": "chūjitsu na"},
    11: {"es": "honesto", "jp_kanji": "正直な", "romaji": "shōjiki na"},
    12: {"es": "ético", "jp_kanji": "倫理的な", "romaji": "rinriteki na"},
    13: {"es": "correcto", "jp_kanji": "正しい", "romaji": "tadashii"},
    14: {"es": "justo", "jp_kanji": "公正な", "romaji": "kōsei na"},
    15: {"es": "honorable", "jp_kanji": "名誉ある", "romaji": "meiyo aru"},
    16: {"es": "virtuoso", "jp_kanji": "徳の高い", "romaji": "toku no takai"}
}

# 11. Dimensión Personalidad-Carácter
dimension_personalidad_caracter = {
    1: {"es": "abusivo", "jp_kanji": "虐待的な", "romaji": "gyakutai teki na"},
    2: {"es": "grosero", "jp_kanji": "無礼な", "romaji": "burei na"},
    3: {"es": "egocéntrico", "jp_kanji": "自己中心的な", "romaji": "jikochūshinteki na"},
    4: {"es": "imprudente", "jp_kanji": "軽率な", "romaji": "keisotsu na"},
    5: {"es": "aburrido", "jp_kanji": "退屈な", "romaji": "taikutsu na"},
    6: {"es": "falso", "jp_kanji": "偽りの", "romaji": "itsuwari no"},
    7: {"es": "descortés", "jp_kanji": "無礼な", "romaji": "burei na"},
    8: {"es": "neutro", "jp_kanji": "中立的な", "romaji": "chūritsuteki na"},
    9: {"es": "curioso", "jp_kanji": "好奇心旺盛な", "romaji": "kōkishin ōseina"},
    10: {"es": "prudente", "jp_kanji": "慎重な", "romaji": "shinchō na"},
    11: {"es": "tímido", "jp_kanji": "内気な", "romaji": "uchiki na"},
    12: {"es": "amable", "jp_kanji": "親切な", "romaji": "shinsetsu na"},
    13: {"es": "sociable", "jp_kanji": "社交的な", "romaji": "shakōteki na"},
    14: {"es": "entusiasta", "jp_kanji": "熱心な", "romaji": "nesshin na"},
    15: {"es": "respetuoso", "jp_kanji": "敬意を払う", "romaji": "keii o harau"},
    16: {"es": "altruista", "jp_kanji": "利他的な", "romaji": "ritateki na"}
}

# 12. Dimensión Costo-Monetario
dimension_costo_monetario = {
    1: {"es": "exorbitante", "jp_kanji": "法外な", "romaji": "hōgai na"},
    2: {"es": "caro", "jp_kanji": "高価な", "romaji": "kōka na"},
    3: {"es": "costoso", "jp_kanji": "高価な", "romaji": "kōka na"},
    4: {"es": "valioso", "jp_kanji": "価値のある", "romaji": "kachi no aru"},
    5: {"es": "lujoso", "jp_kanji": "豪華な", "romaji": "gōka na"},
    6: {"es": "exclusivo", "jp_kanji": "排他的な", "romaji": "haitateki na"},
    7: {"es": "elevado", "jp_kanji": "高い", "romaji": "takai"},
    8: {"es": "neutro", "jp_kanji": "中立的な", "romaji": "chūritsuteki na"},
    9: {"es": "asequible", "jp_kanji": "手頃な", "romaji": "tegoro na"},
    10: {"es": "económico", "jp_kanji": "経済的な", "romaji": "keizaiteki na"},
    11: {"es": "barato", "jp_kanji": "安い", "romaji": "yasui"},
    12: {"es": "accesible", "jp_kanji": "アクセス可能な", "romaji": "akusesu kanō na"},
    13: {"es": "gratis", "jp_kanji": "無料の", "romaji": "muryō no"},
    14: {"es": "mínimo", "jp_kanji": "最小の", "romaji": "saishō no"},
    15: {"es": "simbólico", "jp_kanji": "象徴的な", "romaji": "shōchōteki na"},
    16: {"es": "donativo", "jp_kanji": "寄付の", "romaji": "kifu no"}
}

# 13. Dimensión Esfuerzo
dimension_esfuerzo = {
    1: {"es": "agotador", "jp_kanji": "疲れる", "romaji": "tsukareru"},
    2: {"es": "intenso", "jp_kanji": "激しい", "romaji": "hageshii"},
    3: {"es": "duro", "jp_kanji": "厳しい", "romaji": "kibishii"},
    4: {"es": "cansado", "jp_kanji": "疲れた", "romaji": "tsukareta"},
    5: {"es": "esforzado", "jp_kanji": "努力した", "romaji": "doryoku shita"},
    6: {"es": "complicado", "jp_kanji": "複雑な", "romaji": "fukuzatsu na"},
    7: {"es": "exigente", "jp_kanji": "要求の多い", "romaji": "yōkyū no ōi"},
    8: {"es": "moderado", "jp_kanji": "適度な", "romaji": "tekido na"},
    9: {"es": "manejable", "jp_kanji": "扱いやすい", "romaji": "atsukai yasui"},
    10: {"es": "asequible", "jp_kanji": "手頃な", "romaji": "tegoro na"},
    11: {"es": "suave", "jp_kanji": "穏やかな", "romaji": "odayaka na"},
    12: {"es": "sencillo", "jp_kanji": "簡単な", "romaji": "kantan na"},
    13: {"es": "fácil", "jp_kanji": "易しい", "romaji": "yasashii"},
    14: {"es": "ligero", "jp_kanji": "軽い", "romaji": "karui"},
    15: {"es": "trivial", "jp_kanji": "些細な", "romaji": "sasai na"},
    16: {"es": "sin esfuerzo", "jp_kanji": "努力なしの", "romaji": "doryoku nashi no"}
}

# 14. Dimensión Temperatura
dimension_temperatura = {
    1: {"es": "helado", "jp_kanji": "氷のような", "romaji": "kōri no yō na"},
    2: {"es": "frío", "jp_kanji": "冷たい", "romaji": "tsumetai"},
    3: {"es": "templado", "jp_kanji": "温暖な", "romaji": "ondan na"},
    4: {"es": "cálido", "jp_kanji": "暖かい", "romaji": "atatakai"},
    5: {"es": "caliente", "jp_kanji": "熱い", "romaji": "atsui"},
    6: {"es": "abrasador", "jp_kanji": "焼けつくような", "romaji": "yaketsuku yō na"}
}

# 15. Dimensión Intensidad
dimension_intensidad = {
    1: {"es": "débil", "jp_kanji": "弱い", "romaji": "yowai"},
    2: {"es": "suave", "jp_kanji": "穏やかな", "romaji": "odayaka na"},
    3: {"es": "moderado", "jp_kanji": "適度な", "romaji": "tekido na"},
    4: {"es": "fuerte", "jp_kanji": "強い", "romaji": "tsuyoi"},
    5: {"es": "intenso", "jp_kanji": "激しい", "romaji": "hageshii"},
    6: {"es": "extremo", "jp_kanji": "極端な", "romaji": "kyokutan na"}
}

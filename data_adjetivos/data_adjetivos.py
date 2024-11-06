#data_adjetivos.py


# 1. Dimensión Tamaño
dimension_tamaño = {
    1: "diminuto",       # 1: Muy pequeño
    2: "minúsculo",     # 2: Extremadamente pequeño
    3: "pequeño",       # 3: De tamaño reducido
    4: "corto",         # 4: Distancia o longitud breve
    5: "estrecho",      # 5: Espacio reducido en ancho
    6: "bajo",          # 6: Altura reducida
    7: "largo",         # 7: Gran longitud
    8: "alto",          # 8: Gran altura
    9: "ancho",         # 9: Amplio, de gran extensión
    10: "grande",       # 10: De tamaño considerable
    11: "voluminoso",   # 11: Que ocupa mucho espacio
    12: "enorme",       # 12: Muy grande
    13: "colosal",      # 13: Gigantesco
    14: "gigante",      # 14: Muy grande
    15: "masivo",       # 15: Gran volumen y peso
    16: "monstruoso"    # 16: Extremadamente grande
}

# 2. Dimensión Peso
dimension_peso = {
    1: "ligero",        # 1: Poco peso
    2: "liviano",       # 2: Muy poco peso
    3: "compacto",      # 3: Peso en poco volumen
    4: "denso",         # 4: Gran concentración de masa
    5: "pesado",        # 5: Gran peso
    6: "colosal",       # 6: Muy pesado
    7: "masivo",        # 7: Gran peso y tamaño
    8: "opulento",      # 8: Lujoso y pesado
}

# 3. Dimensión Edad
dimension_edad = {
    1: "nuevo",         # 1: Reciente
    2: "joven",         # 2: En sus primeros años
    3: "reciente",      # 3: Muy reciente
    4: "moderno",       # 4: Actual y contemporáneo
    5: "actual",        # 5: Que ocurre ahora
    6: "vigente",       # 6: Aceptado y utilizado en el presente
    7: "viejo",         # 7: Con muchos años
    8: "antiguo",       # 8: De épocas pasadas
    9: "pasado",        # 9: Que ya no es presente
    10: "histórico",    # 10: Relacionado con la historia
    11: "perenne",      # 11: Duradero, que persiste
    12: "eterno",       # 12: Sin fin
    13: "anacrónico",   # 13: Fuera de su tiempo
    14: "obsoleto",     # 14: Ya no útil
    15: "desfasado",    # 15: Fuera de moda
    16: "caducado"      # 16: Que ha expirado
}

# 4. Dimensión Velocidad
dimension_velocidad = {
    1: "lento",         # 1: Velocidad baja
    2: "perezoso",      # 2: Falta de energía
    3: "torpe",         # 3: Movimiento ineficaz
    4: "tardo",         # 4: Muy lento
    5: "despacio",      # 5: Con lentitud
    6: "pausado",       # 6: Movimiento con interrupciones
    7: "tranquilo",     # 7: Sin prisa
    8: "estático",      # 8: Sin movimiento
    9: "constante",     # 9: Sin cambios en la velocidad
    10: "rápido",       # 10: Con velocidad alta
    11: "ágil",         # 11: Rápido y flexible
    12: "dinámico",     # 12: Activo, en movimiento
    13: "acelerado",    # 13: Incrementando la velocidad
    14: "implacable",   # 14: Sin pausa, imparable
    15: "inmóvil",      # 15: Sin movimiento
    16: "retardado"     # 16: Moviéndose lentamente
}

# 5. Dimensión Estado
dimension_estado = {
    1: "sano",          # 1: En buena salud
    2: "limpio",        # 2: Sin suciedad
    3: "fresco",        # 3: Reciente, nuevo
    4: "intacto",       # 4: Sin daños
    5: "robusto",       # 5: Fuerte
    6: "vacío",         # 6: Sin contenido
    7: "lleno",         # 7: Con contenido
    8: "caliente",      # 8: Alta temperatura
    9: "frío",          # 9: Baja temperatura
    10: "sucio",        # 10: Con suciedad
    11: "enfermo",      # 11: Con problemas de salud
    12: "vivo",         # 12: Con vida
    13: "muerto",       # 13: Sin vida
    14: "frágil",       # 14: Fácil de romper
    15: "dañado",       # 15: Con defectos
    16: "perjudicado"   # 16: Afectado negativamente
}


# 6. Dimensión Belleza Estética
dimension_belleza_estetica = {
    1: "repulsivo",      # 1: Que provoca aversión
    2: "tétrico",        # 2: Que causa temor
    3: "horrible",       # 3: Muy poco atractivo
    4: "feo",            # 4: No atractivo
    5: "desagradable",   # 5: Poco atractivo
    6: "vulgar",         # 6: De mal gusto
    7: "apagado",        # 7: Sin brillo
    8: "neutro",         # 8: Ni feo ni bonito
    9: "sutil",          # 9: Elegante, pero discreto
    10: "brillante",     # 10: Con luz intensa
    11: "bonito",        # 11: Atractivo moderado
    12: "lindo",         # 12: Agradable a la vista
    13: "atractivo",     # 13: Que llama la atención
    14: "elegante",      # 14: Con estilo y gracia
    15: "hermoso",       # 15: Muy atractivo
    16: "espléndido"     # 16: De gran belleza y perfección
}



# 7. Dimensión Personalidad
dimension_personalidad = {
    1: "sincero",       # 1: Genuino
    2: "amable",        # 2: Amistoso
    3: "entusiasta",    # 3: Con energía
    4: "prudente",      # 4: Cauteloso
    5: "respetuoso",    # 5: Considerado
    6: "generoso",      # 6: Dispuesto a dar
    7: "curioso",       # 7: Deseo de aprender
    8: "sociable",      # 8: Que disfruta la compañía
    9: "tímido",        # 9: Reservado
    10: "imprudente",   # 10: Falta de precaución
    11: "falso",        # 11: No genuino
    12: "arrogante",    # 12: Demasiado orgulloso
    13: "presumido",    # 13: Que se cree superior
    14: "egoísta",      # 14: Que solo se preocupa por sí mismo
    15: "tranquilo",     # 15: Serene
    16: "apático"       # 16: Sin interés
}


# 8. Dimensión Facilidad-Dificultad
dimension_facilidad_dificultad = {
    1: "imposible",     # 1: Extremadamente difícil o inalcanzable
    2: "arduo",         # 2: Requiere mucho esfuerzo
    3: "complicado",    # 3: Dificultad alta
    4: "difícil",       # 4: Que demanda esfuerzo
    5: "problemático",  # 5: Con obstáculos o desafíos
    6: "tedioso",       # 6: Repetitivo y cansador
    7: "engorroso",     # 7: Algo molesto
    8: "manejable",     # 8: Puede controlarse
    9: "accesible",     # 9: Fácil de lograr
    10: "simple",       # 10: Sin complicaciones
    11: "fácil",        # 11: Poco esfuerzo requerido
    12: "claro",        # 12: Fácil de entender
    13: "ligero",       # 13: Sin peso emocional o mental
    14: "sencillo",     # 14: Sin obstáculos
    15: "rápido",       # 15: Requiere poco tiempo
    16: "evidente"      # 16: Muy claro y fácil de lograr
}

# 9. Dimensión Emoción-Sentimiento
dimension_emocion_sentimiento = {
    1: "devastado",     # 1: En extremo emocional negativo
    2: "deprimido",     # 2: Muy triste
    3: "triste",        # 3: Sin alegría
    4: "pesimista",     # 4: Sin esperanza
    5: "ansioso",       # 5: Inquietud emocional
    6: "nervioso",      # 6: Con tensión
    7: "preocupado",    # 7: Intranquilo
    8: "neutral",       # 8: Sin emociones fuertes
    9: "contento",      # 9: Con satisfacción
    10: "tranquilo",    # 10: Relajado
    11: "positivo",     # 11: Optimismo
    12: "relajado",     # 12: En calma
    13: "feliz",        # 13: Emoción positiva
    14: "entusiasmado", # 14: Con gran interés
    15: "emocionado",   # 15: Emoción muy positiva
    16: "extasiado"     # 16: Emoción máxima positiva
}

# 10. Dimensión Justicia-Moral
dimension_justicia_moral = {
    1: "cruel",         # 1: Falta de moralidad extrema
    2: "injusto",       # 2: Falta de justicia
    3: "infiel",        # 3: Desleal
    4: "deshonesto",    # 4: Sin honestidad
    5: "irresponsable", # 5: Que no cumple con deberes
    6: "incorrecto",    # 6: Fuera de ética
    7: "deshonroso",    # 7: Que no merece honor
    8: "neutral",       # 8: Sin inclinación ética
    9: "responsable",   # 9: Cumple deberes
    10: "fiel",         # 10: Con lealtad
    11: "honesto",      # 11: Con sinceridad
    12: "ético",        # 12: Actúa conforme a principios
    13: "correcto",     # 13: Actitud moral
    14: "justo",        # 14: Con apego a la justicia
    15: "honorable",    # 15: Merecedor de honor
    16: "virtuoso"      # 16: Que cumple valores morales altos
}

# 11. Dimensión Personalidad-Carácter
dimension_personalidad_caracter = {
    1: "abusivo",       # 1: Extremadamente negativo en carácter
    2: "grosero",       # 2: Malos modales
    3: "egocéntrico",   # 3: Solo enfocado en sí mismo
    4: "imprudente",    # 4: Falta de precaución
    5: "aburrido",      # 5: Falta de interés
    6: "falso",         # 6: Sin sinceridad
    7: "descortés",     # 7: Falta de cortesía
    8: "neutro",        # 8: Carácter equilibrado
    9: "curioso",       # 9: Deseo de saber
    10: "prudente",     # 10: Actúa con cautela
    11: "tímido",       # 11: Reservado
    12: "amable",       # 12: Trata bien a los demás
    13: "sociable",     # 13: Se relaciona bien
    14: "entusiasta",   # 14: Con energía positiva
    15: "respetuoso",   # 15: Con respeto a los demás
    16: "altruista"     # 16: Muy orientado a ayudar
}

# 12. Dimensión Costo-Monetario
dimension_costo_monetario = {
    1: "exorbitante",   # 1: Coste extremadamente alto
    2: "caro",          # 2: Precio alto
    3: "costoso",       # 3: Con costo significativo
    4: "valioso",       # 4: De valor, aunque caro
    5: "lujoso",        # 5: Coste elevado por calidad
    6: "exclusivo",     # 6: Solo para algunos
    7: "elevado",       # 7: Coste alto, pero no extremo
    8: "neutro",        # 8: Precio moderado
    9: "asequible",     # 9: Precio que puede pagarse
    10: "económico",    # 10: Bajo costo
    11: "barato",       # 11: Muy bajo en precio
    12: "accesible",    # 12: A un precio razonable
    13: "gratis",       # 13: Sin costo
    14: "mínimo",       # 14: Costo muy bajo
    15: "simbólico",    # 15: Casi sin costo
    16: "donativo"      # 16: Costo nulo, dado como ayuda
}

# 13. Dimensión Esfuerzo
dimension_esfuerzo = {
    1: "agotador",      # 1: Extremadamente demandante
    2: "intenso",       # 2: Requiere mucho esfuerzo
    3: "duro",          # 3: Muy exigente
    4: "cansado",       # 4: Que causa fatiga
    5: "esforzado",     # 5: Con trabajo y dedicación
    6: "complicado",    # 6: Exige concentración
    7: "exigente",      # 7: Requiere mucho
    8: "moderado",      # 8: Esfuerzo medio
    9: "manejable",     # 9: Puede gestionarse
    10: "asequible",    # 10: Requiere poco esfuerzo
    11: "suave",        # 11: Muy poco esfuerzo
    12: "sencillo",     # 12: Sin gran esfuerzo
    13: "fácil",        # 13: Poco exigente
    14: "ligero",       # 14: Muy fácil
    15: "trivial",      # 15: Insignificante
    16: "sin esfuerzo"  # 16: No requiere esfuerzo alguno
}

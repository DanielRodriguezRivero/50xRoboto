init:
    $ hola =0
    
label uno:
    show melee at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "En lo profundo del caribe..."
    menu:
        "Rijkaard fumando hierba":
            $ puntos+=3
            $ renpy.sound.play("acierto.wav") 
            r "Queda archivada tu respuesta"
        "Ron Bacardi":
            r "Queda archivada tu respuesta"
        "La isla de Melee":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "El caribe profundo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide melee
    jump cuestion
    
label dos:
    $ preguntas += 1
    show sophie at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿De qué pais es originaria Sophie Evans?"
    menu:
        "Tia buenorria":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Guarrilandia":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Mamadocia":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "España":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide sophie
    jump cuestion
    
label tres:
    show lezley at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿En qué está especializada Lezley Zen?"
    menu:
        "Derecho":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Matemáticas":
            r "Queda archivada tu respuesta"
        "Biologia":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Francés":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide lezley
    jump cuestion
    
label cuatro:
    show serrano at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿De que iba Los Serrano antes de convertirse en una excusa para ver los senos de Teté (mayor de edad por cierto)?"
    menu:
        "De ver los senos de Belén Rueda":
            r "Queda archivada tu respuesta"
        "De ver a Jesús Bonilla gritar":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "De ver a Resines haciendo el garrulo (como en todas sus actuaciones)":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "De intuir los senos de la hermana de Teté":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide serrano
    jump cuestion
    
label cinco:
    show kate at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Cual es la bebida favorita de Kate Moss?"
    menu:
        "Coca cola":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Coca light":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Pepsi Coca":
            r "Queda archivada tu respuesta"
        "La coca a palo seco":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide kate
    jump cuestion
    
label seis:
    show musica at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    $ renpy.sound.play("bso1.mp3", 1,1)
    r "¿A qué juego pertenece esta canción?"
    menu:
        "Nonamed":
            r "Queda archivada tu respuesta"
        "Rescate Atlantida":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Navy Moves":
            r "Queda archivada tu respuesta"
        "Dustin":
            r "Queda archivada tu respuesta"
    hide musica
    $ renpy.sound.stop(1,1)
    jump cuestion
    
label siete:
    show musica at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ renpy.play("doraemon.mp3")
    p "Despues de escuchar esta canción de Oliver Onions, cómo lo definirias..."
    $ preguntas += 1
    menu:
        "Vago":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Listo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Enterao":
            r "Queda archivada tu respuesta"
        "Copypastero":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide musica
    $ renpy.sound.stop(0,2)
    jump cuestion
    
label ocho:
    show lutero at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Qué hizo Lutero cuando se encontró al diablo en su habitación?"
    menu:
        "Le tiró el tintero para ver si era un fantasma":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Escribió una hoja de reclamaciones a Dios":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Se enfado mucho":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Le ordenó que soltara su ropa interior de inmediato":
            r "Queda archivada tu respuesta"
    hide lutero
    jump cuestion
    
label nueve:
    show desperate at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Por qué están desesperadas las chicas de Wysteria Lane?"
    menu:
        "El consolador se le quedó sin pilas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "No tienen crédito en la VISA":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Son maniaco-depresivas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Quieren tirarse al jardinero y no saben como":
            r "Queda archivada tu respuesta"
    hide desperate
    jump cuestion
    
label diez:
    show armada at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Qué fue la armada invencible?"
    menu:
        "Un ejemplo fallido de marketing":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Un grupo de tenistas":
            r "Queda archivada tu respuesta"
        "La oportunidad perfecta para acabar con el fish´n´chip":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Un grupo de barcos a los que les pillo una tormenta":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide armada
    jump cuestion
    
label once:
    show caballeros at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Cual de los siguientes caballeros del zodiaco no es gay?"
    menu:
        "Misty":
            r "Extraño juego, la única manera de ganar es no jugar"
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Shun":
            r "Extraño juego, la única manera de ganar es no jugar"
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Hyoga":
            $ renpy.sound.play("acierto.wav")             
            r "Extraño juego, la única manera de ganar es no jugar"
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Afrodita":
            $ renpy.sound.play("acierto.wav")             
            r "Extraño juego, la única manera de ganar es no jugar"
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide caballeros
    jump cuestion
    
label doce:
    show jenna at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual era la profesión de Jenna Jameson antes de ser actriz porno?"
    $ preguntas += 1
    menu:
        "Monja":
            r "Queda archivada tu respuesta"
        "Catequista":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Profesora de lógica difusa":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Stripper":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide jenna
    jump cuestion
    
label trece:
    show queen at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Quien es el bateria de Queen"
    menu:
        "Charlie Watts":
            r "Queda archivada tu respuesta"
        "Lars Ulrich":
            r "Queda archivada tu respuesta"
        "John Deacon":
            r "Queda archivada tu respuesta"
        "Roger Taylor":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide queen
    jump cuestion
    
label catorce:
    r "¿Quien desentona en esta lista?"
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    menu:
        "Joselito":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Efectivamente, es el único que no agarra algo grande entre sus manos al despertarse"
            r "Queda archivada tu respuesta"
        "Nacho Vidal":
            r "Queda archivada tu respuesta"
        "Gandalf el Mago":
            r "Queda archivada tu respuesta"
        "Harry El Sucio":
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label quince:
    show spirit at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Quién fue el creador de {b}The Spirit{/b}?"
    menu:
        "Will Eisner":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Jack Kirby":
            r "Queda archivada tu respuesta"
        "Alan Moore":
            r "Queda archivada tu respuesta"
        "Hugo Pratt":
            r "Queda archivada tu respuesta"
    hide spirit
    jump cuestion
    
label dieciseis:
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "Nobody expects..."
    menu:
        "Otro chiste de los Monty Python":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "nothing":
            r "Queda archivada tu respuesta"
        "Que el atleti gane la Champions":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "The Spanish Inquisition":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion

label diecisiete:
    show tortugas at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Quién era el maestro de Las Tortugas Ninja?"
    menu:
        "El Sr Miyagui":
            r "Queda archivada tu respuesta"
        "Shredder":
            r "Queda archivada tu respuesta"
        "Karate Kimura":
            r "Queda archivada tu respuesta"
        "Splinter":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide tortugas
    jump cuestion
    
label dieciocho:
    show goro at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "Goro es..."
    menu:
        "Diestro":
            r "Queda archivada tu respuesta"
        "Zurdo":
            r "Queda archivada tu respuesta"
        "Ambidiestro":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Onanista":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide goro
    jump cuestion
    
label diecinueve:
    show bobobo at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    $ bobobo=("Nombre del personaje que ataca con su cabello nasal:")
    if bobobo=="Bobobo" or bobobo=="bobobo" or bobobo=="Bobobó" or boboo=="bobobó":
        $ puntos+=3
        r "¡¡Acertaste!!"
    else:
        r "Intentalo en otra ocasión"
    hide bobobo
    jump cuestion
    
label veinte:
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien escribió {b}Crimen y Castigo{/b}?"
    $ preguntas += 1
    menu:
        "Juan Antonio Roca":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Mario Conde":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Mr X":
            r "Queda archivada tu respuesta"
        "Los Albertos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label ventiuno:
    show super at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Para qué consola se desarrolló esta versión de Superman?"
    menu:
        "Vectrex":
            r "Queda archivada tu respuesta"
        "Atari 7800":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Atari 2600":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Odyssey":
            r "Queda archivada tu respuesta"
    hide super
    jump cuestion
    
label ventidos:
    show wally at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Donde está Wally?"
    menu:
        "Tras la pista de Bin Laden":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "En el Zara del pueblo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Muerto":
            r "Queda archivada tu respuesta"
        "Espiando a Carmen Sandiego por la ventana":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide wally
    jump cuestion
    
label ventitres:
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿De quién huia Vazquez?"
    menu:
        "De la inquisición española":
            r "Queda archivada tu respuesta"
        "De los grises":
            r "Queda archivada tu respuesta"
        "De su mujer":
            r "Queda archivada tu respuesta"
        "De sus acreedores":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label venticuatro:
    show kryten at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿En qué serie aparecia este personaje?"
    menu:
        "Dr Who":
            r "Queda archivada tu respuesta"
        "La casa de Bernarda Alba":
            r "Queda archivada tu respuesta"
        "Enano Rojo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Star trek (en una de sus múltiples versiones)":
            r "Queda archivada tu respuesta"
    hide kryten
    jump cuestion
    
label venticinco:
    show elvis at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Qué dijo Elvis antes de morir?"
    menu:
        "Rosebud":
            r "Queda archivada tu respuesta"
        "No debi comerme ese donut":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Oh no, se me han caido los tripis a la taza del water":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Esta es la última pirula y lo dejo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide elvis
    jump cuestion
    
label ventiseis:
    show iglesias at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Por qué dejan seguir cantando a Julio Iglesias?"
    menu:
        "Porque lo hace fuera de España":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Porque forma parte de un plan para minar la moral de los americanos y recuperar Florida para la corona":
            r "Queda archivada tu respuesta"
        "Porque canta bien":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Por si la sequia amenaza el pais":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide iglesias
    jump cuestion
    
    
label ventisiete:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es el deporte de los reyes?"
    menu:
        "Golf":
            r "Queda archivada tu respuesta"
        "El fornicio":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Petanca":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Las Regatas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label ventiocho:
    $ preguntas += 1
    show kenshiro at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué hermano de Kenshiro se hacia pasar por él?"
    menu:
        "Toki":
            r "Queda archivada tu respuesta"
        "Jaggy":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Ryuken":
            r "Queda archivada tu respuesta"
        "Raoh":
            r "Queda archivada tu respuesta"
    hide kenshiro
    jump cuestion
    
label ventinueve:
    $ preguntas += 1
    show wonderwoman at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Actriz que interpretó a Wonder Woman en la serie de televisión"
    menu:
        "Samantha Rogers":
            r "Queda archivada tu respuesta"
        "Lynda Carter":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Lee Mariweather":
            r "Queda archivada tu respuesta"
        "Cathy Lee Crosby":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide wonderwoman
    jump cuestion
    
label treinta:
    $ preguntas += 1
    show brasil at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué se dice de las brasileñas?"
    menu:
        "Que no tienen pelo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Que son de Brasil":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Maravillas":
            r "Queda archivada tu respuesta"
        "De todo, pero ellas no dicen nada porque se lo meten entero en la boca":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide brasil
    jump cuestion
    
label treintayuno:
    show segis at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "Profesión de Segis y Olivio"
    menu:
        "Vagabundos":
            r "Queda archivada tu respuesta"
        "Politicos":
            r "Queda archivada tu respuesta"
        "Traperos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Agentes secretos":
            r "Queda archivada tu respuesta"
    hide segis
    jump cuestion
    
label treintaydos:
    $ preguntas += 1
    show asterix at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué galo de la aldea de Asterix tenia a la esposa más buenorra?"
    menu:
        "Empalmadix":
            r "Queda archivada tu respuesta"
        "Condonix":
            r "Queda archivada tu respuesta"
        "Agotadix":
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Edadepiedrix":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide asterix
    jump cuestion
    
label treintaytres:
    $ preguntas += 1
    show chuck at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Cuando los criminales ven a Chuck Norris..."
    menu:
        "Se rinden de inmediato":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Se dan cuenta de que hace tiempo que han muerto":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "le piden un autografo":
            r "Queda archivada tu respuesta"
        "se vuelan la cabeza para no sufrir":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide chuck
    jump cuestion
    
label treintaycuatro:
    $ preguntas += 1
    show china at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué los restaurantes chinos están siempre vacios y sin embargo nunca quiebran?"
    menu:
        "El gobierno los mantiene por su labor social con los animales abandonados":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Porque estafan a hacienda":
            r "Queda archivada tu respuesta"
        "Los chinos son tapaderas de Lo Pang":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "En realidad no son restaurantes sino pisos patera de 5 estrellas para sus congeneres":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide china
    jump cuestion
    
label tcinco:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Tiene usted pelos en la lengua?"
    menu:
        "No, pero me gustaria tenerlos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Y en el c... tambien tengo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Hola Pepe, me encanta tu programa":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Si, y los aguanto con redecilla":
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label tseis:
    $ preguntas += 1
    show rocky at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué grita Rocky al final de Rocky I?"
    menu:
        "Auxilio":
            r "Queda archivada tu respuesta"
        "Adrian":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Aleluya":
            r "Queda archivada tu respuesta"
        "A mi la legión":
            r "Queda archivada tu respuesta"
    hide rocky
    jump cuestion
    
label tsiete:
    $ preguntas += 1
    show duke at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien es este personaje?"
    menu:
        "George Bush":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Woody Allen cuando duerme la siesta":
            r "Queda archivada tu respuesta"
        "Duke Nukem":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Schwarzenegger de joven":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide duke
    jump cuestion
    
label tocho:
    $ preguntas += 1
    show salto at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué pretende hacerle este hombre al toro?"
    menu:
        "Saltarlo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Enseñarle a nadar":
            r "Queda archivada tu respuesta"
        "El salto del tigre":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Rozarle el lomo (sin manos)":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide salto
    jump cuestion
    
label tnueve:
    $ preguntas += 1
    show goku at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Perro es a gato lo que Goku es a..."
    menu:
        "Un champú acondicionador":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Freezer":
            r "Queda archivada tu respuesta"
        "Un peine":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Chichi":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide goku
    jump cuestion
    
label cuarenta:
    $ preguntas += 1
    show torre at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual era la torre equivalente, en la parodia \"Fin del juego, año dos y pico\"?"
    menu:
        "La torre del oro":
            r "Queda archivada tu respuesta"
        "La torre de Hercules":
            r "Queda archivada tu respuesta"
        "La torre de Nacho Vidal":
            r "Queda archivada tu respuesta"
        "La torre de Gofre":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide torre
    jump cuestion
    
label cuno:
    $ preguntas += 1
    show  interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien es la mujer más bella del universo?"
    menu:
        "Mi novia":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Mi mujer":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "A la que me estoy tirando ahora":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Mi suegra":
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label cdos:
    $ preguntas += 1
    show enterprise at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es el combustible del U.S.S. Enterprise?"
    menu:
        "Gasoleo 98 octanos":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Generador de fusión portatil":
            r "Queda archivada tu respuesta"
        "El ego de William Shatner":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Carbón":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            $ renpy.sound.play("acierto.wav")
            r "Queda archivada tu respuesta"
    hide enterprise
    jump cuestion
    
label ctres:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Nombre del suplemento de la revista Super Juegos que mostraba las fotos de las japonesas más horrendas"
    menu:
        "Mangamania":
            r "Queda archivada tu respuesta"
        "Freak in Japan":
            r "Queda archivada tu respuesta"
        "JapanMania":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Suicide Girls":
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label ccuatro:
    $ preguntas += 1
    show china at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es el deporte nacional chino?"
    menu:
        "Apalear tibetanos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Amenazar a Taiwan":
            r "Queda archivada tu respuesta"
        "Explotar a los trabajadores":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "El fútbol":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide china
    jump cuestion
    
label ccinco:
    $ preguntas += 1
    show navy at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quién ilustró la caratula de Navy Moves?"
    menu:
        "Alfonso Azpiri":
            r "Queda archivada tu respuesta"
        "Boris Vallejo":
            r "Queda archivada tu respuesta"
        "Moebius":
            r "Queda archivada tu respuesta"
        "Luis Royo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide navy
    jump cuestion
    
label cseis:
    $ preguntas += 1
    show carmen at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Que es lo más valioso que ha robado Carmen Sandiego?"
    menu:
        "El rifle de Charlton Heston (ahora ya si)":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "La virginidad de Mr Roboto":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "La fama de Cybill Sheperd":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Las lentillas de Bono (el de U2)":
            r "Queda archivada tu respuesta"
    hide carmen
    jump cuestion
    
label csiete:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué pesa más?"
    menu:
        "Atención que tiene truco"
        "Un kilo de plomo":
            r "Queda archivada tu respuesta"
        "Dos kilos de plomo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Un kilo de Carlos Carnicero":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Tres kilos de plomo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label cocho:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quién escribio 20.000 leguas de viaje submarino?"
    menu:
        "Jacques Cousteau":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "El buzo de verano azul":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Flipper":
            r "Queda archivada tu respuesta"
        "Julio Verne":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label cnueve:
    $ preguntas += 1
    show alemania at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cómo se rien los alemanes?"
    menu:
        "Ju, ju, ju":
            r "Queda archivada tu respuesta"
        "hail, hail, hail":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "¿Reirse? ¿los alemanes?":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Ja, ja, ja (esto va con doble sentido)":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide alemania
    jump cuestion
    
label cincuenta:
    $ preguntas += 1
    show laurie at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué personaje interpretaba Hugh Laurie en esta foto?"
    menu:
        "Monseiur Pompidou":
            r "Queda archivada tu respuesta"
        "El principe regente":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Conde Von Papen":
            r "Queda archivada tu respuesta"
        "House en un mal día":
            r "Queda archivada tu respuesta"
    hide laurie
    jump cuestion
    
label ciuno:
    $ preguntas += 1
    show yoshi at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿En que juego apareció por primera vez Yoshi?"
    menu:
        "Super Mario Bros 3":
            r "Queda archivada tu respuesta"
        "Super Mario Kart":
            r "Queda archivada tu respuesta"
        "It´s just another super mario game":
            r "Queda archivada tu respuesta"
        "Super Mario World":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide yoshi
    jump cuestion
    
label cidos:
    $ preguntas += 1
    show melendi at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es el chocolate que más pone a Melendi?"
    menu:
        "Amargo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Paki":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Fondant":
            r "Queda archivada tu respuesta"
        "Xauen":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide melendi
    jump cuestion
    
label citres:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "En Benalmádena se casarond dos. Uno era macho y el otro..."
    menu:
        "Boris Izaguirre":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Hembra":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "La porra me sostenga"
            r "Queda archivada tu respuesta"
        "Una burra":
            r "Queda archivada tu respuesta"
        "Hermafrodita":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label cicuatro:
    $ preguntas += 1
    show mark at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Como lograba Mark Lenders agujerear las paredes con un balón?"
    menu:
        "Mark Lenders es un robot":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque mola tanto que puede hacer lo que quiera":
            r "Queda archivada tu respuesta"
        "No lo hacia, su padre iba detras con un pico":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Las paredes en japón están hechas de plastelina, por eso durante los terremotos no se caen los edificios":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide mark
    jump cuestion
    
label cicinco:
    $ preguntas += 1
    show kennedy at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quién mató a Kennedy?"
    menu:
        "Una dieta rica en grasas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Castro":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "La CIA":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "La factura de la peluqueria de Jacqueline Kennedy":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide kennedy
    jump cuestion
    
label ciseis:
    $ preguntas += 1
    show capitan at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué acompañaban Crispin y Goliath al Capitán Trueno, allá donde fuera este?"
    menu:
        "Porque les debia dinero":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque eran colegas de la mili":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Porque querian que les presentara a las hermanas gemelas de Sigrid":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Por simple atracción física":
            r "Queda archivada tu respuesta"
    hide capitan
    jump cuestion
    
label cisiete:
    $ preguntas += 1
    show anarosa at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Ana Rosa está..."
    menu:
        "Buena":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Muy buena":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Eres un degenerado":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "A mi me pone más la Estebam":
            r "Queda archivada tu respuesta"
    hide anarosa
    jump cuestion
    
label ciocho:
    $ preguntas += 1
    show argentina at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien tiene la culpa de la actual situación económica de Argentina?"
    menu:
        "Menem":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Esto, Menem":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "El boludo de Menem":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "La concha de la madre de Menem":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide argentina
    jump cuestion
    
label cinueve:
    $ preguntas += 1
    show heman at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Donatello es a Splinter lo que He-Man es a..."
    menu:
        "Los estilistas de Factor G":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Vidal Sasoon":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "La hechicera":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Shredder":
            r "Queda archivada tu respuesta"
    hide heman
    jump cuestion
    
label sesenta:
    $ preguntas += 1
    show troyacaballo at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué tenia en su interior el caballo de Troya?"
    menu:
        "Una botella de vino":
            r "Queda archivada tu respuesta"
        "Un puñado de griegos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Caramelos y regalos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "madera":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide troyacaballo
    jump cuestion
    
label suno:
    $ preguntas += 1
    show locke at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué a Locke no le crece el pelo en la isla pese a que le devolvió la movilidad en las piernas?"
    menu:
        "Porque es familia de Lex Luthor":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Porque la isla sólo te transporta en el tiempo un par de años atrás":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "No es calvo, se rapa para parecer más sexy":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "¿Quien es Locke?":
            r "Queda archivada tu respuesta"
    hide locke
    jump cuestion
    
label sdos:
    $ preguntas += 1
    show atreyu at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cómo se llamaba el caballo de Atreyu?"
    menu:
        "Artax":
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Guarrilandia":
            r "Queda archivada tu respuesta"
        "Fujur":
            r "Queda archivada tu respuesta"
        "España":
            r "Queda archivada tu respuesta"
    hide atreyu
    jump cuestion
    
label stres:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué es un beso negro?"
    menu:
        "Besar a Will Smith":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Una guarreria":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Lo último que pediria un racista en Harlem":
            r "Queda archivada tu respuesta"
        "Lo único que te digo es que si no te lavas los dientes antes no pasa nada":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label scuatro:
    $ preguntas += 1
    show coco at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Hola soy Coco y te voy a..."
    menu:
        "Meter un palo que te habio":
            r "Queda archivada tu respuesta"
        "Dar dos yoyas que te van a temblar las orejas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Comer to´l buyuyu":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Enseñar la diferencia entre mucho y poco":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide coco
    jump cuestion
    
label scinco:
    $ preguntas += 1
    show madonna at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿A que edad perdió la virginidad Madonna?"
    menu:
        "Madonna es virgen":
            $ puntos+=2
            r "Esto..."
            r "Asi que has pulsado aqui"
            r "Ha sido de cachondeo ¿verdad?"
            r "Querias ver si Roboto habia preparado algo, porque una pregunta tan estúpida alguna trampa debia tener"
            r "Pues bien, has acertado."
            r "Bienvenido al Easter Egg de 50xRoboto"
            r "Podrás preguntar en tres ocasiones lo que quieras sobre Roboto y yo encantado te lo responderé"
            $ bobobo= renpy.input("Primera cuestión")
            r "Oh, lo siento, eso no se puede contar"
            $ bobobo= renpy.input("Prueba de nuevo:")
            r "No se como lo haces pero siempre preguntas algo que no puedo responder"
            $ bobobo= renpy.input("La última oportunidad:")
            r "Efectivamente"
            r "Roboto lo hace sin descanso"
            r "Oh, era eso lo que habias preguntado ¿no?"
        "Me pidio que no lo contara":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "A los quince":
            r "Queda archivada tu respuesta"
        "¿A quien le importa?":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide madonna
    jump cuestion
    
label sseis:
    $ preguntas += 1
    show holmes at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué Sherlock Holmes no iba con mujeres pero sin embargo se metia opio siempre que podia?"
    menu:
        "Porque era misógino y drogata":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Las mujeres son peores que la droga":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Las drogas son mejores que las mujeres":
            r "Queda archivada tu respuesta"
        "Las mujeres perjudican la salud más que la droga":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide holmes
    jump cuestion
    
label ssiete:
    $ preguntas += 1
    show madrid at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cuantos títulos ha ganado el Real Madrid en toda su historia?"
    menu:
        "Suficientes":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Pocos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Mas que el Barcelona":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Ninguno":
            r "Queda archivada tu respuesta"
    hide madrid
    jump cuestion
    
label socho:
    $ preguntas += 1
    show jack at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿A qué se dedica Jack Bauer los restantes 364 días del año?"
    menu:
        "Es frutero":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "A tocarse las granadas":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Lo congelan hasta la próxima crisis":
            r "Queda archivada tu respuesta"
        "Es funcionario":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide jack
    jump cuestion
    
label snueve:
    $ preguntas += 1
    show putin at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué tenemos que sacar para ganar a Putin?"
    menu:
        "Piedra":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Un Topol-M":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Una llave de judo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "A su suegra":
            r "Queda archivada tu respuesta"
    hide putin
    jump cuestion
    
label setenta:
    $ preguntas += 1
    show arpon at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿De qué tamaño es el arpón del Capitán Ahab?"
    menu:
        "King Size":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Mediano con estrias":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "XXL":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Dos metros":
            r "Queda archivada tu respuesta"
    hide arpon
    jump cuestion
    
label stuno:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Encuentra al que desentona"
    menu:
        "Ian McKellen":
            r "Queda archivada tu respuesta"
        "Tom Selleck":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Efectivamente, es el único que lleva bigote."
            r "Queda archivada tu respuesta"
        "Oscar Wilde":
            r "Queda archivada tu respuesta"
        "Jesus Vazquez":
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label stdos:
    $ preguntas += 1
    show zipi at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿A qué se dedica Pantuflo Zapatilla, padre de los traviesos Zipi y Zape?"
    menu:
        "A comer":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Es filatélico y colombifílico":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "A dejar insatisfecha a Jaimita":
            r "Queda archivada tu respuesta"
        "A la bebida (con esos hijos...)":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide zipi
    jump cuestion
    
label sttres:
    $ preguntas += 1
    show curro at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cómo lograba acabar con los franceses Curro Jimenez?"
    menu:
        "A patillazos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Con el aliento del algarrobo":
            r "Queda archivada tu respuesta"
        "Enloqueciendolos con una disertación del estudiante sobre el contrato social":
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "A navajazos, como buenos españoles":
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide curro
    jump cuestion
    
label stcuatro:
    $ preguntas += 1
    show cabal at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cómo se llama este juego?"
    menu:
        "Cabal. ¡¡Si lo pone en la imagen!!":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Debe ser una trampa, seguro. Pues digo que... Operation Wolf":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Nam, dios mio, Nam":
            r "Queda archivada tu respuesta"
        "Super Mario cogió su fusil":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide cabal
    jump cuestion
    
label stcinco:
    $ preguntas += 1
    show r28 at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué es más rápido que el R28 de Fernando Alonso?"
    menu:
        "Un eyaculador precoz ante Carolina Kurkova desnuda":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Un rumano delante de una joyeria sin seguridad":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "King Africa perseguido por su dietista":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Todos los anteriores":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide r28
    jump cuestion
    
label stseis:
    $ preguntas += 1
    show arale at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cómo se llama el ser alado compañero de Arale?"
    menu:
        "Sembei":
            r "Queda archivada tu respuesta"
        "Gatchan":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Suppaman":
            r "Queda archivada tu respuesta"
        "Taro":
            r "Queda archivada tu respuesta"
    hide arale
    jump cuestion
    
label stsiete:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué cruzó el pollo la carretera?"
    menu:
        "Porque le perseguia su mujer":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "No cruzó, la carretera se desplazo bajo él":
            r "Queda archivada tu respuesta"
        "Para que no le metieran una barra de acero por el ano":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Chuck Norris se lo ordenó":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label stocho:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué haces si te roban la moto en Coslada?"
    menu:
        "Llamas a la mafia":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Llamas a Asuntos Internos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Llamas a Superman":
            r "Queda archivada tu respuesta"
        "Llamas al concesionario para comprarte una nueva porque de la otra te puedes ir despidiendo":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label stnueve:
    $ preguntas += 1
    show gordagalaxias at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien creó {b}La Gorda de las galaxias{/b}?"
    menu:
        "Nico":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Jan":
            r "Queda archivada tu respuesta"
        "Ramis":
            r "Queda archivada tu respuesta"
        "Cera":
            r "Queda archivada tu respuesta"
    hide gordagalaxias
    jump cuestion
    
label ochenta:
    $ preguntas += 1
    show elvira at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué nombre pone en el dni de Elvira?"
    menu:
        "Elli Walash":
            r "Queda archivada tu respuesta"
        "Cassandra Peterson":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Laurin Heist":
            r "Queda archivada tu respuesta"
        "Andrea Simpson":
            r "Queda archivada tu respuesta"
    hide elvira
    jump cuestion
    
label ouno:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien es el gafe de televisión por antonomasia?"
    menu:
        "Llum Barrera":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Pepe Gafez":
            r "Queda archivada tu respuesta"
        "Flipy":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Carolina Ferre":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label odos:
    $ preguntas += 1
    show diana at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual era el nombre de la lagarta más sexy de V?"
    menu:
        "Lidia":
            r "Queda archivada tu respuesta"
        "Julie":
            r "Queda archivada tu respuesta"
        "Allison":
            r "Queda archivada tu respuesta"
        "Diana":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide diana
    jump cuestion
    
label otres:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué dejó su blog Javi Moya?"
    menu:
        "Agárrame la po...":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Javi Moya nunca existió, era el sobrenombre de un consorcio de chinos aburridos":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Consiguió un trabajo en la SGAE":
            r "Queda archivada tu respuesta"
        "La policia del Copyright cayó sobre él":
            $ renpy.sound.play("acierto.wav")             
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label ocuatro:
    $ preguntas += 1
    show gta at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien es el protagonista de Grand Theft Auto más molón?"
    menu:
        "Cj":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Tony Vercetti":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "El mudo de GTA III":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Niko Bellic":
            r "Queda archivada tu respuesta"
    hide gta
    jump cuestion
    
label ocinco:
    $ preguntas += 1
    show michael at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien es este actor?"
    menu:
        "El negro de Friends":
            r "Pues no, en Friends no salian negros. Si la pregunta te parecia racista, imaginate la serie..."
            r "Queda archivada tu respuesta"
        "El negro de Perdidos":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "El negro de Raices":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "El negro de Matrix":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide michael
    jump cuestion
    
label oseis:
    $ preguntas += 1
    show picolo at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué intenta detener Piccolo?"
    menu:
        "El plan hidrológico nacional":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "La negociación de Zapatero con ETA":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "La renovación del PP":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "El trenhotel Barcelona-Málaga":
            r "Queda archivada tu respuesta"
    hide picolo
    jump cuestion
    
label osiete:
    $ preguntas += 1
    show lolek at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Nombre de este personaje"
    menu:
        "Bolek":
            r "Queda archivada tu respuesta"
        "Ralph Wiggum":
            r "Queda archivada tu respuesta"
        "Lolek":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Aaron Bernstein":
            r "Queda archivada tu respuesta"
    hide lolek
    jump cuestion
    
label oocho:
    $ preguntas += 1
    show aguilera at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es la razón de la reciente pechonalidad de Christina Aguilera?"
    menu:
        "Implantes":
            r "Queda archivada tu respuesta"
        "Masajeo intensivo e implantes":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Friegas con jugo de melón e implantes":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Succiónes periodicas e implantes":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide aguilera
    jump cuestion
    
label onueve:
    $ preguntas += 1
    show penelope at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué Penelope Cruz se lia con todos los protagonistas de sus películas?"
    menu:
        "Es ninfómana":
            r "Queda archivada tu respuesta"
        "Es enamoradiza":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Es una enamoradiza ninfómana":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Para trepar al modo tradicional":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide penelope
    jump cuestion
    
label noventa:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Mueres y en el infierno te dicen que si no quieres pasar alli la eternidad, deberás volver a la tierra y hacer rico lo más rápidamente posible. ¿Qué trabajo escogerias?"
    menu:
        "Oficial de la condicional de Pete Doherty":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Lo fascinante de esta cuestión, es que podrias cambiar los nombres, ¡¡¡y seguirian teniendo sentido!!!"
            r "Queda archivada tu respuesta"
        "Camello de Maradona":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Lo fascinante de esta cuestión, es que podrias cambiar los nombres, ¡¡¡y seguirian teniendo sentido!!!"
            r "Queda archivada tu respuesta"
        "Estilista de Britney Spears":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Lo fascinante de esta cuestión, es que podrias cambiar los nombres, ¡¡¡y seguirian teniendo sentido!!!"
            r "Queda archivada tu respuesta"
        "Psicóloga de Amy Winehouse":
            r "Lo fascinante de esta cuestión, es que podrias cambiar los nombres, ¡¡¡y seguirian teniendo sentido!!!"
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label nuno:
    $ preguntas += 1
    show clemente at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿A qué equipo entrena Javier Clemente?"
    menu:
        "Javier ¿qué?":
            r "Queda archivada tu respuesta"
        "Ah, ¿pero su trabajo es entrenar?":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Al patapum parriba":
            $ puntos+=3
            $ renpy.sound.play("acierto.wav")
            r "Queda archivada tu respuesta"
        "Al que le da la gana":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide clemente
    jump cuestion
    
label ndos:
    $ preguntas += 1
    show oliver at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cuanto duraba un partido en \"Campeones\"?"
    menu:
        "90 minutos":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "90 capítulos":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "90 horas":
            r "Queda archivada tu respuesta"
        "Lo que tardabas en apagar la tele":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide oliver
    jump cuestion
    
label ntres:
    $ preguntas += 1
    show cupido at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué se celebra el día de San Valentin?"
    menu:
        "Los beneficios de El Corte Inglés":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "El dia internacional de la toga":
            r "Queda archivada tu respuesta"
        "El dia de los cursis":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Cursis, enamorados, tanto monta, monta tanto"
            r "Lo mismo es"
            r "Queda archivada tu respuesta"
        "El dia de los enamorados":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
    hide cupido
    jump cuestion

label ncuatro:
    $ preguntas += 1
    show calleja at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Donde hizo la comunión Jesús Calleja?"
    menu:
        "En el Everest (huyendo de los chinos que lo confundieron con un tibetano)":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "En una gruta subterranea":
            r "Queda archivada tu respuesta"
        "En Castilla y León":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "En la iglesia de su pueblo":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide calleja
    jump cuestion

label ncinco:
    $ preguntas += 1
    show interrogacion at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "Van dos por la calle y el de enmedio..."
    menu:
        "Es el de Los Chichos":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Se cae y le echa la culpa al de atras":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Te planta una torta por mirarle el culo a su novia":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "El de enmedio no existe":
            r "Que tio mas aburrido, pues hala no hay puntos"
            r "Queda archivada tu respuesta"
    hide interrogacion
    jump cuestion
    
label nseis:
    $ preguntas += 1
    show picolo2 at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien interpretará a este persona en la nueva película de Dragon Ball?"
    menu:
        "Un guisante hiperdesarrollado":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Spike":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Un ecologista de Greenpeace":
            r "Queda archivada tu respuesta"
        "El amigo del novio de Scarlett Johansson":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide picolo2
    jump cuestion
    
label nsiete:
    $ preguntas += 1
    show halo at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Que nesesita este hombre?"
    menu:
        "Un billete a Ecuador":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Un arma":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Clases de dicción":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Ir a un taller de chapa y pintura":
            r "Queda archivada tu respuesta"
    hide halo
    jump cuestion
    
label nocho:
    $ preguntas += 1
    show bill at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué sonrie Bill Clinton en esta foto?"
    menu:
        "Porque Hillary le está tocando el bastón de mando":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Porque es la noche feliz en Hooters y Hillary tiene que quedarse en casa estudiando":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Porque está pensando en las becarias que tendrá cuando sea presidente":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque Hillary le puso vaselina en los dientes (no pregunteis como ni por qué)":
            r "Queda archivada tu respuesta"
    hide bill
    jump cuestion
    
label nnueve:
    $ preguntas += 1
    show elvis at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué llamaban a Elvis: La pelvis?"
    menu:
        "Porque se jincaba a todo lo que se le pusiera a tiro (animal o vegetal)":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Para que fuera facilmente distinguible de un Playmobil":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Porque era un fan de los Hula Hops":
            r "Queda archivada tu respuesta"
        "Para que se fijaran en su paquete":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide elvis
    jump cuestion
    
label cien:
    show rosy at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    $ preguntas += 1
    r "¿Por qué no se ha hecho nunca la cirugia estética Rosy de Palma?"
    menu:
        "¿Estás de broma? Si no le hace falta":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Porque entonces no la reconocerian los miembros de su planeta cuando vuelvan a recogerla":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque ella se ve guapa":
            r "Queda archivada tu respuesta"
        "Se la hizo, pero fue al mismo cirujano del Joker":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide rosy
    jump cuestion
    
label ci:
    $ preguntas += 1
    show juego at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿En qué juego eran censurados los pechos de esta señorita?"
    menu:
        "Phantis":
            r "Queda archivada tu respuesta"
        "Game Over":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Hundra":
            r "Queda archivada tu respuesta"
        "Sabrina":
            r "Queda archivada tu respuesta"
    hide juego
    jump cuestion
    
label cii:
    $ preguntas += 1
    show risto at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué desayuna Risto Mejide?"
    menu:
        "Choco Krispies":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Humildad":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Un vaso de bilis":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Dos triunfitos pasados por agua":
            r "Queda archivada tu respuesta"
    hide risto
    jump cuestion
    
label ciii:
    $ preguntas += 1
    show batman at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Que le dice Batman a Robin, para que suba al batmovil?"
    menu:
        "Te dejo jugar con la palanca de cambios":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Tomare las curvas muy cerradas":
            r "Queda archivada tu respuesta"
        "Robin, sube al batmovil":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Vamos, te llevaré a la tienda de piruletas":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide batman
    jump cuestion
    
label civ:
    $ preguntas += 1
    show carmen at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Donde se esconde Carmen Sandiego?"
    menu:
        "En su casa":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "En un sitio lejos de Wally":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "En el area 51":
            r "Queda archivada tu respuesta"
        "En el club La fusta veloz, lleva látigo y antifaz y se hace llamar mistress Pain":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide carmen
    jump cuestion

label cv:
    $ preguntas += 1
    show arce at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quien compuso la canción de esta serie?"
    menu:
        "Claudio Biern Boyd":
            r "Queda archivada tu respuesta"
        "Miliki":
            r "Queda archivada tu respuesta"
        "Oliver Onions":
            r "Queda archivada tu respuesta"
        "Emilio Aragón":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide arce
    jump cuestion
    
label cvi:
    $ preguntas += 1
    show madonna at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué Madonna besa a todas las chicas que se le acercan?"
    menu:
        "Para quitarse el mal sabor de boca":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Porque tiene las lentillas mal graduadas y piensa que son hombres":
            r "Queda archivada tu respuesta"
        "Para vender el reportaje, que con tanto niños hay que sacar dinero de donde sea":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque tanto le da meter la lengua en un lado u otro, el caso es meterla":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide madonna
    jump cuestion
    
label cvii:
    $ preguntas += 1
    show setas at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Quién tiene las setas más grandes?"
    menu:
        "La de la derecha":
            $ renpy.sound.play("acierto.wav") 
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "La de la izquierda":
            r "Queda archivada tu respuesta"
        "Setas no se, pero la de enmedio tiene unas tetas impresionantes":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Todas son iguales":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide setas
    jump cuestion
    
label cviii:
    $ preguntas += 1
    show goku at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Por qué le cortaron el rabo a Goku?"
    menu:
        "Para que no se convirtiera en mono":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Por envidia":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=1
            r "Queda archivada tu respuesta"
        "Porque tanto pelo en un rabo da grima":
            r "Queda archivada tu respuesta"
        "Para que dejara alguna para los demás":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
    hide goku
    jump cuestion
    
label cix:
    $ preguntas += 1
    show planta at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Qué ocurria cuando tocabas esta planta?"
    menu:
        "Te entraba urticaria":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Te comia una mano":
            r "Queda archivada tu respuesta"
        "Mario se transformaba en fontanero cabreado":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Te convertias en Super Mario":
            r "Queda archivada tu respuesta"
    hide planta
    jump cuestion
    
label cx:
    $ preguntas += 1
    show espada at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿A quien pertenece esta espada?"
    menu:
        "David el gnomo":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=2
            r "Queda archivada tu respuesta"
        "Makinavaja":
            r "Queda archivada tu respuesta"
        "Link":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Conan el bárbaro cuando tenia 2 meses":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide espada
    jump cuestion
    
label cxi:
    $ preguntas += 1
    show argentina at Position(xpos=20, ypos=41, xanchor=0, yanchor=0)
    r "¿Cual es la principal exportación de Argentina?"
    menu:
        "Psicólogos":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Humildad":
            r "Queda archivada tu respuesta"
        "Dentistas":
            $ renpy.sound.play("acierto.wav")            
            $ puntos+=3
            r "Queda archivada tu respuesta"
        "Carne":
            $ renpy.sound.play("acierto.wav")
            $ puntos+=1
            r "Queda archivada tu respuesta"
    hide argentina
    jump cuestion
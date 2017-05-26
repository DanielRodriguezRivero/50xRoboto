init:
       
    $ config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)

    # Personajes
    $ r =Character('Robotín', color="#c8ffc8")
    $ p =Character('Sulara', color="#c8ffc8")
            
    #variables
    $ preguntas=0
    $ salto = 0
    $ puntos=0
    $ hola=""
    $ bobobo=""
    
    #imagenes
    image back="back.jpg"
    image back1="back1.jpg"  #imagen robotin
    image fin2="fin2.jpg"
    image musica="winamp.png"  #imagen para pruebas sonidos
    image presentadora="presentadora.png"
    image picolo="picolo.jpg"
    image picolo2 ="picolo2.jpg"
    image setas="setas.jpg"
    image cabal="cabal.png"
    image melee="melee.gif"
    image lezley="lezley.jpg"
    image sophie="sophie.jpg"
    image risto="risto.jpg"
    image interrogacion="interrogacion.jpg"
    image putin="putin.jpg"
    image melendi="melendi.jpg"
    image duke="duke.jpg"
    image r28="r28.jpg"
    image kennedy="kennedy.jpg"
    image espada="espada.jpg"
    image bill="bill.jpg"
    image clemente="clemente.jpg"
    image rosy="rosy.jpg"
    image china="china.jpg"
    image locke="locke.jpg"
    image enterprise="enterprise.png"
    image madrid="madrid.jpg"
    image heman="heman.jpg"
    image arpon="arpon.jpg"
    image coco="coco.jpg"
    image gta="gta.jpg"
    image goku="goku.jpg"
    image calleja="calleja.jpg"
    image alemania="alemania.gif"
    image jenna="jenna.jpg"
    image brasil="brasil.jpg"
    image argentina="argentina.gif"
    image madonna="madonna.jpg"
    image penelope="penelope.jpg"
    image holmes="holmes.gif"
    image aguilera="aguilera.jpg"
    image iglesias="iglesias.jpg"
    image wally="wally.jpg"
    image carmen="carmen.jpg"
    image elvis="elvis.jpg"
    image jack="jack.jpg"
    image oliver="oliver.jpg"
    image curro="curro.jpg"
    image kate="kate.jpg"
    image desperate="desperate.jpg"
    image mark="mark.gif"
    image anarosa="anarosa.jpg"
    image michael="michael.jpg"
    image capitan="capitan.jpg"
    image zipi="zipi.jpg"
    image cupido="cupido.jpg"
    image chuck="chuck.jpg"
    image batman="batman.jpg"
    image rocky="rocky.jpg"
    image planta="planta.png"
    image arce="arce.jpg"
    image juego="juego.jpg"
    image halo="halo.png"
    image arale="arale.jpg"
    image atreyu="atreyu.jpg"
    image tortugas="tortugas.png"
    image super="super.gif"
    image kryten="kryten.jpg"
    image torre="torre.jpg"
    image lolek="lolek.jpg"
    image yoshi="yoshi.png"
    image laurie="laurie.png"
    image lutero="lutero.jpg"
    image armada="armada.jpg"
    image caballeros="caballeros.jpg"
    image serrano="serrano.jpg"
    image goro="goro.jpg"
    image bobobo="bobobo.jpg"
    image navy="navy.jpg"
    image queen="queen.jpg"
    image salto="salto.jpg"
    image wonderwoman="wonderwoman.png"
    image diana="diana.jpg"
    image elvira="elvira.jpg"
    image spirit="spirit.jpg"
    image troyacaballo="troyacaballo.gif"
    image gordagalaxias="gordagalaxias.png"
    image asterix="asterix.jpg"
    image segis="segis.jpg"
    image kenshiro="kenshir.jpg"
    
    
label start:
    $ hola= renpy.input("Como te llamas?")
    if hola=="DANI" or hola=="Dani" or hola=="dani":
        r "Funciona"
    scene back   
    show presentadora  
    p "¡¡Hola!!"
    p "Te agradeceria que me miraras a los ojos"
    p "Gracias."
    p "Si, te estarás preguntando... \"Yo he visto a esta chica en alguna parte \""
    p "Todo el mundo me dice que me parezco a mi prima malvada Tigara"
    p "No se por qué la verdad..."
    p "Bienvenido a la madre de todos los concursos: The anual contest to be a new Mr Roboto"
    p "En español: \"Roboto pregunta\""
    p "A través de veinte preguntas, deberás probar tus conocimientos sobre los más diversos temas"
    p "Cada respuesta tiene una determinada puntuación, que va de 3 a 1, según lo acertada que sea"
    p "..."
    p "La sabiduria es relativa"
    p "El premio... no hay, sólo la satisfacción de haber aprendido algo"
    p "Puede parecer fácil, pero ni el mismo Mr Roboto es capaz de acertarlas todas correctamente."
    p "No os asusteis."
    p "Aunque no lo parezca, todas tienen su lógica, retorcida en ocasiones"
    p "Para no distraerte con mi..." 
    p "personalidad, el encargado de realizar las preguntas será Robotín, el dibujo ilegítimo que el propio Mr Roboto creo tras una noche desenfrenada de Fanta y Panteras Rosa"
    p "¡¡¡Mucha suerte!!!"
    hide presentadora
    hide back with dissolve
    scene back1 with fade
    r "Hola soy Robotín, la mascota de Fin del juego"
    r "Que no te engañe mi aspecto infantil, con estas pinzas he arrancado más...."
    r "Ah, me dicen que este es un cuestionario para casi todos los públicos y no puedo decir testículos"
    r "Bien, comencemos"
    $ renpy.music.play("ganador.mp3", loop=True)

    #esubtitle "Along with sfonts and the ability to change the text window, this lets us render reasonable subtitles."  #para usar como subtitulos el texto
    jump cuestion
    
label fin:
    hide back1
    scene back
    show presentadora
    $ renpy.music.stop(0,0)
    p "Hasta aquí llegó el cuestionario."
    p "Espero que no te haya resultado muy dificil"
    p "Más dificil es sujetarmelas a la hora de comer, y ya ves, me las apaño."
    p "Bien, veamos tu puntuacion"
    $ renpy.pause(2.0)
    p "Has obtenido %(puntos)d puntos "
    if  puntos>0 and  puntos<=10:
        p "Eres un fistro pecador. Tu ni siquiera tienes una pegatina de anís del mono. Cobarde"
    elif  puntos>10 and  puntos<= 21:
        p "No has hecho mucho el ridiculo, pero has estado cerca. Deberias leer más Fin del juego y menos "
    elif  puntos>21 and  puntos<= 41:
        p "Eres como la Fanta. Ni pinchas ni cortas en la guerra de las colas."
        p "Sigue intentandolo"
    elif  puntos>41 and  puntos<= 51:
        p "Tienes un cerebro como estas que tengo entre mis firmes manos, pero no es suficiente."
        p "Te queda un largo camino hasta alcanzar el Roboto absoluto."
        p "El estado de la mente en que toda mujer está muy buena y toda película es incomparable a una de Pajares y Esteso."
    elif puntos>51 and  puntos<= 59:
        p "Has obtenido el premio Mr Roboto a la excelencia personal. Sólo te ha faltado un suspiro para poder alcanzar la puntuación perfecta"
    elif puntos== 60:
        p "¡¡Felicidades!! Tu mente está sincronizada con la de Mr Roboto. Si eres una mujer, estás hecha para acostarte con él. Así que ya sabes, su mail está en la página \"Fin del juego\""
    with dissolve
    p "Espero que lo hayas pasado bien."
    p "Yo mucho. Bueno, ya lo ves"
    p "Hasta la próxima"
    hide presentadora
    hide back
    scene fin2
    p "Y recuerda, lee Fin del Juego o Backside Games o Mr Roboto pinta o Fuengirola on line"
    p "O cualquiera de los trabajos del basto imperio de Roboto"
    hide fin2
    return
    
     
label cuestion:
    if preguntas < 20:
        jump saltodos
    else:
        jump fin
    
label saltodos:
    $ salto = renpy.random.randint(1,111)
    if salto == 1:
        jump uno
    elif salto == 2:
        jump dos
    elif salto == 3:
        jump tres
    elif salto == 4:
        jump cuatro
    elif salto == 5:
        jump cinco
    elif salto == 6:
        jump seis
    elif salto == 7:
        jump siete
    elif salto == 8:
        jump ocho
    elif salto == 9:
        jump nueve
    elif salto == 10:
        jump diez
    elif salto == 11:
        jump once
    elif salto == 12:
        jump doce
    elif salto == 13:
        jump trece
    elif salto == 14:
        jump catorce
    elif salto == 15:
        jump quince
    elif salto == 16:
        jump dieciseis
    elif salto == 17:
        jump diecisiete
    elif salto == 18:
        jump dieciocho
    elif salto == 19:
        jump diecinueve
    elif salto == 20:
        jump veinte
    elif salto == 21:
        jump ventiuno
    elif salto == 22:
        jump ventidos
    elif salto == 23:
        jump ventitres
    elif salto == 24:
        jump venticuatro
    elif salto == 25:
        jump venticinco
    elif salto == 26:
        jump ventiseis
    elif salto == 27:
        jump ventisiete
    elif salto == 28:
        jump ventiocho
    elif salto == 29:
        jump ventinueve
    elif salto == 30:
        jump treinta
    elif salto == 31:
        jump treintayuno
    elif salto == 32:
        jump treintaydos
    elif salto == 33:
        jump treintaytres
    elif salto == 34:
        jump treintaycuatro
    elif salto == 35:
        jump tcinco
    elif salto == 36:
        jump tseis
    elif salto == 37:
        jump tsiete
    elif salto == 38:
        jump tocho
    elif salto == 39:
        jump tnueve
    elif salto == 40:
        jump cuarenta
    elif salto == 41:
        jump cuno
    elif salto == 42:
        jump cdos        
    elif salto == 43:
        jump ctres
    elif salto == 44:
        jump ccuatro
    elif salto == 45:
        jump ccinco
    elif salto == 46:
        jump cseis
    elif salto == 47:
        jump csiete
    elif salto == 48:
        jump cocho
    elif salto == 49:
        jump cnueve
    elif salto == 50:
        jump cincuenta
    elif salto == 51:
        jump ciuno
    elif salto == 52:
        jump cidos
    elif salto == 53:
        jump citres
    elif salto == 54:
        jump cicuatro
    elif salto == 55:
        jump cicinco
    elif salto == 56:
        jump ciseis
    elif salto == 57:
        jump cisiete
    elif salto == 58:
        jump ciocho
    elif salto == 59:
        jump cinueve
    elif salto == 60:
        jump sesenta
    elif salto == 61:
        jump suno
    elif salto == 62:
        jump sdos
    elif salto == 63:
        jump stres
    elif salto == 64:
        jump scuatro
    elif salto == 65:
        jump scinco
    elif salto == 66:
        jump sseis
    elif salto == 67:
        jump ssiete
    elif salto == 68:
        jump socho
    elif salto == 69:
        jump snueve
    elif salto == 70:
        jump setenta
    elif salto == 71:
        jump stuno
    elif salto == 72:
        jump stdos
    elif salto == 73:
        jump sttres
    elif salto == 74:
        jump stcuatro
    elif salto == 75:
        jump stcinco
    elif salto == 76:
        jump stseis
    elif salto == 77:
        jump stsiete
    elif salto == 78:
        jump stocho
    elif salto == 79:
        jump stnueve
    elif salto == 80:
        jump ochenta
    elif salto == 81:
        jump ouno
    elif salto == 82:
        jump odos
    elif salto == 83:
        jump otres
    elif salto == 84:
        jump ocuatro
    elif salto == 85:
        jump ocinco
    elif salto == 86:
        jump oseis
    elif salto == 87:
        jump osiete
    elif salto == 88:
        jump oocho
    elif salto == 89:
        jump onueve
    elif salto == 90:
        jump noventa
    elif salto == 91:
        jump nuno
    elif salto == 92:
        jump ndos
    elif salto == 93:
        jump ntres
    elif salto == 94:
        jump ncuatro
    elif salto == 95:
        jump ncinco
    elif salto == 96:
        jump nseis
    elif salto == 97:
        jump nsiete
    elif salto == 98:
        jump nocho
    elif salto == 99:
        jump nnueve
    elif salto == 100:
        jump cien
    elif salto == 101:
        jump ci
    elif salto == 102:
        jump cii
    elif salto == 103:
        jump ciii
    elif salto == 104:
        jump civ
    elif salto == 105:
        jump cv
    elif salto == 106:
        jump cvi
    elif salto == 107:
        jump cvii
    elif salto == 108:
        jump cviii
    elif salto == 109:
        jump cix
    elif salto == 110:
        jump cx
    elif salto == 111:
        jump cxi
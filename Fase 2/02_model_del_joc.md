# 1. Components principals del joc

El microvideojoc **Survival Terminal** és un joc textual de supervivència i gestió de recursos. El sistema es construeix a partir d'uns quants components principals, suficients per mantenir un abast assumible i coherent amb la Fase 1.

Els components principals són:

- **Joc**: coordina el flux general de la partida i controla el bucle principal.
- **Jugador**: representa l'estat del personatge i les accions que pot fer.
- **Recurs**: representa els elements que el jugador pot trobar o consumir per modificar el seu estat.

Aquest model és deliberadament simple perquè el projecte ha de cabre dins del límit aproximat de 10 hores i, alhora, ha de permetre fer després proves, depuració i millores reals.

# 2. Entitats identificades

## 2.1 Joc
És l'entitat que governa la partida. S'encarrega d'inicialitzar el sistema, mostrar informació, gestionar el torn actual i comprovar si la partida continua o acaba.

## 2.2 Jugador
És l'entitat central del joc. Manté els estats principals del personatge, com la salut, l'energia, el menjar disponible i els dies sobreviscuts.

## 2.3 Recurs
Representa un objecte simple que es pot obtenir durant l'exploració i que pot afectar l'estat del jugador. En aquesta primera versió servirà sobretot per modelar menjar o recursos de recuperació.

# 3. Atributs clau de cada entitat

## 3.1 Atributs de `Joc`

- `jugador: Jugador`  
  Conté la instància del jugador actiu.
- `diesObjectiu: int`  
  Nombre de dies que cal sobreviure per guanyar.
- `finalitzat: bool`  
  Indica si la partida ha acabat o no.

## 3.2 Atributs de `Jugador`

- `salut: int`  
  Valor de vida actual del jugador.
- `energia: int`  
  Valor d'energia actual.
- `menjar: int`  
  Quantitat de recursos consumibles disponibles.
- `diesSupervivencia: int`  
  Nombre de dies o torns superats.

## 3.3 Atributs de `Recurs`

- `nom: String`  
  Nom del recurs.
- `valorEnergia: int`  
  Quantitat d'energia que pot recuperar o aportar.
- `consumible: bool`  
  Indica si el recurs es consumeix en utilitzar-lo.

# 4. Accions, mètodes o funcions principals

## 4.1 Mètodes de `Joc`

- `iniciar()`  
  Prepara la partida i inicialitza els valors.
- `mostrarEstat()`  
  Mostra a pantalla l'estat actual del jugador.
- `processarAccio(opcio)`  
  Interpreta l'opció escollida pel jugador i executa l'acció corresponent.
- `comprovarFi()`  
  Verifica si es compleix una condició de victòria o derrota.
- `buclePrincipal()`  
  Executa el cicle principal de la partida fins que el joc finalitza.

## 4.2 Mètodes de `Jugador`

- `menjar()`  
  Consumeix menjar i recupera energia.
- `descansar()`  
  Recupera salut o energia segons la regla implementada.
- `explorar()`  
  Intenta obtenir un recurs, amb possible recompensa o penalització.
- `estaViu()`  
  Retorna si la salut del jugador és superior a zero.

## 4.3 Mètodes de `Recurs`

- `aplicarAlJugador(jugador)`  
  Aplica els efectes del recurs sobre l'estat del jugador.

# 5. Explicació del diagrama de classes

El diagrama de classes mostra l'estructura estàtica del sistema i la relació entre les tres entitats principals del joc:

- **Joc** és la classe coordinadora.
- **Joc** conté una instància de **Jugador**, perquè tota la partida gira al voltant d'un únic jugador.
- **Jugador** pot utilitzar un o més **Recurs**, especialment durant l'acció d'explorar.

L'organització és així perquè permet separar responsabilitats:

- La lògica global de la partida no queda barrejada amb l'estat del personatge.
- L'estat del jugador es manté encapsulat.
- Els recursos es poden ampliar en el futur sense haver de reescriure tota la lògica principal.

Aquest model no és decoratiu: està pensat perquè es pugui programar directament. Cada classe té una funció clara i una relació concreta amb la resta.

**Fitxer del diagrama:** `diagrames/diagrama_classes.png`

# 6. Explicació del diagrama de comportament

Per representar el flux del joc s'ha triat un **diagrama d'activitat**, perquè és el tipus que millor encaixa amb un joc textual basat en un bucle repetitiu.

El diagrama mostra aquest procés:

1. Inici de la partida.
2. Mostrar l'estat del jugador.
3. Llegir l'acció escollida.
4. Aplicar les conseqüències.
5. Comprovar si hi ha victòria o derrota.
6. Si no hi ha final, continuar el bucle.

Aquest diagrama reflecteix exactament el bucle principal definit a la Fase 1. Per tant, compleix el requisit que el model de comportament no sigui genèric, sinó vinculat al joc real que es vol implementar.

**Fitxer del diagrama:** `diagrames/diagrama_comportament.png`

# 7. Correspondència entre diagrames i codi futur

La traducció dels diagrames al codi real serà directa:

- La classe **Joc** es convertirà en un fitxer o mòdul principal que controlarà la partida.
- La classe **Jugador** es convertirà en una classe separada amb atributs i mètodes propis.
- La classe **Recurs** es convertirà en una classe simple per representar objectes consumibles.

Correspondència concreta:

- El **diagrama de classes** defineix quines classes s'han de crear, quins atributs necessiten i quines responsabilitats tindrà cadascuna.
- El **diagrama d'activitat** defineix l'ordre lògic del `while` principal del joc i les comprovacions de final de partida.

Això permet que, a la Fase 3, la implementació sigui coherent amb el model i no improvisada.

# 8. Estructura inicial del repositori

Es proposa aquesta estructura inicial:

```text
SurvivalTerminal/
├── README.md
├── 01_idea_i_abast.md
├── 02_model_del_joc.md
├── src/
│   ├── main.py
│   ├── joc.py
│   ├── jugador.py
│   └── recurs.py
├── diagrames/
│   ├── diagrama_classes.png
│   └── diagrama_comportament.png
└── docs/
```

Aquesta estructura té sentit perquè:

- separa la documentació del codi;
- deixa un espai específic per als diagrames;
- prepara el projecte per créixer sense perdre ordre;
- facilita després la fase de proves, depuració i millores.

# 9. Primer commit i README inicial

El primer commit hauria de deixar evidència clara de l'inici del projecte. El contingut mínim recomanat és:

- `README.md` inicial
- `01_idea_i_abast.md`
- `02_model_del_joc.md`
- carpeta `diagrames/`
- carpeta `src/` amb l'estructura base

Exemple de missatge de primer commit:

```bash
git commit -m "Inicialitza el projecte Survival Terminal amb documentació i estructura base"
```

El `README.md` inicial ha d'explicar com a mínim:

- títol del projecte;
- descripció breu del joc;
- objectiu general;
- tecnologies previstes;
- estructura inicial del repositori.

# Validació final de la fase

Aquest model és coherent amb la Fase 1 perquè:

- manté el mateix tipus de joc: supervivència textual;
- conserva el mateix bucle principal;
- incorpora estats clars: salut, energia, menjar i dies;
- limita l'abast a tres classes principals, suficients per una primera versió viable;
- prepara una base realista per programar després en la fase d'implementació.

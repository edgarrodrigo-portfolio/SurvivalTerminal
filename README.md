# 1. Títol provisional del joc
Survival Terminal

# 2. Tipus de microvideojoc escollit
Joc de supervivència / gestió de recursos (textual)

# 3. Objectiu del joc
L’objectiu del joc és sobreviure el màxim nombre de dies possibles gestionant recursos com menjar, energia i salut.

# 4. Rol del jugador
El jugador controla un personatge que es troba en una situació de supervivència.

Pot:
- Menjar per recuperar energia
- Descansar per recuperar salut
- Explorar per trobar recursos
- Prendre decisions que afecten els seus estats

# 5. Regles bàsiques
- Cada acció consumeix energia
- Si l’energia arriba a 0, el jugador perd salut
- Els recursos són limitats
- Cada dia passa automàticament després d’una acció

# 6. Condicions de victòria i derrota
Victòria:
- Sobreviure un nombre determinat de dies (ex: 10 dies)

Derrota:
- La salut arriba a 0
- L’energia arriba a 0 i no es pot recuperar

# 7. Bucle principal del joc
El bucle del joc és:
1. Mostrar estat del jugador (vida, energia, dies)
2. El jugador escull una acció
3. S’apliquen conseqüències
4. Es comprova si ha guanyat o perdut
5. Es repeteix

# 8. Repte principal i dificultat
Repte:
- Gestionar correctament els recursos limitats

Dificultat:
- Mitjana (cal prendre decisions estratègiques)

# 9. Limitacions explícites
- No hi haurà gràfics avançats
- No hi haurà multijugador
- No hi haurà mapa complex
- No hi haurà sistema d’inventari avançat
- Només interfície per consola (text)

# 10. Riscos tècnics
1. Gestió incorrecta dels estats (vida, energia)
   → Solució: validar valors després de cada acció

2. Errors en la lògica del bucle del joc
   → Solució: provar cada iteració del bucle

3. Problemes amb l’entrada de l’usuari
   → Solució: validar input (opcions correctes)

# 11. Exploració amb IA

Prompt 1:
"Dóna'm idees de microvideojocs simples que es puguin fer en menys de 10 hores amb Python"

Resposta resumida:
- Joc de supervivència
- Joc de preguntes
- Joc de combat per torns

Prompt 2:
"Explica un bucle de joc simple per un joc de supervivència textual"

Resposta resumida:
- Mostrar estat
- Escollir acció
- Aplicar conseqüències
- Repetir fins condició final

# 12. Proposta final escollida
S’escull el joc de supervivència perquè és simple, clar i fàcil de modular.

# 13. Justificació de viabilitat
Aquest projecte és viable perquè:
- No requereix gràfics
- Té una lògica clara
- Es pot implementar en menys de 10 hores
- Utilitza estructures bàsiques (condicions, bucles, variables)

# 14. Mini pla de treball

Fase 1: Definir idea i regles  
Fase 2: Dissenyar estructura del codi  
Fase 3: Crear prototip funcional  
Fase 4: Provar i corregir errors  
Fase 5: Millorar i documentar  

# 15. Eines previstes i justificació

- Llenguatge: Python
  → Fàcil d’utilitzar i ràpid de desenvolupar

- IDE: Visual Studio Code
  → Lleuger i compatible amb Python

- IA: ChatGPT
  → Ajuda en idees, estructura i resolució de dubtes

- GitHub
  → Control de versions i entrega del projecte

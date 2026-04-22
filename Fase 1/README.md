# 🎮 Survival Terminal

Microvideojoc desenvolupat com a projecte de l’assignatura d’Entorns de Desenvolupament.

## 📌 Descripció

Survival Terminal és un joc de supervivència en mode text on el jugador ha de gestionar recursos per sobreviure el màxim nombre de dies possible.

El joc està pensat per ser simple però estructurat, amb un bucle de joc clar i estats definits.

---

## 🎯 Objectiu del joc

Sobreviure durant un nombre determinat de dies gestionant correctament:
- ❤️ Salut
- ⚡ Energia
- 📅 Dies

---

## 🕹️ Mecàniques del joc

El jugador pot realitzar diferents accions:

- 🍖 Menjar → recupera energia
- 😴 Descansar → recupera salut
- 🔍 Explorar → pot obtenir recursos (amb risc)

Cada acció té conseqüències i afecta els estats del jugador.

---

## 🔁 Bucle de joc

1. Es mostra l’estat actual del jugador
2. El jugador escull una acció
3. S’apliquen els efectes
4. Es comprova si el jugador guanya o perd
5. Es repeteix fins final de partida

---

## 🧠 Estats del joc

El sistema es basa en tres variables principals:

- Salut
- Energia
- Dies

Aquestes variables canvien constantment segons les accions del jugador.

---

## 🏁 Condicions

### ✅ Victòria
- Sobreviure X dies (configurable)

### ❌ Derrota
- Salut = 0
- Energia = 0 (sense possibilitat de recuperació)

---

## ⚙️ Tecnologies utilitzades

- Python 🐍
- Visual Studio Code 💻
- GitHub 🌐
- ChatGPT 🤖 (suport en idees i estructura)

---

## 📁 Estructura del projecte

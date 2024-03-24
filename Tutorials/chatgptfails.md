![Banner](https://github.com/nih23/Chatbot-Hackathon/blob/main/res/Banner.jpg?raw=true)

# ChatGPT fails
LLMs wie ChatGPT liefern möglicherweise nicht immer korrekte Datensätze. Darauf weißt ChatGPT selbst sogar explizit hin: _"ChatGPT kann Fehler machen. Überprüfen Sie wichtige Informationen."_
Die Ursache für die Fehlinformationen ist noch nicht ganz bekannt; oftmals füllt ChatGPT **nicht vorhandenes Wissen** (also Informationen, die dem Modell anhand fehlender Trainingsdaten nicht zur Verfügung stehen) mit allgemeinem Wissen auf, so wie hier in dem Folgenden Szenario zum Baumkataster der Stadt Leipzig dargestellt.

**1. Startdatensatz**
- [Baumkataster der Stadt Leipzig](https://opendata.leipzig.de/dataset/baumkataster-stadt-leipzig1): Baumverzeichnis, das je nach Stadtteil, Baumalter, etc. gefiltert werden kann.

**2. Abgleich**
- Google: Wo steht der älteste Baum der Stadt Leipzig? Ergebnis: [Starke Eiche im Auwald in Leipzig](https://www.baumkunde.de/baumregister/5221-starke_eiche_im_auwald_in_leipzig/).

**3. ChatGPT Test**
- User: _"wo ist der älteste baum der stadt leipzig?"_
- ChatGPT: _"Der älteste Baum Leipzigs ist die Starkeiche, die nordwestlich der Stadt im Auwaldgebiet Rosental steht. Die Eiche, die im dichten Bestand des Auwaldes steht und im Sommer nur schwer zu überblicken ist, wird auf ein Alter von etwa 600 Jahren geschätzt, obwohl diese Zahl möglicherweise zu hoch angesetzt sein könnte​"_ [''](https://www.monumentale-eichen.de/sachsen/2-kategorie/leipzig/).
- User: _"wie kommst du auf 600 jahre?"_
- ChatGPT: _"Entschuldigung für das Missverständnis. Die genaue Altersangabe von 600 Jahren stammt aus den Suchergebnissen, die ich gefunden habe, aber es scheint, dass diese Information nicht direkt aus den Quellen zitiert wurde, die ich überprüft habe. Die Angabe eines Alters von 600 Jahren für die Starkeiche im Rosental von Leipzig war eine Annahme basierend auf den verfügbaren Informationen. Für präzise und aktuelle Informationen über das Alter des Baumes wäre es am besten, direkt bei einer lokalen Behörde oder einer Umweltorganisation in Leipzig nachzufragen, die solche Daten führt oder Forschungen dazu betreibt."_

Das dargestellte Szenario beweist, dass es notwendig ist, Outputs von generativer KI kritisch zu überprüfen. Dies kann einerseits durch gezielte Rückfragen erfolgen. Andererseits können Nutzer auch ChatGPT mit dem (vermeintlich) Korrekten Input konfrontieren: 
![Banner](https://github.com/nih23/Chatbot-Hackathon/blob/main/res/Banner.jpg?raw=true)

# Chatbot-Hackathon

In diesem Repository wird ein Chatbot im Rahmen des Chatbot Hackathons vom KI-Netzwerk Dresden (22.3.2024) entwickelt. Der Chatbot soll öffentliche Daten der Stadt Leipzig zugänglich machen, so dass Jugendliche während eines Jugend hackt Hackathons im Rahmen der Data Week Leipzig mit diesem Chatbot kreativ mit öffentlichen Daten experimentieren können.

# Getting started
Das Python Paket kann mit folgendem Befehl installiert werden:
```pip install -e /Users/nih23/Code/Chatbot-Hackathon```

Das Projekt ist in die Teilmodule **backend**, **data** und **ui** strukturiert. *Backend* stellt Zugriff zu verschiedenen Inferenz-Servern her; *data* stellt Data Loader bereit, die ein Langchain Document zurückliefern und **ui** stellt User Interfaces zur Visualisierung der Chatbot Ergebnisse bereit.

# Hilfreiche Links

**Spannende Datensätze:**
- [Eichhörnchen-Basisdatensatz New York City](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data_preview)
- [Visualisierung der Fellfarben der Eichhörnchen im Central Park](https://data.cityofnewyork.us/Environment/2018-Squirrel-Census-Fur-Color-Map/fak5-wcft)
- [Homepage zur Bürger:innenbeteiligung zum Eichhörnchen-Reporting](https://www.thesquirrelcensus.com/)

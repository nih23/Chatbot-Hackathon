# Erstellen eines OpenAI GPT

Am Beispiel: Versuch von Auswertung der Daten von
[Lebenszufriedenheisdaten](https://opendata.leipzig.de/dataset/zufriedenheitsfaktoren-jahreszahlen-kleinraumig1/resource/38c8e984-ebe0-43c9-ac45-60c47899905e)
Durch Suche auf dem [Statistikportal](https://statistik.leipzig.de/) findet man die weitergehende Beschreibung
https://statistik.leipzig.de/statdist/table.aspx?cat=4&rub=11 .

## Anlegen GPT
Auf https://chat.openai.com/gpts Button "Create"

![Create GPT](img/ErstelleGPT.png)

Es öffnet sich ein Assistent, mit dem man ein GPT anlegen kann.
Als erstes kann man im Reiter Create beschreiben, welchen Zweck des GPT hat. Der Assistent passt dann die 
Konfiguration des GPT an. Auf der rechten Seite im Preview Tab kann man den gegenwärtigen Stand des GPTs jederzeit 
testen. Zum Beispiel:

    Die Aufgabe des GPT ist die Lebenszufriedenheit Daten von Leipzig auszuwerten. Dazu ist eine Datei aus Knowledge 
    eingefügt, die durch den Code Interpret ausgewertet werden kann je nach Anforderung des Nutzers. Die 
    Zusatzinformationen zum Datensatz sind:
    
        Zufriedenheitsfaktoren (Jahreszahlen, kleinräumig)
        Kleinräumige Daten auf Ortsteil- und Stadtbezirksebene zur Zufriedenheit der Bevölkerung (Umfragedaten),
        Mittelwert sehr zufrieden (1) bis sehr unzufrieden (5)

    Wenn es sich anbietet, kann das DBT ein Bild zu Repräsentation der Daten erstellen. 

Das sollte eine Beschreibung des zwecks des GPT enthalten eine möglichst genaue Beschreibung der Daten, die 
hochgeladen sind, und wie die Antworten gewünscht sind.

Im Gespräch mit dem Assistenten können zum Beispiel Name und Bild des GPT festgelegt werden.

Im Reiter Konfiguration müssen dann noch die Daten hochgeladen werden. Das kann zum Beispiel ein CSV oder JSON-File sein. Das GPT kann dann diese Daten je nach Bedarf auswerten. 
Der Reiter Konfiguration zeigt dann auch alle Prompts und Einstellungen des GPT an, die man nach der Ersterstellung 
mit dem Assistenten dann bearbeiten kann, um Feinheiten einzustellen. Die Daten können mit "Upload Files" 
hochgeladen werden.

![Reiter Konfiguration](img/ReiterKonfiguration.png)

Zum Veröffentlichen des GPT ist der Button Create oben rechts zuständig. Die Auswahl "Anyone with a Link" speichert das GPT so ab, dass man es anderen zur Verfügung stellen kann, es aber nicht im GPT-Store veröffentlicht wird. 

![GPT Veroeffentlichen](img/GPTVeroeffentlichen.png)

Das Beispiel-GPT ist [hier verfügbar](https://chat.openai.com/g/g-TITRy4NhJ-lebenszufriedenheitsanalyst-leipzig) .

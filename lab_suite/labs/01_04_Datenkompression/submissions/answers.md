# Fragebogen: Wort-Entropie (word_dictionary.py)

Nach dem Ausführen von `word_dictionary.py` mit eigenem Text in `sampletext.txt`:

**Konsolenausgabe einfügen:** Nutze das Merge-Symbol in der Task-Card, um die Ausgabe aus `console_log.txt` hier einzufügen. Anschließend die Ausgabe **kommentieren**.

---

**1. Konsolenausgabe**

*(Wird per „Konsolenausgabe einfügen“ unten eingefügt. Danach bitte kommentieren.)*

---

**2. Deine Kommentierung**

- Wie unterscheidet sich die Wort-Entropie von der Zeichen-Entropie (entropy1.py)?  
  *[kurz beschreiben]*
  Die Wortentropie ist viel höher als die Zeichenentropie.

- Was sagt die Entropie in Byte im Vergleich zur tatsächlichen Dateigröße aus?  
  *[kurz begründen]*

Die spezifische minimle Daten-Entropie, welche man beim speichern theoretisch erreichen könnte bei Wort-Entropie.

---

## Konsolenausgabe

```
Analyze the file:  /home/student/Documents/KT-course/lab_suite/labs/01_04_Datenkompression/sampletext.txt
Total number of words:     132
Number of different words: 106

-------Table of words:-----------------------------------------
                            und | cnt=  7    p=0.053   H=4.237 bit/word   H_av=0.225 bit/word
                            der | cnt=  5    p=0.038   H=4.722 bit/word   H_av=0.179 bit/word
                         seiner | cnt=  4    p=0.030   H=5.044 bit/word   H_av=0.153 bit/word
                            Die | cnt=  4    p=0.030   H=5.044 bit/word   H_av=0.153 bit/word
                            die | cnt=  3    p=0.023   H=5.459 bit/word   H_av=0.124 bit/word
                           Gold | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                       Metallen | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                          Wegen | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                             es | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                             in | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                       Kulturen | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                  Goldgewinnung | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                            mit | cnt=  2    p=0.015   H=6.044 bit/word   H_av=0.092 bit/word
                          zählt | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                             zu | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            den | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         ersten | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            von | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       Menschen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    verarbeitet | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         wurden | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     auffallend | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     glänzenden | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         gelben | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          Farbe | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          wurde | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     metallisch | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       gediegen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          Natur | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       gefunden | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                             Es | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          lässt | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           sich | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           sehr | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            gut | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     mechanisch | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     bearbeiten | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     korrodiert | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          nicht | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                  Beständigkeit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         seines | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        Glanzes | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     Seltenheit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    scheinbaren | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
              Unvergänglichkeit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                   auffallenden | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        Schwere | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    verwendeten | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          viele | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            vor | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          allem | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            für | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                 herausgehobene | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       rituelle | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    Gegenstände | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        Schmuck | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                 Frühgeschichte | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                   europäisches | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       Altertum | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    Mittelalter | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                 präkolumbische | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     sogenannte | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      Goldmaske | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            des | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      Agamemnon | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            (ca | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           1400 | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                              v | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            Chr | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                              ) | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                             im | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                 Nationalmuseum | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          Athen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            ist | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           seit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         frühen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     Kupferzeit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                   nachgewiesen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        leichte | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                  Legierbarkeit | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                         vielen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       moderate | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
              Schmelztemperatur | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      günstigen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                  Eigenschaften | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    Legierungen | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        machten | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                            als | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      Werkstoff | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      attraktiv | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     -reinigung | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       erfolgte | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                          durch | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                  Goldwäscherei | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                   Amalgamation | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    Kupellation | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                     (Oxidieren | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      unedlerer | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                        Metalle | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           Blei | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           auch | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      Läuterung | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                       genannt) | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                           oder | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                    Kombination | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
                      Verfahren | cnt=  1    p=0.008   H=7.044 bit/word   H_av=0.053 bit/word
-----------------------------------------------------------------

Average Entropy H = 6.529 bit/word
Total Entropy of 132 words H=861.844 bit (108 bytes)
Size of text file: 1053 bytes
```

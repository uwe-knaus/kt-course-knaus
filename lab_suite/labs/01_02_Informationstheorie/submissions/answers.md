# Fragebogen: Entropie-Analyse (entropy1.py)

Nach dem Ausführen von `entropy1.py` mit eigenem Text in `sampletext.txt`:

**Konsolenausgabe einfügen:** Nutze das Merge-Symbol in der Task-Card, um die Ausgabe aus `console_log.txt` hier einzufügen. Anschließend die Ausgabe **kommentieren**.

---

**1. Konsolenausgabe**

*(Wird per „Konsolenausgabe einfügen“ unten eingefügt. Danach bitte kommentieren.)*

---

**2. Deine Kommentierung:**

- Was fällt dir bei der Entropie deines Textes auf?  
  *[z. B. Vergleich mit anderen Texten, Zeichenverteilung, Redundanz]*

Bei 2 zufälligen Texten mit Sinn scheint die Entropie relativ ähnlich zu sein. Die Gesamtentropie hängt dann eher von der Länge ab. Außerdem sind die häfigsten Zeichen Leerzeichen, welche bei texten relativ redundant sein können. Zeichenverteilung scheint nicht wirklich einen Unterschied zu machen.
---

## Konsolenausgabe

```
Analyze the file:  /home/student/Documents/KT-course/lab_suite/labs/01_02_Informationstheorie/sampletext.txt

-----File Contents:---------------------------------------------------
Gold (mittelhochdeutsch golt; bereits althochdeutsch auch gold, zu einer indogermanischen Wurzel *ghel- ‚gelb‘[12]) ist ein chemisches Element mit dem Elementsymbol Au (lateinisch aurum) und der Ordnungszahl 79. Es steht im Periodensystem zusammen mit Kupfer, Silber und Roentgenium in der 1. Nebengruppe (Gruppe 11). Gold gehört zudem zu den Übergangsmetallen und den Edelmetallen.



Bei Gold handelt es sich um ein gelblich glänzendes, inertes, seltenes, relativ weiches und sehr gut verformbares Metall. Es ist der Menschheit bereits seit der Antike bekannt und besitzt einen enormen kulturellen Einfluss als Symbol für Reichtum und Macht. Historisch hat es eine große Rolle als Zahlungsmittel in Form von Goldmünzen gespielt. Viele Kriege und Raubzüge sind auf die Gier nach Gold zurückzuführen.



Es gibt viele Anwendungen von Gold. Von den im Jahre 2024 geförderten etwa 3661[13] Tonnen Gold wurde über die Hälfte von der Schmuckbranche verarbeitet, ein Viertel diente als Geldanlage (Investment), rund 11 % wurde von den Zentralbanken und rund 8 % von der Industrie nachgefragt.[14] In der Natur kommt Gold wegen seiner Reaktionsunlust vor allem in gediegener (elementarer) Form vor. 

Number of characters: 1190
Character Dictionary: {'G': 11, 'o': 35, 'l': 58, 'd': 51, ' ': 173, '(': 5, 'm': 34, 'i': 57, 't': 60, 'e': 150, 'h': 33, 'c': 22, 'u': 45, 's': 48, 'g': 28, ';': 1, 'b': 18, 'r': 60, 'a': 38, ',': 7, 'z': 12, 'n': 90, 'W': 1, '*': 1, '-': 1, '‚': 1, '‘': 1, '[': 3, '1': 9, '2': 3, ']': 3, ')': 5, 'E': 7, 'y': 3, 'A': 3, 'O': 1, '7': 1, '9': 1, '.': 11, 'P': 1, 'K': 2, 'p': 6, 'f': 9, 'S': 3, 'R': 5, 'N': 2, 'ö': 2, 'Ü': 1, '\n': 5, 'B': 1, 'ä': 2, 'v': 12, 'w': 6, 'M': 3, 'k': 8, 'ü': 6, 'H': 2, 'ß': 1, 'Z': 2, 'F': 2, 'V': 3, 'J': 1, '0': 1, '4': 2, '3': 2, '6': 2, 'T': 1, 'I': 3, '%': 2, '8': 1}

-------Table of characters:----------------
       | cnt=173    p=0.145   H=2.782 bit/char  H_av=0.404 bit/char
 e     | cnt=150    p=0.126   H=2.988 bit/char  H_av=0.377 bit/char
 n     | cnt= 90    p=0.076   H=3.725 bit/char  H_av=0.282 bit/char
 t     | cnt= 60    p=0.050   H=4.310 bit/char  H_av=0.217 bit/char
 r     | cnt= 60    p=0.050   H=4.310 bit/char  H_av=0.217 bit/char
 l     | cnt= 58    p=0.049   H=4.359 bit/char  H_av=0.212 bit/char
 i     | cnt= 57    p=0.048   H=4.384 bit/char  H_av=0.210 bit/char
 d     | cnt= 51    p=0.043   H=4.544 bit/char  H_av=0.195 bit/char
 s     | cnt= 48    p=0.040   H=4.632 bit/char  H_av=0.187 bit/char
 u     | cnt= 45    p=0.038   H=4.725 bit/char  H_av=0.179 bit/char
 a     | cnt= 38    p=0.032   H=4.969 bit/char  H_av=0.159 bit/char
 o     | cnt= 35    p=0.029   H=5.087 bit/char  H_av=0.150 bit/char
 m     | cnt= 34    p=0.029   H=5.129 bit/char  H_av=0.147 bit/char
 h     | cnt= 33    p=0.028   H=5.172 bit/char  H_av=0.143 bit/char
 g     | cnt= 28    p=0.024   H=5.409 bit/char  H_av=0.127 bit/char
 c     | cnt= 22    p=0.018   H=5.757 bit/char  H_av=0.106 bit/char
 b     | cnt= 18    p=0.015   H=6.047 bit/char  H_av=0.091 bit/char
 z     | cnt= 12    p=0.010   H=6.632 bit/char  H_av=0.067 bit/char
 v     | cnt= 12    p=0.010   H=6.632 bit/char  H_av=0.067 bit/char
 G     | cnt= 11    p=0.009   H=6.757 bit/char  H_av=0.062 bit/char
 .     | cnt= 11    p=0.009   H=6.757 bit/char  H_av=0.062 bit/char
 1     | cnt=  9    p=0.008   H=7.047 bit/char  H_av=0.053 bit/char
 f     | cnt=  9    p=0.008   H=7.047 bit/char  H_av=0.053 bit/char
 k     | cnt=  8    p=0.007   H=7.217 bit/char  H_av=0.049 bit/char
 ,     | cnt=  7    p=0.006   H=7.409 bit/char  H_av=0.044 bit/char
 E     | cnt=  7    p=0.006   H=7.409 bit/char  H_av=0.044 bit/char
 p     | cnt=  6    p=0.005   H=7.632 bit/char  H_av=0.038 bit/char
 w     | cnt=  6    p=0.005   H=7.632 bit/char  H_av=0.038 bit/char
 ü     | cnt=  6    p=0.005   H=7.632 bit/char  H_av=0.038 bit/char
 (     | cnt=  5    p=0.004   H=7.895 bit/char  H_av=0.033 bit/char
 )     | cnt=  5    p=0.004   H=7.895 bit/char  H_av=0.033 bit/char
 R     | cnt=  5    p=0.004   H=7.895 bit/char  H_av=0.033 bit/char
 b'\n' | cnt=  5    p=0.004   H=7.895 bit/char  H_av=0.033 bit/char
 [     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 2     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 ]     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 y     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 A     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 S     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 M     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 V     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 I     | cnt=  3    p=0.003   H=8.632 bit/char  H_av=0.022 bit/char
 K     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 N     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 ö     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 ä     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 H     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 Z     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 F     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 4     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 3     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 6     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 %     | cnt=  2    p=0.002   H=9.217 bit/char  H_av=0.015 bit/char
 ;     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 W     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 *     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 -     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 ‚     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 ‘     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 O     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 7     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 9     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 P     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 Ü     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 B     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 ß     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 J     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 0     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 T     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
 8     | cnt=  1    p=0.001   H=10.217 bit/char  H_av=0.009 bit/char
-------------------------------------------

Average Entropy H = 4.665 bit/char
Total Entropy of 1190 characters H=5551.15 bit = 694.00 byte
```

---

## Konsolenausgabe

```
Analyze the file:  /home/student/Documents/KT-course/lab_suite/labs/01_02_Informationstheorie/sampletext.txt

-----File Contents:---------------------------------------------------
Gold zählt zu den ersten Metallen, die von Menschen verarbeitet wurden. Wegen seiner auffallend glänzenden gelben Farbe wurde es metallisch gediegen in der Natur gefunden. Es lässt sich sehr gut mechanisch bearbeiten und korrodiert nicht. Wegen der Beständigkeit seines Glanzes, seiner Seltenheit, seiner scheinbaren Unvergänglichkeit und seiner auffallenden Schwere verwendeten es viele Kulturen vor allem für herausgehobene rituelle Gegenstände und Schmuck.

Frühgeschichte, europäisches Altertum und Mittelalter, präkolumbische Kulturen

Die sogenannte Goldmaske des Agamemnon (ca. 1400 v. Chr.) im Nationalmuseum Athen



Die Goldgewinnung ist seit der frühen Kupferzeit nachgewiesen. Die leichte Legierbarkeit mit vielen Metallen, die moderate Schmelztemperatur und die günstigen Eigenschaften der Legierungen machten Gold als Werkstoff attraktiv. Die Goldgewinnung und -reinigung erfolgte durch Goldwäscherei, Amalgamation und Kupellation (Oxidieren unedlerer Metalle mit Blei, auch Läuterung genannt) oder in Kombination der Verfahren. 
Number of characters: 1039
Character Dictionary: {'G': 8, 'o': 24, 'l': 47, 'd': 39, ' ': 128, 'z': 6, 'ä': 10, 'h': 32, 't': 56, 'u': 39, 'e': 155, 'n': 88, 'r': 58, 's': 38, 'M': 5, 'a': 41, ',': 8, 'i': 62, 'v': 9, 'c': 24, 'b': 10, 'w': 8, '.': 10, 'W': 3, 'g': 33, 'f': 13, 'F': 2, 'm': 21, 'N': 2, 'E': 2, 'k': 9, 'B': 2, 'S': 4, 'U': 1, 'K': 5, 'ü': 4, '\n': 4, 'p': 5, 'A': 4, 'D': 4, '(': 2, '1': 1, '4': 1, '0': 2, 'C': 1, ')': 2, 'L': 3, '-': 1, 'O': 1, 'x': 1, 'V': 1}

-------Table of characters:----------------
 e     | cnt=155    p=0.149   H=2.745 bit/char  H_av=0.409 bit/char
       | cnt=128    p=0.123   H=3.021 bit/char  H_av=0.372 bit/char
 n     | cnt= 88    p=0.085   H=3.562 bit/char  H_av=0.302 bit/char
 i     | cnt= 62    p=0.060   H=4.067 bit/char  H_av=0.243 bit/char
 r     | cnt= 58    p=0.056   H=4.163 bit/char  H_av=0.232 bit/char
 t     | cnt= 56    p=0.054   H=4.214 bit/char  H_av=0.227 bit/char
 l     | cnt= 47    p=0.045   H=4.466 bit/char  H_av=0.202 bit/char
 a     | cnt= 41    p=0.039   H=4.663 bit/char  H_av=0.184 bit/char
 d     | cnt= 39    p=0.038   H=4.736 bit/char  H_av=0.178 bit/char
 u     | cnt= 39    p=0.038   H=4.736 bit/char  H_av=0.178 bit/char
 s     | cnt= 38    p=0.037   H=4.773 bit/char  H_av=0.175 bit/char
 g     | cnt= 33    p=0.032   H=4.977 bit/char  H_av=0.158 bit/char
 h     | cnt= 32    p=0.031   H=5.021 bit/char  H_av=0.155 bit/char
 o     | cnt= 24    p=0.023   H=5.436 bit/char  H_av=0.126 bit/char
 c     | cnt= 24    p=0.023   H=5.436 bit/char  H_av=0.126 bit/char
 m     | cnt= 21    p=0.020   H=5.629 bit/char  H_av=0.114 bit/char
 f     | cnt= 13    p=0.013   H=6.321 bit/char  H_av=0.079 bit/char
 ä     | cnt= 10    p=0.010   H=6.699 bit/char  H_av=0.064 bit/char
 b     | cnt= 10    p=0.010   H=6.699 bit/char  H_av=0.064 bit/char
 .     | cnt= 10    p=0.010   H=6.699 bit/char  H_av=0.064 bit/char
 v     | cnt=  9    p=0.009   H=6.851 bit/char  H_av=0.059 bit/char
 k     | cnt=  9    p=0.009   H=6.851 bit/char  H_av=0.059 bit/char
 G     | cnt=  8    p=0.008   H=7.021 bit/char  H_av=0.054 bit/char
 ,     | cnt=  8    p=0.008   H=7.021 bit/char  H_av=0.054 bit/char
 w     | cnt=  8    p=0.008   H=7.021 bit/char  H_av=0.054 bit/char
 z     | cnt=  6    p=0.006   H=7.436 bit/char  H_av=0.043 bit/char
 M     | cnt=  5    p=0.005   H=7.699 bit/char  H_av=0.037 bit/char
 K     | cnt=  5    p=0.005   H=7.699 bit/char  H_av=0.037 bit/char
 p     | cnt=  5    p=0.005   H=7.699 bit/char  H_av=0.037 bit/char
 S     | cnt=  4    p=0.004   H=8.021 bit/char  H_av=0.031 bit/char
 ü     | cnt=  4    p=0.004   H=8.021 bit/char  H_av=0.031 bit/char
 b'\n' | cnt=  4    p=0.004   H=8.021 bit/char  H_av=0.031 bit/char
 A     | cnt=  4    p=0.004   H=8.021 bit/char  H_av=0.031 bit/char
 D     | cnt=  4    p=0.004   H=8.021 bit/char  H_av=0.031 bit/char
 W     | cnt=  3    p=0.003   H=8.436 bit/char  H_av=0.024 bit/char
 L     | cnt=  3    p=0.003   H=8.436 bit/char  H_av=0.024 bit/char
 F     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 N     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 E     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 B     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 (     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 0     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 )     | cnt=  2    p=0.002   H=9.021 bit/char  H_av=0.017 bit/char
 U     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 1     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 4     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 C     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 -     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 O     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 x     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
 V     | cnt=  1    p=0.001   H=10.021 bit/char  H_av=0.010 bit/char
-------------------------------------------

Average Entropy H = 4.489 bit/char
Total Entropy of 1039 characters H=4663.57 bit = 583.00 byte
```

---

## Konsolenausgabe

```
Analyze the file:  /home/student/Documents/KT-course/lab_suite/labs/01_02_Informationstheorie/sampletext.txt

-----File Contents:---------------------------------------------------
Gold zählt zu den ersten Metallen, die von Menschen verarbeitet wurden. Wegen seiner auffallend glänzenden gelben Farbe wurde es metallisch gediegen in der Natur gefunden. Es lässt sich sehr gut mechanisch bearbeiten und korrodiert nicht. Wegen der Beständigkeit seines Glanzes, seiner Seltenheit, seiner scheinbaren Unvergänglichkeit und seiner auffallenden Schwere verwendeten es viele Kulturen vor allem für herausgehobene rituelle Gegenstände und Schmuck.

Frühgeschichte, europäisches Altertum und Mittelalter, präkolumbische Kulturen

Die sogenannte Goldmaske des Agamemnon (ca. 1400 v. Chr.) im Nationalmuseum Athen



Die Goldgewinnung ist seit der frühen Kupferzeit nachgewiesen. Die leichte Legierbarkeit mit vielen Metallen, die moderate Schmelztemperatur und die günstigen Eigenschaften der Legierungen machten Gold als Werkstoff attraktiv. Die Goldgewinnung und -reinigung erfolgte durch Goldwäscherei, Amalgamation und Kupellation (Oxidieren unedlerer Metalle AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmit Blei, auch Läuterung genannt) oder in Kombination der Verfahren. 
Number of characters: 1094
Character Dictionary: {'G': 8, 'o': 24, 'l': 47, 'd': 39, ' ': 128, 'z': 6, 'ä': 10, 'h': 32, 't': 56, 'u': 39, 'e': 155, 'n': 88, 'r': 58, 's': 38, 'M': 5, 'a': 41, ',': 8, 'i': 62, 'v': 9, 'c': 24, 'b': 10, 'w': 8, '.': 10, 'W': 3, 'g': 33, 'f': 13, 'F': 2, 'm': 21, 'N': 2, 'E': 2, 'k': 9, 'B': 2, 'S': 4, 'U': 1, 'K': 5, 'ü': 4, '\n': 4, 'p': 5, 'A': 59, 'D': 4, '(': 2, '1': 1, '4': 1, '0': 2, 'C': 1, ')': 2, 'L': 3, '-': 1, 'O': 1, 'x': 1, 'V': 1}

-------Table of characters:----------------
 e     | cnt=155    p=0.142   H=2.819 bit/char  H_av=0.399 bit/char
       | cnt=128    p=0.117   H=3.095 bit/char  H_av=0.362 bit/char
 n     | cnt= 88    p=0.080   H=3.636 bit/char  H_av=0.292 bit/char
 i     | cnt= 62    p=0.057   H=4.141 bit/char  H_av=0.235 bit/char
 A     | cnt= 59    p=0.054   H=4.213 bit/char  H_av=0.227 bit/char
 r     | cnt= 58    p=0.053   H=4.237 bit/char  H_av=0.225 bit/char
 t     | cnt= 56    p=0.051   H=4.288 bit/char  H_av=0.219 bit/char
 l     | cnt= 47    p=0.043   H=4.541 bit/char  H_av=0.195 bit/char
 a     | cnt= 41    p=0.037   H=4.738 bit/char  H_av=0.178 bit/char
 d     | cnt= 39    p=0.036   H=4.810 bit/char  H_av=0.171 bit/char
 u     | cnt= 39    p=0.036   H=4.810 bit/char  H_av=0.171 bit/char
 s     | cnt= 38    p=0.035   H=4.847 bit/char  H_av=0.168 bit/char
 g     | cnt= 33    p=0.030   H=5.051 bit/char  H_av=0.152 bit/char
 h     | cnt= 32    p=0.029   H=5.095 bit/char  H_av=0.149 bit/char
 o     | cnt= 24    p=0.022   H=5.510 bit/char  H_av=0.121 bit/char
 c     | cnt= 24    p=0.022   H=5.510 bit/char  H_av=0.121 bit/char
 m     | cnt= 21    p=0.019   H=5.703 bit/char  H_av=0.109 bit/char
 f     | cnt= 13    p=0.012   H=6.395 bit/char  H_av=0.076 bit/char
 ä     | cnt= 10    p=0.009   H=6.773 bit/char  H_av=0.062 bit/char
 b     | cnt= 10    p=0.009   H=6.773 bit/char  H_av=0.062 bit/char
 .     | cnt= 10    p=0.009   H=6.773 bit/char  H_av=0.062 bit/char
 v     | cnt=  9    p=0.008   H=6.925 bit/char  H_av=0.057 bit/char
 k     | cnt=  9    p=0.008   H=6.925 bit/char  H_av=0.057 bit/char
 G     | cnt=  8    p=0.007   H=7.095 bit/char  H_av=0.052 bit/char
 ,     | cnt=  8    p=0.007   H=7.095 bit/char  H_av=0.052 bit/char
 w     | cnt=  8    p=0.007   H=7.095 bit/char  H_av=0.052 bit/char
 z     | cnt=  6    p=0.005   H=7.510 bit/char  H_av=0.041 bit/char
 M     | cnt=  5    p=0.005   H=7.773 bit/char  H_av=0.036 bit/char
 K     | cnt=  5    p=0.005   H=7.773 bit/char  H_av=0.036 bit/char
 p     | cnt=  5    p=0.005   H=7.773 bit/char  H_av=0.036 bit/char
 S     | cnt=  4    p=0.004   H=8.095 bit/char  H_av=0.030 bit/char
 ü     | cnt=  4    p=0.004   H=8.095 bit/char  H_av=0.030 bit/char
 b'\n' | cnt=  4    p=0.004   H=8.095 bit/char  H_av=0.030 bit/char
 D     | cnt=  4    p=0.004   H=8.095 bit/char  H_av=0.030 bit/char
 W     | cnt=  3    p=0.003   H=8.510 bit/char  H_av=0.023 bit/char
 L     | cnt=  3    p=0.003   H=8.510 bit/char  H_av=0.023 bit/char
 F     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 N     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 E     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 B     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 (     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 0     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 )     | cnt=  2    p=0.002   H=9.095 bit/char  H_av=0.017 bit/char
 U     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 1     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 4     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 C     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 -     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 O     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 x     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
 V     | cnt=  1    p=0.001   H=10.095 bit/char  H_av=0.009 bit/char
-------------------------------------------

Average Entropy H = 4.531 bit/char
Total Entropy of 1094 characters H=4957.06 bit = 620.00 byte
```

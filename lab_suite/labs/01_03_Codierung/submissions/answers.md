# Fragebogen: Huffman-Codierung (huffman.py)

Nach dem Ausführen des Skripts und **Einfügen der Konsolenausgabe** (Merge-Symbol in der Task-Card):

---

**1. Konsolenausgabe**

*(Wird per „Konsolenausgabe einfügen“ unten eingefügt. Danach bitte kommentieren.)*

---

**2. Deine Kommentierung**

- Was zeigen die ausgegebenen Huffman-Codes?  
  *[kurz beschreiben]*

  Jedem Zeichen wird eine Bit kombination zugeordnet, wobei die Länge der Bitwörter variieren können und häufiger genutzt Buchstaben eher Bit kombination bekommen mit geringer Bitzahl.

- Warum haben häufigere Zeichen kürzere Codewörter?  
  *[kurz begründen]*

  Weil man haüfige Zeichen dann billiger übertragen kann.

---

## Konsolenausgabe

```
Enter the string to compute Huffman Code Tree: ---------------------------------------------------------
Dictionary of Characters with char frequency:       {'A': 2, 'K': 2, 'L': 2, 'H': 1, 'G': 1, 'Z': 1}
Dictionary converted into a list:                   dict_items([('A', 2), ('K', 2), ('L', 2), ('H', 1), ('G', 1), ('Z', 1)])
List of characters sorted to descending frequency:  [('A', 2), ('K', 2), ('L', 2), ('H', 1), ('G', 1), ('Z', 1)]
Huffman Code Dictionary:                            {'L': '00', 'K': '01', 'A': '10', 'H': '110', 'Z': '1110', 'G': '1111'}

 Char | Huffman code 
----------------------
 'A'  |          10
 'K'  |          01
 'L'  |          00
 'H'  |         110
 'G'  |        1111
 'Z'  |        1110
```

---

## Konsolenausgabe

```
Enter the string to compute Huffman Code Tree: ---------------------------------------------------------
Dictionary of Characters with char frequency:       {'A': 2, 'D': 2, 'G': 1, 'T': 2, 'F': 3}
Dictionary converted into a list:                   dict_items([('A', 2), ('D', 2), ('G', 1), ('T', 2), ('F', 3)])
List of characters sorted to descending frequency:  [('F', 3), ('A', 2), ('D', 2), ('T', 2), ('G', 1)]
Huffman Code Dictionary:                            {'D': '00', 'A': '01', 'G': '100', 'T': '101', 'F': '11'}

 Char | Huffman code 
----------------------
 'F'  |          11
 'A'  |          01
 'D'  |          00
 'T'  |         101
 'G'  |         100
```

---

## Konsolenausgabe

```
Enter the string to compute Huffman Code Tree: ---------------------------------------------------------
Dictionary of Characters with char frequency:       {'Ä': 2, 'Ö': 3, 'Ü': 2}
Dictionary converted into a list:                   dict_items([('Ä', 2), ('Ö', 3), ('Ü', 2)])
List of characters sorted to descending frequency:  [('Ö', 3), ('Ä', 2), ('Ü', 2)]
Huffman Code Dictionary:                            {'Ö': '0', 'Ü': '10', 'Ä': '11'}

 Char | Huffman code 
----------------------
 'Ö'  |           0
 'Ä'  |          11
 'Ü'  |          10
```

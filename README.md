# uris - metadata for assigning URIs

URIs are made of two elements, separated by a period: `AuthorURI.TitleOfBook`

1. Author URI is made of two elements: 
2. Book title: (a) Shorten titles to one or two words when possible; (2) Drop the owrd `kitab` from the title **URI Example**: `0748Dhahabi.TarikhIslam` 

# Workflow

1. Use EditPadPro with OpenArabic mARkdown installed
2. Open file `__Entire_Corpus_Working.txt` > text in the file should get automatically highlighted
3. Text files have already been grouped into the same works, but there are mistakes here and there: 1) wrong books grouped together; 2) not all text files that have the text of the same book were grouped together.
4. A new record starts with `######## BEGofRECORD ###########`; the entire bibliography can be folded (`right click > Fold all`) 
5. The line that immediately follows is the line where the `URI` is either already provided or should be added
	1. If the `URI` already exists, nothing needs to be done; in this case the line starts with `#FOLDER#` and is followed immediately by the `URI` of a book (highlighted with orange) and a selection of thematic tags (highlighted with green), for example: `#FOLDER#===# 0748Dhahabi.TarikhIslam (TAGS: BIO, CENT0800, CHR, COL, DHB, PPE, _TABAQAT, _TARAJIM, _TARIKH)`
	2. When the `URI` does not exist, the line starts with one of the following three options (**NB**: options #2 and #3 can be ignored for now, `URIs` for books of #1 only should be provided): 
		1. `#BookURI##===#` (no highlighting) — the `URI` for this book may be added
		2. `#BookURI?##===#` (highlighted with black) — there is no need to add the `URI` for this book for now
		3. `#BookURI-##===#` (highlighted with red) — there is no need to add the `URI` for this book for now

6. **Adding `URIs`**
	1. Make sure that the `URI` of an author does not exist, before creating one; the easiest way to do that is to search for the year of death in Annotation to OpenArabic https://github.com/OpenArabic/Annotation
	2. If it exists, use the existing one; if not, you need to create one

	3. **Creating Author `URI`**:
		1. Author `URI` is made of two elements:  (1) `YEAR of DEATH` (always 4 digits, add zeros in the beginning for dates before 1000 AH); (2) ideally, `SHUHRA` of the author (which are ideosyncratic), for example: `0748Dhahabi`.
		2. Issues with the **date of death**:
			1. If only the century is known, use the last year of that century 4th century hijri > `0400`
			2. If pre-hijri (for example, 56 before hijra), use `0001` 
			3. If current time, use `1450`
		3. Issues with **shuhra**: when it is difficult to identify the `SHUHRA`, use the following elements (as they seems to present in the majority of records)
				1. In this order of priority: `Laqab`, `Kunya`, `Nasab` (`Ibn Fulan`, where `Fulan` is the name of the father)
				3. In this order of priority: `Nisba` geographical; `Nisba` religious; `Nisba` tribal
				4. Examples: `0430AbuNucaymIsbahani`, `0463KhatibBaghdadi`, `0900AbuCabdAllahHimyari`

	4. **Creating Book URI**
		1. Drop the word *kitāb* from the title
		2. Abbreviate the title to the shortest meaningful string, for example: *al-Kāmil fī-l-taʾrīḫ* becomes `Kamil`
		2. Use camelCase when connecting words, for example: *Taʾrīḫ al-islām* becomes `TarikhIslam`
		2. Drop *hamza*s, for example: *Suʾāl*, becomes `Sual`
		3. *ʿAyn*s are transliterated with `c` and capitalized when necessary, for example: ʿAlī becomes `Cali`; *iʿtidāl* becomes `Ictidal` 
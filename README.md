# uris - metadata for assigning URIs

URIs are made of two elements, separated by a period: `AuthorURI.TitleOfBook`

1. Author URI is made of two elements: 
	- `YEAR of DEATH` (always 4 digits, add zeros in the beginning for dates before 1000 AH)
	- `SHUHRA` of the author
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
6. 
 • Add URIs to `Add URI` column • Make sure that URI of an author does not exist, before creating one!  Comment: The easiest way to do that is to search for the year of death in Annotation to OpenArabic  https://github.com/OpenArabic/Annotation • Creating AUTHOR uri  1. Ideally we should use SHUHRAs (which are ideosyncratic)  2. When it is difficult to identify the SHUHRA, I used the following two elements (as they seems to present in the majority of records)  0. Date of death  1. Ibn Fulan (name of the father)  2. Nisba (geographical, religious, tribal)   Issues with dates:  If only the century is known, use the last year of that century  4th century hijri > `0400`  If pre-hijra:  56 before hijra > `0001`  If current time:  > `1450` • Use camelCase when connecting words  Example TarikhIslam < Taʾrīḫ al-islām • Hamzas are dropped  Example: Sual < Suʾāl  • ʿAyns are transliterated with `c` and capitalized when necessary  Example: Cali < ʿAlī  Example: Ictidal < iʿtidāl  
Repository containing program for quizzing word knowledge using customizable word lists.

Shall contain following functions
	Multiple choice questions for word definitions from language A to language B
	<||> from language B to language A
	<||> only for specific word types (verbs, etc.)
	Fit word into sentence

LangB in this case is swedish, meaning that all other language words are 
defined in terms of swedish words

Data in csv format with entries of the form:
File name : <languageA.csv>
<word in langA>, <meaning in langB>, <word type>, <sentences in langA where the word is replaced by ___>

TODO: Add mode game modes and possibility to sort words by type.

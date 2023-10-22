from translate import Translator

print("ENGLISH TO GERMAN TRANSLATOR")
language_sel = ""
language = input("\n1 - German\n2 - French\nSelect a language: ")
if language == "1":
	language_sel = "de"
else:
	language_sel = "fr"

translator = Translator(to_lang=language_sel)

while True:
	user_text = input("Enter text to translate 'q' to quit: ")
	if user_text.lower() == "q":
		break
	translation = translator.translate(user_text)
	print(f"\nYour translation:\n: {translation}")

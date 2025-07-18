from googletrans import Translator, LANGUAGES  # type: ignore

# Function to show available languages
def show_Languages():
    print("\nAvailable Languages:")
    for key, value in LANGUAGES.items():
        print(f'{key} ---- {value}')
    print('\n')

# Function to translate text
def translate_text(text, src_lan, trans_lang):
    translated = Translator().translate(text, src=src_lan, dest=trans_lang)
    return translated.text

# Set source language to English
src = 'en'

# Loop for repeated translation
while True:
    show_Languages()

    trans = input("Enter the language code : ").strip().lower()

    if trans not in LANGUAGES:
        print("Invalid Language Code. Please try again.")
        continue

    text = input("Enter the text in English: ")

    translated = translate_text(text, src, trans)

    print(f"{translated}")

    repeat = input("Do you want to translate again? (y/n): ").strip().lower()
    if repeat == 'n':
        print("Thank you !")
        break

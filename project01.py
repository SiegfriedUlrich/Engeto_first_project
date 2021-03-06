login = dict(
    bob='123',
    ann='pass123',
    mike='password123',
    liz='pass123',
)
separator = "-" * 40
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

user = input('username: ')
password = input("password: ")

if user not in login:
    print("This is not a valid username")
    quit()
elif login.get(user) != password:
    print("This is not a valid password")
    quit()
else:
    print(
        f"{separator}",
        f"Welcome to the app, {user}.".center(len(separator)),
        f"We have {len(TEXTS)} texts to be analyzed.".center(len(separator)),
        f"{separator}",
        sep="\n"
    )

selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if selection.isalpha() or int(selection) == 0 or int(selection) > len(TEXTS):
    print(f"Your input is not supported, please enter"
          f" a number btw. 1 and {len(TEXTS)} to select.")
else:
    clean_text = []
    titlecase_words = []
    upercase_words = []
    lowercase_words = []
    numeric_strings = []

    for word in TEXTS[int(selection) - 1].split():
        clean_word = word.strip(",.:;'-")
        clean_text.append(clean_word)

    for words in clean_text:
        if words.istitle():
            titlecase_words.append(words)
        elif words.isupper() and words.isalpha():
            upercase_words.append(words)
        elif words.islower():
            lowercase_words.append(words)
        elif words.isdigit():
            numeric_strings.append(int(words))

    print(f"There are {len(clean_text)} words in the selected text.",
          f"There are {len(titlecase_words)} titlecase words.",
          f"There are {len(upercase_words)} upercase words.",
          f"There are {len(lowercase_words)} lowercase words.",
          f"There are {len(numeric_strings)} numeric strings.",
          f"The sum of all numbers: {sum(numeric_strings)}", sep="\n"
          )
    print(separator, f" LEN| OCCURRENCES         |NR.".center(40), separator,
          sep="\n")

    frequency = dict()

    for word in clean_text:
        if len(word) not in frequency:
            frequency[len(word)] = 1
        else:
            frequency[len(word)] = frequency[len(word)] + 1

    for index in sorted(frequency.items()):
        print(f"{index[0]}   |"
              f"{index[1] * '*':<20}"
              f" |{index[1]}x".center(len(separator)), sep="\n"
              )

import pandas as pd
import spacy
import random
from spacy.training.example import Example

try:
    df = pd.read_csv(r"C:\Users\manal\OneDrive\Desktop\Legacy\Python Projects\Food and Calories - Sheet1.csv")
except FileNotFoundError:
    print("File not found or wrong path")

print(df.head())

food_calories = df.set_index('Food')["Calories"].to_dict()
# if 'Apple' in food_calories:
#     print(f"Calories in Apple: {food_calories['Apple']}")
# else:
#     print("Apple not found in the dataset. Check food names.")
def check_offsets(nlp, train_data):
    from spacy.training import offsets_to_biluo_tags
    for text, annot in train_data:
        doc = nlp.make_doc(text)
        try:
            offsets_to_biluo_tags(doc, annot["entities"])
        except Exception as e:
            print(f"\n❌ Offset Error in: '{text}'\n{annot['entities']}\n→ {e}\n")



TRAIN_DATA = [
    ("I ate 2 chapatis for lunch.", {"entities": [(6, 7, "QUANTITY_VALUE"), (8, 16, "FOOD_ITEM")]}),
    ("Had a large apple as a snack.", {"entities": [(12, 17, "FOOD_ITEM"), (6, 11, "PORTION_SIZE")]}),
    ("250 grams of paneer for dinner.", {"entities": [(0, 3, "QUANTITY_VALUE"), (4, 9, "QUANTITY_UNIT"), (13, 19, "FOOD_ITEM")]}),
    ("I consumed 1 glass of milk.", {"entities": [(11, 12, "QUANTITY_VALUE"), (13, 18, "QUANTITY_UNIT"), (22, 26, "FOOD_ITEM")]}),
    ("Just ate one bowl of veg pulao.", {"entities": [(9, 13, "QUANTITY_VALUE"), (17, 26, "FOOD_ITEM")]}),
    ("Had some moong dal today.", {"entities": [(9, 18, "FOOD_ITEM")]}), # No explicit quantity
    ("Breakfast was 3 idlis.", {"entities": [(15, 16, "QUANTITY_VALUE"), (17, 22, "FOOD_ITEM")]}),
    ("Ate 150ml of orange juice.", {"entities": [(4, 9, "QUANTITY_VALUE"), (10, 22, "FOOD_ITEM")]}),
   
    # Basic Food Items with Quantity
    ("I ate 2 chapatis for lunch.", {"entities": [(6, 7, "QUANTITY_VALUE"), (8, 16, "FOOD_ITEM")]}),
    ("Had one apple as a snack.", {"entities": [(9, 12, "QUANTITY_VALUE"), (13, 18, "FOOD_ITEM")]}),
    ("Consumed 250 grams of paneer.", {"entities": [(9, 12, "QUANTITY_VALUE"), (13, 18, "QUANTITY_UNIT"), (22, 28, "FOOD_ITEM")]}),
    ("My breakfast was 3 idlis.", {"entities": [(17, 18, "QUANTITY_VALUE"), (19, 24, "FOOD_ITEM")]}),
    ("I had 50 ml of coffee.", {"entities": [(7, 9, "QUANTITY_VALUE"), (10, 12, "QUANTITY_UNIT"), (16, 22, "FOOD_ITEM")]}),
    ("Ate 2 slices of pizza.", {"entities": [(4, 5, "QUANTITY_VALUE"), (6, 12, "QUANTITY_UNIT"), (16, 21, "FOOD_ITEM")]}),

    # Implied Quantities / Portion Sizes
    ("Had a small bowl of dal for dinner.", {"entities": [(8, 13, "PORTION_SIZE"), (21, 24, "FOOD_ITEM")]}),
    ("My lunch was some rice and curry.", {"entities": [(12, 16, "PORTION_SIZE"), (17, 21, "FOOD_ITEM"), (26, 31, "FOOD_ITEM")]}),
    ("Just a little bit of chocolate.", {"entities": [(9, 14, "PORTION_SIZE"), (22, 31, "FOOD_ITEM")]}),
    ("I had some oranges today.", {"entities": [(7, 11, "PORTION_SIZE"), (12, 19, "FOOD_ITEM")]}),
    ("Ate a single chapati.", {"entities": [(4, 10, "QUANTITY_VALUE"), (11, 18, "FOOD_ITEM")]}),

    # Multiple Food Items
    ("Breakfast: 1 banana, 2 eggs, and a glass of milk.", {"entities": [
        (11, 12, "QUANTITY_VALUE"), (13, 19, "FOOD_ITEM"),
        (21, 22, "QUANTITY_VALUE"), (23, 27, "FOOD_ITEM"),
        (35, 40, "QUANTITY_UNIT"), (44, 48, "FOOD_ITEM")
    ]}),
    ("Lunch consisted of roti, sabzi, and a cup of yogurt.", {"entities": [
        (19, 23, "FOOD_ITEM"), (25, 30, "FOOD_ITEM"),
        (37, 40, "QUANTITY_UNIT"), (44, 50, "FOOD_ITEM")
    ]}),
    ("Dinner was chicken biryani with raita.", {"entities": [(12, 26, "FOOD_ITEM"), (32, 37, "FOOD_ITEM")]}),
    ("I had 1 bowl of vegetable soup and 2 slices of bread.", {"entities": [
        (7, 8, "QUANTITY_VALUE"), (9, 13, "QUANTITY_UNIT"), (17, 30, "FOOD_ITEM"),
        (35, 36, "QUANTITY_VALUE"), (37, 43, "QUANTITY_UNIT"), (47, 52, "FOOD_ITEM")
    ]}),
    ("Ate a large burger with fries.", {"entities": [(6, 11, "PORTION_SIZE"), (12, 18, "FOOD_ITEM"), (24, 29, "FOOD_ITEM")]}),


    # Variations in Quantity Expressions
    ("I consumed 1 whole liter of water.", {"entities": [(11, 12, "QUANTITY_VALUE"), (18, 23, "QUANTITY_UNIT"), (27, 32, "FOOD_ITEM")]}),
    ("Had 500g of grapes.", {"entities": [(4, 8, "QUANTITY_VALUE"), (12, 18, "FOOD_ITEM")]}), # "g" is a unit, but 500g is often treated as one token for value+unit
    ("About 200 ml of juice.", {"entities": [(6, 9, "QUANTITY_VALUE"), (10, 12, "QUANTITY_UNIT"), (16, 21, "FOOD_ITEM")]}),
    ("Almost half a cup of milk.", {"entities": [(7, 11, "QUANTITY_VALUE"), (14, 17, "QUANTITY_UNIT"), (21, 25, "FOOD_ITEM")]}),
    ("Three pieces of toast.", {"entities": [(0, 5, "QUANTITY_VALUE"), (6, 12, "QUANTITY_UNIT"), (16, 21, "FOOD_ITEM")]}),
    ("One glass of lassi.", {"entities": [(0, 3, "QUANTITY_VALUE"), (4, 9, "QUANTITY_UNIT"), (13, 18, "FOOD_ITEM")]}),

    # More Indian Food Items
    ("I ate one dosa with sambar.", {"entities": [(6, 9, "QUANTITY_VALUE"), (10, 14, "FOOD_ITEM"), (20, 26, "FOOD_ITEM")]}),
    ("Had two parathas for dinner.", {"entities": [(4, 7, "QUANTITY_VALUE"), (8, 17, "FOOD_ITEM")]}),
    ("Consumed a bowl of poha.", {"entities": [(11, 15, "QUANTITY_UNIT"), (19, 23, "FOOD_ITEM")]}),
    ("My evening snack was vada pav.", {"entities": [(20, 28, "FOOD_ITEM")]}),
    ("Ate a scoop of ice cream.", {"entities": [(6, 11, "QUANTITY_UNIT"), (15, 25, "FOOD_ITEM")]}),
    ("I had a small serving of biryani.", {"entities": [(7, 12, "PORTION_SIZE"), (13, 20, "QUANTITY_UNIT"), (24, 31, "FOOD_ITEM")]}),
    ("Just finished a plate of chole bhature.", {"entities": [(19, 34, "FOOD_ITEM")]}),
    ("Drank 2 glasses of buttermilk.", {"entities": [(6, 7, "QUANTITY_VALUE"), (8, 15, "QUANTITY_UNIT"), (19, 29, "FOOD_ITEM")]}),
    ("My meal included some gulab jamun.", {"entities": [(19, 23, "PORTION_SIZE"), (24, 35, "FOOD_ITEM")]}),
    ("I had a single cup of chai.", {"entities": [(6, 12, "QUANTITY_VALUE"), (13, 16, "QUANTITY_UNIT"), (20, 24, "FOOD_ITEM")]}),

    # General statements (less specific, good for general intent)
    ("I'm logging my food.", {"entities": []}), # No entities here, good negative example
    ("What did I eat today?", {"entities": []}),
    ("Can you help me with calories?", {"entities": []}),
    ("Thanks, that's all.", {"entities": []}),
    ("Hello, bot!", {"entities": []}),

    # More examples with numbers and units
    ("I had 15 ml of syrup.", {"entities": [(6, 8, "QUANTITY_VALUE"), (9, 11, "QUANTITY_UNIT"), (15, 20, "FOOD_ITEM")]}),
    ("Ate 0.5 kg of potatoes.", {"entities": [(4, 8, "QUANTITY_VALUE"), (12, 21, "FOOD_ITEM")]}),
    ("Roughly 1.5 cups of corn.", {"entities": [(9, 13, "QUANTITY_VALUE"), (14, 18, "QUANTITY_UNIT"), (22, 26, "FOOD_ITEM")]}),
    ("2 large bananas.", {"entities": [(0, 1, "QUANTITY_VALUE"), (2, 7, "PORTION_SIZE"), (8, 15, "FOOD_ITEM")]}),
    ("About 300g of chicken breast.", {"entities": [(6, 10, "QUANTITY_VALUE"), (14, 28, "FOOD_ITEM")]}),
]

nlp = spacy.blank("en")
check_offsets(nlp, TRAIN_DATA)
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

for _,annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"] #cox NER will not exactly look at word chappati in isolation , it needs to understand its word context and grammatical roles or its neighbours. It 
other_pipe = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*other_pipe): #(*) is an unpacking operator as disable_pipe accepts just individual pipe names and not list
    optimizer = nlp.begin_training()
    cleaned_training_data = []  
    for epoch in range(30):
        random.shuffle(TRAIN_DATA)
        losses = {}

        for data,annotations in TRAIN_DATA:
            doc = nlp.make_doc(data) #helps tokenize data
            example = Example.from_dict(doc,annotations) #This line pairs your tokenized input text (doc) with its corresponding correct answers (annotations). This Example object is what spaCy's training algorithm uses to learn.
            nlp.update([example], drop=0.5, losses=losses, sgd=optimizer)

           

            

nlp.to_disk('./food_ner_models')
print("Model saved to ./food_ner_model")

# Testing time
# Load the saved model
nlp_loaded = spacy.load("./food_ner_models")

#test sentences
TEST_SENTENCES = [
    "I had 100ml of milk and some cerial in breakfast",
    "My mood was off so I ate a pineapple pastry to recharge it !",
    "I love drinking coffee , so i just had a shot of espresso.",
    "I had a sandwhich but that didnt go well so i added a slice of extra cheese.",
     "Today I had a small apple and 100 grams of moong dal.",
    "My dinner was one portion of chicken curry.",
    "Just had some tea.",
    "Consumed 50ml of orange juice."
]

for test in TEST_SENTENCES:
    doc = nlp_loaded(test)
    print(f"original text {test}")
    for ent in doc.ents:
         print(f"  - Entity: '{ent.text}', Label: '{ent.label_}', Start: {ent.start_char}, End: {ent.end_char}")

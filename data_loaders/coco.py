import json
import io
from tensorflow.python.keras import preprocessing

CAPTIONS_DIR = '../annotations/captions_val2017.json'
IMAGES_DIR = 'val2017'

caption_file = io.open(CAPTIONS_DIR)

caption_json = json.load(caption_file)

annotations = caption_json["annotations"]
annotation_count = len(annotations)
tokenizer = preprocessing.text.Tokenizer(num_words=10)

for annotation in annotations:
    image_id = annotation["image_id"]
    caption = annotation["caption"]
    tokenizer.fit_on_texts(caption)
    a = tokenizer.texts_to_sequences(caption)
    print(str(image_id) + ": " + caption)
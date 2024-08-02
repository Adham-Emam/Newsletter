from mtranslate import translate
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize


def paraphraser(sentence):
    translation = translate(
        sentence,
        "en",
        "ar",
    )

    # nltk.download("punkt")  # Download NLTK tokenizer models if not already downloaded
    # nltk.download("wordnet")  # Download WordNet if not already downloaded

    paraphrased_sentence = paraphrase_sentence(translation)

    ar_translation = translate(paraphrased_sentence, "ar", "en")

    return ar_translation


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)


def paraphrase_sentence(sentence):
    words = word_tokenize(sentence)
    paraphrased_sentence = []
    for word in words:
        synonyms = get_synonyms(word)
        if synonyms:
            paraphrased_sentence.append(
                synonyms[0]
            )  # Choose the first synonym as a simple paraphrase
        else:
            paraphrased_sentence.append(word)
    return " ".join(paraphrased_sentence)

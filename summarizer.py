import numpy as np
from Sum import tokenizer
from Sum import tr


def get_summary_from_text_file(rawtext):

    text = rawtext
    stop_words = open(
        "C:/nts/Sum/stopwords.txt", 'r', encoding="utf-8").read()
    word_endings = open(
        "C:/nts/Sum/word_endings.txt", 'r', encoding='utf-8').read()
    valid_characters = tokenizer.get_valid_chars()
    # print(stop_words.split("\n"))
    # print(text)

    text = tokenizer.remove_useless_characters(text, valid_characters)
    print(text)

    sentences = tokenizer.get_sentences_as_arr(text)
    words_arr = tokenizer.get_words_as_arr(sentences)

    words_arr = tokenizer.remove_stop_words_and_filter_word_arr(
        words_arr, word_endings, stop_words,)
    # print(words_arr)

    sentences, words_arr = tokenizer.remove_empty_sentences(sentences, words_arr)

    tokens, token_dict = tokenizer.tokenize(words_arr)

    association_matrix, counter_vector = tr.create_association_matrix(tokens, No_of_unique_chars=len(token_dict))

    word_influence_vector = tr.calculate_word_ranks(association_matrix, counter_vector)

    sentence_influence = tr.calculate_sentence_influence(tokens, word_influence_vector)

    summary_sentences = tr.get_n_influencial_sentence(sentences, sentence_influence, n=np.ceil(len(sentences)*0.55))

    summarized_text = tr.get_summarized_text(summary_sentences)

    # print(summarized_text)
    return summarized_text
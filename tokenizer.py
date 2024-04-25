import numpy as np
import json


def get_valid_chars():
    valid_characters = list(json.load(open(
        'C:/nts/Sum/valid_chars.json', 'r', encoding="utf-8")).keys())
    return valid_characters


def remove_useless_characters(text, valid_characters):
    valid_text = ''
    for chars in text:
        if chars in valid_characters:
            valid_text += chars
    # print(valid_text)
    return valid_text


def get_sentences_as_arr(text):
    arr = text.split('।')
    return arr


def remove_stop_words_and_filter_word_arr(word_arr, word_endings, stop_words):
    stop_words = stop_words.split('\n')
    new_word_arr = []
    word_endings = word_endings.split("\n")
    for sentences in word_arr:
        new_sentences = []
        for words in sentences:
            for endings in word_endings:
                if words.endswith(endings):
                    words = words[:-len(endings)]
                    # print(f"endings = {endings}, word = {words}")
                    break
            # print(words)
            for st_word in stop_words:
                if st_word == words:
                    # print(words)
                    break
            new_sentences.append(words)
        # print(new_sentences)
        new_word_arr.append(new_sentences)
    return new_word_arr


def get_words_as_arr(sentence_arr):
    ret_arr = []
    for sentence in sentence_arr:
        word_arr = sentence.split(" ")
        ret_arr.append(word_arr)
    return ret_arr


def remove_empty_sentences(sentences, words_arr):
    new_sentences = []
    new_words_arr = []
    for (sent, sent_arr) in zip(sentences, words_arr):
        if len(sent_arr) > 1:           
            new_sentences.append(sent)
            new_words_arr.append(sent_arr)

    return new_sentences, new_words_arr


def search_and_get_index(arr, val):
    for i, item in enumerate(arr):
        if item == val:
            return i
    return -1


def tokenize(word_arr):
    word_list = []
    tokenized_sentence = []
    count = 0
    for sentence in word_arr:
        token_words = []
        for word in sentence:
            ind = search_and_get_index(word_list, word)
            if ind == -1:
                word_list.append(word)
                token_words.append(count)
                count += 1
            else:
                token_words.append(ind)
        tokenized_sentence.append(token_words)
    return tokenized_sentence, word_list
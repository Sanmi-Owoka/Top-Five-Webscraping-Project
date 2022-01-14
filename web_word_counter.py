class WordCounter:
    word_num = 7
    def word_counter(self, word_list):
        """dictionary containing all words and word_count"""
        count_dict = {word: word_list.count(word) for word in word_list}

        """dictionary containing all words and word_count in descending order"""
        sorted_count_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))

        """list containing highest numbers of words with the amount specified in word_num"""
        seven_highest_words_list = list(sorted_count_dict.items())[:self.word_num]

        """dictionary containing highest number of words and word_count"""
        seven_highest_words_dict= dict(seven_highest_words_list)

        """list containing highest number of words"""
        highest_word_list = list(seven_highest_words_dict.keys())
        print(f"The top word is: {highest_word_list[0]}")
        return seven_highest_words_dict

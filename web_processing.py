from utils import utils


class WebProcess:
    def text_process(self, web_content):
        web_text = web_content.replace("\n", "  ").replace(u'\xa0', u' ')
        web_text_list = web_text.split(" ")
        """step to filter all none alphabets"""
        web_text_filter = [word.title() for word in web_text_list if word.isalpha()]

        """step to remove all common words using the common words list from the utils module"""
        web_common_word_filter = [word for word in web_text_filter if word.lower() not in utils.common_words]
        return web_common_word_filter









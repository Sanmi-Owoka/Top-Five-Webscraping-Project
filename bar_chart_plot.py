from matplotlib import pyplot as plt


class BarChart:
    def plot_bar_chart(self, seven_highest_words_dict):
        """Graph x-axis= data_x and y-axis= data_y"""
        data_x = list(seven_highest_words_dict.keys())
        data_y = list(seven_highest_words_dict.values())
        plt.bar(data_x, data_y, color="#3a3f5c")
        plt.xlabel("WORDS")
        plt.ylabel("WORD'S COUNT")
        plt.title("Graph of Highest Numbers of Word")
        plt.show()

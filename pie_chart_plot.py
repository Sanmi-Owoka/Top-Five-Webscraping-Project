from matplotlib import pyplot as plt


class PieChart:

    def plot_pie_chart(self, seven_highest_words_dict):
        data_x = list(seven_highest_words_dict.keys())
        data_y = list(seven_highest_words_dict.values())
        explode = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        plt.pie(data_y, labels=data_x, wedgeprops={"edgecolor": "white"}, autopct="%1.1f%%", explode=explode)
        plt.title("Graph of Highest Numbers of Word")
        plt.show()


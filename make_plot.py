from dateutil.parser import parse
from numpy import cumsum
import matplotlib.pyplot as plt


with open("blog_data.tsv", "r") as file:
    blog = [line.split('\t') for line in file]

with open("book_data.tsv", "r") as file:
    books = [line.split('\t') for line in file]

book_dates = [parse(dt[0]) for dt in books]
book_dates = [book_dates[i] for i in [0, 1, 3, 4, 6, 8, -1]]
blog_dates = [parse(dt[0]) for dt in blog]

book_words = cumsum([int(dt[1]) for dt in books])
book_words = [book_words[i] for i in [0, 1, 3, 4, 6, 8, -1]]
blog_words = cumsum([int(dt[1]) for dt in blog])


plt.plot_date(book_dates[:-1], book_words[:-1], '.-', label='Books')
plt.plot_date(blog_dates, blog_words, '-', label='Blog entries')
plt.plot_date(book_dates[-2:], book_words[-2:], '.--', c='b')
plt.legend(loc='best')
plt.ylabel('word count', rotation='horizontal')
plt.axes().yaxis.set_label_coords(0, 1.02)
plt.show()

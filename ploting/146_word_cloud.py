from wordcloud import WordCloud
import matplotlib.pyplot as plt


words_array = ["data", "science", "python", "data", "analysis", "visualization", 
               "python", "machine", "learning", "python", "data", "AI"]

words_string = " ".join(words_array)

wordcloud = WordCloud(width=800, height=400).generate(words_string)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="gaussian")
plt.axis("off")
plt.title("Word Cloud Example")
plt.show()

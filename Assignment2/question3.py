import matplotlib.pyplot as plt

# Data given for plotting
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["blue", "orange", "green", "red", "violet", "brown"]
# Exploding Java part
explode = (0.1, 0, 0, 0, 0, 0)
# Plot in the pie chart
plt.pie(popularity, startangle=140, labels=languages, explode=explode, colors=colors, shadow=True
        , wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
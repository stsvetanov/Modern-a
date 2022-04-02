from Lecture_24_services_v2.movies.movies_api_config import themoviedb_apikey
import locale
import pandas
import matplotlib
import matplotlib.pyplot as plt
import requests
from matplotlib.ticker import FuncFormatter # to format currency on charts axis
locale.setlocale(locale.LC_ALL, 'en-US')

api_key = themoviedb_apikey

response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key + '&primary_release_year=2017&sort_by=revenue.desc')
highest_revenue = response.json() # store parsed json response

# uncomment the next line to get a peek at the highest_revenue json structure
print(highest_revenue)

highest_revenue_films = highest_revenue['results']

# define column names for our new dataframe
columns = ['film', 'revenue']

# create dataframe with film and revenue columns
df = pandas.DataFrame(columns=columns)

# for each of the highest revenue films make an api call for that specific movie to return the budget and revenue
for film in highest_revenue_films:
    # print(film['title'])
    film_revenue = requests.get('https://api.themoviedb.org/3/movie/'+ str(film['id']) +'?api_key='+ api_key+'&language=en-US')
    film_revenue = film_revenue.json()
    # print(locale.currency(film_revenue['revenue'], grouping=True ))
    df.loc[len(df)] = [film['title'], film_revenue['revenue']] # store title and revenue in our dataframe

print(df.head())


matplotlib.style.use('ggplot')
fig, ax = plt.subplots()
df.plot(x='film', y='revenue', kind="barh",  color=['#624ea7', '#599ad3', '#f9a65a', '#9e66ab', 'purple'], ax=ax)

# format xaxis in terms of currency
formatter = FuncFormatter(locale.currency)
ax.xaxis.set_major_formatter(formatter)
ax.legend().set_visible(False)

avg = df['revenue'].mean()

# Add a line for the average
ax.axvline(x=avg, color='b', label='Average', linestyle='--', linewidth=1)

ax.set(title='American Films with Highest Revenue (2017)', xlabel='Revenue', ylabel='Film')
plt.show()

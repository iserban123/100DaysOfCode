from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
answer = response.text
soup = BeautifulSoup(answer, "html.parser")
print(soup.prettify())
movie = soup.find_all(name="h3",class_="title")
movie_titles = [mov.getText() for mov in movie]
movies = movie_titles[::-1]
print(movies)
with open("movie.text", mode="w") as file:
    for m in movies:
        file.write(f"{m}\n")

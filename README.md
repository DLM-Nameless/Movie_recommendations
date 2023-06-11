# Movie_recommendations



## Members

* [Mariela Yael Arias Rojo](https://github.com/marielaAriass)
* [Leonardo Ariel Tapia Figueroa](https://github.com/leotapia11)
* [Débora Joselyn Tolentino Díaz](https://github.com/Debytd)

Final Project for the Distributed Computing 2023-2 class, for the Universidad Nacional Autónoma de México (National Autonomous University of México | UNAM), in Escuela Nacional de Estudios Superiores Unidad Morelia Campus (National School of Superior-Level Studies, Morelia Campus | ENES Morelia).

The contents of this repository are licensed under the GNU General Public License version 3. Visit https://www.gnu.org/licenses/gpl-3.0.html for more information.

## Introduction
Whenever we try to watch a movie, we tend to spend up to a few hours choosing a movie to watch. 

## Definition 
Creating a platform that collects information about movies, such as title, genre, rating, streaming platform where it's available, and popularity, so you can make personalized recommendations. By asking questions like streaming platform or genre of interest, the platform could filter the options and provide accurate and relevant suggestions for the user.

## General Objective
- Offer personalized movies recommendations based on the user's information that has been collected through a short questionnaire.

## Objectives
- Collect relevant information from movies: Collect detailed information about movies, such as genre, plot, rating, etc.
- Ellaborate an algorithm which can provide movie recommendations that fit the user's tastes. The personalized recommendation can increase user satisfaction and increase the likelihood that they will return to the page.
- Create an engaging user experience: By making the movie search process easier and more comfortable for the user, you can create a more engaging user experience.

## General system architecture
![General system architecture](https://user-images.githubusercontent.com/100146837/233822542-40df160a-978c-427c-81cd-b597208b44f9.jpg)

## Toolset
The project is to be developed by making use of modern [Python 3](https://www.python.org/) libraries, including but not limited to:
* [Dash](https://dash.plotly.com/)
* [json](https://docs.python.org/es/3/library/json.html)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)

In addition we use:
* [TMDb API](https://www.themoviedb.org/documentation/api)

## Methodogoly
The project starts with the creation of a spider that crawls the required data from the TMDb API, followed by a script for the creation of a database that contains the following data of the obtained movies: title, genre, rating, views, release date and streaming platform where available.

Subsequently, the production script is responsible for creating an interactive platform where you can find the most popular movies of the moment. A menu is also displayed with the options of genres and streaming platforms, where the user can choose the one of their interest. At the time of selection, the 10 films with the best rating will be shown.

## Results
The result is a platform in which we can choose the genre of the movies that we are interested in watching and the streaming platform that we have available.
![01](https://github.com/DLM-Nameless/Movie_recommendations/assets/100146837/5fd1fa74-1f2d-45a7-8192-e26a2ef319b7)
![02](https://github.com/DLM-Nameless/Movie_recommendations/assets/100146837/c922f940-17a8-477d-88b8-33663a20a599)

And the most viewed movies of the moment will be shown. 
![03](https://github.com/DLM-Nameless/Movie_recommendations/assets/100146837/b8994483-3b26-47b3-8e7e-8dfae36daf7b)

## Conclusions

In our daily life, when we have to choose a movie to watch, we don't have an idea of all the available options, but with this prototype, we can get great help.

It is concluded that it is necessary to continue working to provide a product that is increasingly simple and smarter. However, the current prototype is functional and can be easily implemented in a distributed system, as expected from this project.

## References
According to the documentation available at [this link](https://dash.plotly.com/dash-enterprise/database-connections?de-version=5.1), you can get more information about database connections in Dash Enterprise.





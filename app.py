import streamlit as st
import pickle
import pandas as pd
import requests
st.title("Welcome to Movie recomended system")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
option = st.selectbox(
     'Select your favorite movie',
     movies['title'].values)

st.write('You selected:', option)
def recommend(movie):
     mymovies=[]
     posters=[]
     index = movies[movies['title'] == movie].index[0]
     distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
     for i in distances[1:11]:
          movie_id = movies.iloc[i[0]].movie_id
          posters.append(fetch_poster(movie_id))
          mymovies.append(movies.iloc[i[0]].title)
     return mymovies,posters
if st.button('recommend'):
     moviesname,posters=recommend(option)
     col1, col2, col3, col4, col5,col6,col7,col8,col9,col10 = st.columns(10)
     with col1:
          st.image(posters[0]+"          ")
          st.text(moviesname[0]+"        ")

     with col2:
          st.image(posters[1]+"                ")
          st.text(moviesname[1]+"              ")


     with col3:
          st.image(posters[2]+"          ")
          st.text(moviesname[2]+"        ")

     with col4:
          st.image(posters[3]+"          ")
          st.text(moviesname[3]+"        ")

     with col5:
          st.image(posters[4])
          st.text(moviesname[4])
     with col6:
          st.image(posters[5])
          st.text(moviesname[5])
     with col7:
          st.image(posters[6])
          st.text(moviesname[6])
     with col8:
          st.image(posters[7])
          st.text(moviesname[7])
     with col9:
          st.image(posters[8])
          st.text(moviesname[8])

     with col10:
          st.image(posters[9])
          st.text(moviesname[9])

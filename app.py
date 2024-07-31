import streamlit as st
import pickle
import pandas as pd


# method for recommend
def Recommend(selected_movie_name):
     
    idx = indices()[selected_movie_name]
    
    sig_scores = list(enumerate(sigmoid[idx]))
    
    sig_scores = sorted(sig_scores,key = lambda x:x[1],reverse=True)
    
    sig_scores = sig_scores[1:6]
    
    recommended_movies = []
    movies_indices = [i[0] for i in sig_scores]
    
    return movies['original_title'].iloc[movies_indices]


#imported movies pkl file
movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)
movies = movies_list[['original_title']]

#imported sigmoid function file
sigmoid = pickle.load(open('sigmoid.pkl','rb'))

#imported indices function
indices = pickle.load(open('indices.pkl','rb'))

st.title('Movie Recommender System')

#option box
selected_movie_name=st.selectbox(
    'How would you like to start?',
    movies )

#recommend button
if st.button('Recommend'):
    r = Recommend(selected_movie_name)
    
    for i in r:
     st.write(i)




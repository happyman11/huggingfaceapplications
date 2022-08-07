#%%
###import packages

#
import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
import pandas as pd
import time
import openpyxl  
import base64   

#%%
st.set_page_config(layout="wide")


# Text/Title

with st.container():
    components.html(
     """
     <div style="position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   color: black;
   
   text-align: center;">
  <h1>Text Generator</h1>
</div>
     """,height=50,)

#%%
#Navigation bar
with st.container():
 #navbar 
#https://bootsnipp.com/snippets/nNX3a     https://www.mockplus.com/blog/post/bootstrap-navbar-template
   components.html(
       """
       <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<!------ Include the above in your HEAD tag ---------->
<nav class="navbar navbar-icon-top navbar-expand-lg navbar-dark bg-dark" >
  <a class="navbar-brand" href="https://www.rstiwari.com" target="_blank">Profile</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href=" https://tiwari11-rst.medium.com/" target="_blank" >
          <i class="fa fa-home"></i>
          Medium
          <span class="sr-only">(current)</span>
          </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href=" https://happyman11.github.io/" target="_blank">
          <i class="fa fa-envelope-o">
            <span class="badge badge-danger">Git Pages</span>
          </i>
         
        </a>
      </li>
      
        <li class="nav-item">
        <a class="nav-link" href="https://happyman11.github.io/" target="_blank">
          <i class="fa fa-globe">
            <span class="badge badge-success">Badges</span>
          </i>
         
        </a>
      </li>
          
        </a>
      </li>
      
      <li class="nav-item">
        <a class="nav-link disabled" href="https://ravishekhartiwari.blogspot.com/" target="_blank">
          <i class="fa fa-envelope-o">
            <span class="badge badge-warning">Blogspot</span>
          </i>
          
        </a>
      </li>
      
      
    </ul>
  
    
  </div>
</nav>
       """, height=70,
    )



###
generator = pipeline("text-generation")
def analysis_sentence(comments):

    output=generator(comments,max_length=100)
    return (output)
    
    

        
def format_output(ouput):
    
    
    dict_op=output[0]
    formatted_output=dict_op["generated_text"]
                       
                        
    return(formatted_output) 
    




with st.container():
     
     col10, col11, col12 = st.columns([2,4,3])   
     with col11:
         sentiments= st.text_input("Sentence","Type  here...")



with st.container():
     
     col10, col11, col12 = st.columns(3)   
     with col11:
         Submitted=st.button("Process")

if (Submitted):
    output=analysis_sentence(sentiments)
    with st.spinner('Formatting output '):
     time.sleep(5)
     
    analysis=format_output(output)
    
    
    st.header("Input Sentence")
    st.write(sentiments)
    
    st.header("Prediction from Model")
    st.write(analysis)    



##add for excel


 
#footer

with st.container():
    components.html(
     """
     <div style="position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: black;
   color: white;
   text-align: center;">
  <p>Ravi Shekhar Tiwari</p>
</div>
     """,height=140,)
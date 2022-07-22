from sentence_transformers import SentenceTransformer, util
import pandas as pd

from dbconnection import db_model

def corpus_fun_public():

    # Return DataFrame from DataBase
    df = db_model.database_connection()
    # df = pd.read_csv("COVID19_web_CLEAN.csv")


    # Select Column
    corpus = df['scientific_title'].values

    # len(df['Scientific title'][df['Scientific title'].isnull()])
    # len(df['Public title'][df['Public title'].isnull()])
    # len(df['Primary outcome'][df['Primary outcome'].isnull()])
    
    # Get corpus from column in dataframe
    model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)

    # Return Corpus
    return corpus, model, corpus_embeddings


# def corpus_fun_scientific():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['SCIENTIFIC TITLE'].values
    
#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings


# def corpus_fun_study_design():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['STUDY DESIGN'].values

#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings


# def corpus_fun_inclusion_criteria():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['INCLUSION CRITERIA'].values

#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings


# def corpus_fun_exclusion_criteria():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['EXCLUSION CRITERIA'].values

#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings


# def corpus_fun_condition():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['CONDITION'].values

#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings

# def corpus_fun_primary_outcome():
#     # df = db_model.database_connection()
#     df = pd.read_csv("COVID19_web_CLEAN.csv")

#     corpus = df['PRIMARY OUTCOME'].values

#     model = SentenceTransformer('sentence-transformers/msmarco-MiniLM-L-6-v3')
#     corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
#     return corpus, model, corpus_embeddings
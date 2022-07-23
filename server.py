from pickle import TRUE
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

from models import corpusModel, searchModel
from dbconnection import db_query

corpus_1, model_1, corpus_embeddings_1 = corpusModel.corpus_fun_public()
# corpus_2, model_2, corpus_embeddings_2 = corpusModel.corpus_fun_scientific()
# corpus_3, model_3, corpus_embeddings_3 = corpusModel.corpus_fun_study_design()
# corpus_4, model_4, corpus_embeddings_4 = corpusModel.corpus_fun_inclusion_criteria()
# corpus_5, model_5, corpus_embeddings_5 = corpusModel.corpus_fun_exclusion_criteria()
# corpus_6, model_6, corpus_embeddings_6 = corpusModel.corpus_fun_condition()
# corpus_7, model_7, corpus_embeddings_7 = corpusModel.corpus_fun_primary_outcome()


app = Flask(__name__)
CORS(app)

# Version
@app.route("/") 
def api_main(): 
    version = {
      "name": "Analytics_API",
      "version":"0.0.0"
    }
    return jsonify(version)

# Search Model
@app.route('/search', methods=['POST'])
def api_search_model():

    jsondata = request.json
    query= jsondata['query']
    answers=int(jsondata['answers'])

    # Public Title
    index_1, scores_1 = searchModel.search(query,answers,corpus_1, model_1, corpus_embeddings_1)
    # # Scientific Title
    # index_2, scores_2 = searchModel.search(query,answers,corpus_2, model_2, corpus_embeddings_2)
    # # Study Design
    # index_3, scores_3 = searchModel.search(query,answers,corpus_3, model_3, corpus_embeddings_3)
    # # Inclusion Criteria
    # index_4, scores_4 = searchModel.search(query,answers,corpus_4, model_4, corpus_embeddings_4)
    # # Exclusion Criteria
    # index_5, scores_5 = searchModel.search(query,answers,corpus_5, model_5, corpus_embeddings_5)
    # # Condition
    # index_6, scores_6 = searchModel.search(query,answers,corpus_6, model_6, corpus_embeddings_6)
    # # Primary Outcome
    # index_7, scores_7 = searchModel.search(query,answers,corpus_7, model_7, corpus_embeddings_7)

    output_data = {
                  # Public Title
                  'index_1': index_1, 
                  'scores_1' : scores_1, 

                  # # Scientific Title
                  # 'index_2': index_2, 
                  # 'scores_2' : scores_2, 

                  # # Study Design
                  # 'index_3': index_3, 
                  # 'scores_3' : scores_3, 

                  # # Inclusion Criteria
                  # 'index_4': index_4, 
                  # 'scores_4' : scores_4, 

                  # # Exclusion Criteria
                  # 'index_5': index_5, 
                  # 'scores_5' : scores_5, 

                  # # Condition
                  # 'index_6': index_6, 
                  # 'scores_6' : scores_6, 

                  # # Primary Outcome
                  # 'index_7': index_7, 
                  # 'scores_7' : scores_7, 
                    }

    print(output_data)
    return jsonify(output_data)

# Database conection
@app.route('/query', methods=['POST'])
def api_query():

    jsondata = request.json
    query= jsondata['query']

    output_data = db_query.database_connection(query)

    return output_data.to_json(orient='records')


app.run(port=(8000), debug=TRUE) 
"""Data Structure Out put
    { 'Orgingin':'Kindofmodel',  'OutputData':[[1,2,3],[1,2,3]]}
"""
from numpy.ma.core import append
import pandas as pd
from sentence_transformers import util
import torch



def search(query, answers, corpus, model, corpus_embeddings):
  top_k = min(answers, len(corpus))

  query_embedding = model.encode(query, convert_to_tensor=True)

  # We use cosine-similarity and torch.topk to find the highest 5 scores
  cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
  top_results = torch.topk(cos_scores, k=top_k)

  index = []
  scores = []
  for score, idx in zip(top_results[0], top_results[1]):
      #print(idx.item())
      #print(corpus[idx], "(Score: {:.4f})".format(score))
      index.append(idx.item())
      scores.append(score.item())


  return index, scores
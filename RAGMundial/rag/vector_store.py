from langchain_openai import OpenAIEmbeddings
import numpy as np

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

text1 = "La capital de Francia es Paris"
text2 = "Paris es un nombre común para mascotas"

vec1 = embeddings.embed_query(text1)
vec2 = embeddings.embed_query(text2)

print(f"Dimension de los vectores: {len(vec1)}")

cos_sin = np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print(f"Similitud coseno entre vec1 y vec2: {cos_sin:.3f}")
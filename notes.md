### NER Methods



#### GLiNER 
- https://arxiv.org/pdf/2311.08526
- utilizes smaller scale Bidirectional Language Models (BiLM), e.g. BERT or deBERTa.
- treates the task of Open (identification of any type) NER as matching entity type embeddings to textual span representations in latent space
- has three main components:
     - pre-trained textual encoder (e.g. deBERTa)
     - a span representation module which computes span embeddings from token embeddings
     - an entity representation module which computes entity embeddings that model seeks to extract



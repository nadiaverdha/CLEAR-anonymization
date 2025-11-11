### NER Methods



#### GLiNER 
- https://arxiv.org/pdf/2311.08526
- utilizes smaller scale Bidirectional Language Models (BiLM), e.g. BERT or deBERTa.
- treates the task of Open (identification of any type) NER as matching entity type embeddings to textual span representations in latent space
- has three main components:
     - pre-trained textual encoder (e.g. deBERTa)
     - a span representation module which computes span embeddings from token embeddings
     - an entity representation module which computes entity embeddings that model seeks to extract



#### BANER (Boundary-Aware LLMs for Few-Shot Named Entity Recongnition)
- https://aclanthology.org/2025.coling-main.691.pdf
- it introduces a novel few-shot NER approach which employs boundary-aware contrastive learning to enhance an LLM's ability to perceive entity boundaries
- uses LoRAHub
- comprises:
    - entity span detection
        - prompt representation 
            - BANER fine-tunes LLM using LoRA (updates only small parameters) and prompts
            - prompt is fed into the LLM to perform entity span detection
        - boundary-aware contrastive learning (Khosla et al., 2020)
            - teaches the model to distinguish correct entity boundaries
    - entity type classification
        - a specific entity class is assiged to each span identified during entity span detection

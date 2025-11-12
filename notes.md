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
- recently few shot NER have gathered a lot of attention
    - prompt-based methods: leverage the knowledge of LLMs by utilizing templates, prompts, etct to effectively harness the internal knowledge of LLMs
    - metric-based methods: aim to learn the future space w/ robust generalizability and classify test samples using nearest class protorypes / or neighboring samples; may fail to fully utilize entity type knowledge from the source domain during type classification stage..
    - recently the focus -> two stage architecture,task is decomposed into entity span detection and entitiy typing subtasks. Challeng! -> over/underdetection of false entity spans during span detection
- it introduces a novel few-shot NER approach which employs boundary-aware contrastive learning to enhance an LLM's ability to perceive entity boundaries
- uses LoRAHub
- task
    - given a sequence Y with L tokens, NER aims to assign each token xi to its corresponding label y from Y U O (Y - predefined labels, O - other labesls)
    - NER is first pretrained on data-sufficient source domain and then fine-tuned in target domain w/ only few labeled samples
    - task is to recognize entities in the target Set after learning from the Domain set (support set)
- comprises:
    - entity span detection
        - prompt representation 
            - BANER fine-tunes LLM using LoRA (updates only small parameters)
            - prompt is fed into the LLM to perform entity span detection
        - boundary-aware contrastive learning (Khosla et al., 2020)
            - teaches the model to distinguish correct entity boundaries
        - LLM is fine-tuned using LoRA - freezing pretrained parameters and introducing trainable rank decomposition matrices ionto each layer of the transformer architecture
    - entity type classification
        - a specific entity class is assiged to each span identified during entity span detection
        - using a prompt, the model constructs a prototype for each given entity type
        - for each span in a query the distance between its representation and prototype is calculated
- outperforms previous sota methods



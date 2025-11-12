### NER Methods



#### GLiNER 
- https://arxiv.org/pdf/2311.08526
- https://github.com/urchade/GLiNER
- utilizes smaller scale Bidirectional Language Models (BiLM), e.g. BERT or deBERTa.
- treates the task of Open (identification of any type) NER as matching entity type embeddings to textual span representations in latent space
- has three main components:
     - pre-trained textual encoder (e.g. deBERTa)
     - a span representation module which computes span embeddings from token embeddings
     - an entity representation module which computes entity embeddings that model seeks to extract


#### BANER (Boundary-Aware LLMs for Few-Shot Named Entity Recongnition)
- https://aclanthology.org/2025.coling-main.691.pdf
- https://github.com/UESTC-GQJ/BANER
- recently few shot NER have gathered a lot of attention
    - prompt-based methods: leverage the knowledge of LLMs by utilizing templates, prompts, etc to effectively harness the internal knowledge of LLMs
    - metric-based methods: aim to learn the future space w/ robust generalizability and classify test samples using nearest class prototypes / or neighboring samples; may fail to fully utilize entity type knowledge from the source domain during type classification stage..
    - recently the focus -> two stage architecture,task is decomposed into entity span detection and entitiy typing subtasks. Challenge! -> over/underdetection of false entity spans during span detection
- introduces a novel few-shot NER approach which employs boundary-aware contrastive learning to enhance an LLM's ability to perceive entity boundaries
- uses LoRAHub
- task
    - given a sequence of tokens X NER aims to assign each token xi to its corresponding label y from Y U O (Y - predefined labels, O - other labesls)
    - NER is first pretrained on data-sufficient source domain and then fine-tuned in target domain w/ only few labeled samples
    - task is to recognize entities in the target Set after learning from the Domain set (support set)
- comprises:
    - entity span detection
        - prompt representation 
            - BANER fine-tunes LLM using LoRA (updates only small parameters)
            - prompt is fed into the LLM to perform entity span detection
        - boundary-aware contrastive learning (Khosla et al., 2020)
            - teaches the model to distinguish correct entity boundaries
        - LLM is fine-tuned using LoRA - freezing pretrained parameters and introducing trainable rank decomposition matrices into each layer of the transformer architecture
    - entity type classification
        - a specific entity class is assiged to each span identified during entity span detection
        - using a prompt, the model constructs a prototype for each given entity type
        - for each span in a query the distance between its representation and prototype is calculated
- outperforms previous sota methods


#### RetrieveAll
- https://arxiv.org/pdf/2505.19128
- a universal multilingual NER based on dynamic LoRA
- this framework constructs an input-aware LoRA retrieval mechanism, enabling hybrid multilingual recognition and reasoning accross multiple languages
- LoRA:
    - adds decomposable training matrices that are combined in parallel with the pre-trained parameters
    - enables fine-tuning only a small number of low-rank parameters
- multilingual NER
    - is decomposed into several sub-tasks of NER for different languages
    - each LoRA parameter injected into LLM is trained on the NER task for each language 
        -> model's focus is enhanced for each language-specific task, surpressing interference and conflict btw languages
        -> the lightweight parameter update mechanism on LoRA allows the model to quickly converge even in environments with limited data resources
        -> when adding a new language, only LoRA parameters need to be adjusted and not the LLM parameters 
        -> model can dynamically select suitable LoRAs based on input language
    - input to multilingual NER comes from any of the predefined languages or from a combination
    - for each training sample, the LLM generates entitiy-level and context-level representations, the most appropriate contextual and entity examples for each sample are computed using cosine similarity & a dynamic threshold 
    - after identifying the top k most relevant contextual examples, the language of the input sequence is inferred by calculating the most frequent language label from the set
    -  the designed LoRA module is then integrated with the LLM parameters
- dataset MultiCONER, PAN-X


#### NER Retriever
- https://arxiv.org/pdf/2509.04011
- https://github.com/ShacharOr100/ner_retriever
- a variant of NER where the types of interest are not provided in advance, & a user-friendly type description is used to retrieve documents mentioning entities of that type
- leverages the internal structure of LLMS to obtain type-aware representations of entity mentions
- task: NER is defined as retrieving texts that mention entities belonging to a given entity type (coming from a query) 
- embedding-based approach in which both entity mentions & type queries are embedded into a shared semantic space using a mid-layer od LLaMA 2.1 8B & then followed by a lightweight multi-layer perceptron (MLP) that maps the embeddings into a compact, type-aware vector space
- MPL is trained with contrastive objective to align entities of the same type and separate those of different types
- at indexing, the computed & transformed embeddings are stored; at query time, we embed the user-specific type and retrieve the most similar entity vector via nearest-neighbor search
- this approach relies on extracting entity mention embeddings from intermediate layers of a pre-trained LLM (not all layers capture type semantics equally well)
- since the embeddings are high-dimensional, MLP is used to transform them into a more compact form, using a triplet contrastive loss:
    - each training tripplet includes three components
        - an anchor: natural language description e.g. politician
        - a set of positives: entity mentions of the same type (angela merkel)
        - a set of negatives: mentions from different types (Danube river)
    - the contrastive objective encourages embeddings of the same-type entities to be close together and dissimal types to be well separated
- implementative of NER Retriever 
    - entity detection
        - important: identify spans of all entities in a text, independent of their semantic meaning
        - LLM is employed
    - indexing
        - for each docu, all entity mentions are identified and the docu is passed through a frozen LLM encoder -> MLP -> the resulting entity vectors are stored in a cector index linked to their corresponding document
        - optimized for cosine search
    - retrieval 
        - at query time the user provides a type description in natural language
        - query is embedded the same way as above in the same embedding space as indexed entries
        - the k most similar entity embeddings are retrieved
- dataset NERetriver (Katz et al., 2023), Few-NERD (supervised) (Ding et al., 2021), MultiCoNER 2 (Fetahu et al., 2023)


#### EL4NER
- https://arxiv.org/pdf/2505.23038
- 



#### RUIE
- https://www.arxiv.org/pdf/2409.11673
- https://github.com/OStars/RUIE
- Unified information extraction (UIE) -> aims to extract diverse structured information from unstructured text
- a framework that leverages in-context learning for efficient task generation
- introduces a novel demostration selection mechanism combining LLM preferences with a keyword-enhanced reward model, and employs a bi-encoder retriever training through contrastive learning & knowledge distilation
- In-context Learning   -> ability of LLMs to perform new tasks with only a few examples or demostrations
                        -> fine-tuning can be circumvented
- IE - a) NER , b) RE (relation extraction) , c) EE (event extraction)
- sample format: 1)task name, 2) schema - task ontology represented in form of python list 3) input context to be extracted 4) structured output linearized by NL
-  older IE check text similarity btw the input text and examples, RUIE lets LLM decide which examples are more helpful
    - use BM25 to narrow down relevant examples
    - calculate scores for those examples based on how well LLM performs with them
- Keyword enhanced reward
    - improves the scoring and ranking of example pairs
    - to make the fine-grained info btw the input query & the candidate examples fully interactive 
    - <keyword> tags are added around each important span in the input
    - train cross-encoder using cross entropy loss (to make the CE score the positive examples higher)
        - to score how well a candidate matches the query
        - output real-value scores
- UIE retriever training
    - bi-encoder architecture that approximates the cross-encoder reward model
    - computes similarity using dot product btw vector embeddings
- 31 datasets 














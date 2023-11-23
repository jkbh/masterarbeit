- [ ] Self-Attention in the context of Bert?

# BERT
 
Main contribution is the usage of context from the left and right of a text segment to train its representatoin, hence the term bidirectional.

BERT can be fine-tuned to all kinds of tasks by just adding one extra output layer. Such tasks can be query answering, language inference or grounding information.

## Intro

Two existing strategies for applying pre-trained representations to tasks:
1. Feature-Based
2. Fine-Tuning

Feature-based(ELMo) uses task specific architectures that **include** pre-trained representatios.

Fine-tuning(GPT) has minimal task-specific parameters and is trained own downstream task by fine-tuning all pretrained params.

Both approaches share unidirectional pretraining.

Authors argue that unidirectionality yields less rich representations, especially in sentence-level tasks.

Introduce masked language model(MLM):
Random tokens are masked and need to be predict based on left and right context(neighbouring tokens)

Two Pretraing Tasks:
1. Masked MLM

They don't always use the [MASK] token but sometimes mask with a random token or keep the original. This is because while finetuning the [MASK] doesn't appear.

2. Next Sentence Prediction


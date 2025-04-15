---
base_model:
- mistralai/Mistral-7B-Instruct-v0.2
- segolilylabs/Lily-Cybersecurity-7B-v0.2
language:
- en
tags:
- cybersecurity
- cyber security
- hacking
- mistral
- finetune
- ctf
datasets:
- ShadowEternity/CTF-writeups
---

# CTF-Helper
Model Link - https://huggingface.co/ShadowEternity/CTFsolver

#### Done for ML - Mini Project by:
- Akash Varunn
- Martin Rozariyo
- Praneesh  R V
- Santosh Tharun
- Prasanna Kumar
## Model description
CTFsolver is a fine-tuned Mistral-7B model, originally adapted from Lily-Cybersecurity-7B-v0.2. This model is specifically trained to assist with Capture The Flag (CTF) challenges, providing detailed writeups, exploit generation, and cybersecurity solutions.

Built on top of Mistral-7B, it incorporates cybersecurity knowledge from Lily-Cybersecurity-7B-v0.2 and has been further fine-tuned on real-world CTF challenge solutions and security research papers.


## Training

CTFsolver has been fine-tuned on ShadowEternity's CTF-writeups dataset, containing:

    Publicly available CTF solutions

    Cybersecurity blogs and research papers

    CTF challenge walkthroughs from top security teams

## Limitations
Our model is fine-tuned on top of Lily-Cybersecurity which is finetuned from Mistral-7B-Instruct-v0.2 as such it inherits many of the biases from that model.

As with any model, It can make mistakes. Consider checking important information. 

Stay within the law and use ethically.

# Decision 3: Concatenate responses before chunking

## Context
As part of the Information Extraction phase of the methodology of [Romano et al (2024)](https://www.sciencedirect.com/science/article/pii/S0957417424011588), we pass relevant text data into a BERT model to predict the value of a masked value (or values) within a user-added prompt. Text is split into tokens as part of this process, with each token corresponding to a word by default. There is a maximum permissible token count of 512 tokens for each prediction call, which includes the prompt.

An initial approach to processing the various question responses handled each response separately, but a small percentage of responses are longer than the limit. A method (innoprod/text_analysis/chunking_tools.py > `chunk_text_sentencewise`) was developed for breaking such text into smaller chunks, while also keeping sentences intact and in order, and attempting to split the text evenly (i.e., into chunks of similar size).

## Options considered
1. Chunking the individual too-long response individually.
2. First combining the responses to all relevant questions for each firm, then chunking the combined responses (where needed).

## Discussion

Advantages of Option 1:
* Simplicity of the text preparation before feeding into the BERT model.

Disadvantages of Option 1:
* This would lead to a larger number of chunks to be assessed than could otherwise be achieved. 

Advantages of Option 2:
* This would lead to smaller number of chunks to be assessed per firm, thereby simplifying the post-prediction analysis.

Disadvantages of Option 2:
* The order in which question responses are concatenated will have a (small) impact. For example, for a single firm, if the response to Question A is a little longer than the limit and the response to Question B is comfortably less than the limit, then
    - If Response B is appended to the end of Response A, then the two chunks to be assessed will be (1) most of Response A, excluding a little text at the end and (2) the end part of Response A followed by all of Response B.
    - If Response A is appended to the end of Response B, then the two chunks to be assessed will be (1) all of of Response B, plus the first part of Response A appended and (2) most of Response A, excluding a little text from the start.

## Decision
We will adopt the second option, namely combining the responses to all relevant questions for each firm and then chunking this combined response where needed.

## Status
Accepted

## Consequences

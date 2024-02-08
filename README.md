# Prompt Engineering Examples for ChatGPT4PCG 2

This repository contains examples of prompt engineering for [ChatGPT4PCG 2 competition](https://chatgpt4pcg.github.io/).
We provide examples of an implementation of the prompt engineering techniques utilizing our Python
package, [`chatgpt4pcg-python`](https://github.com/chatgpt4pcg/chatgpt4pcg-python). We implemented several prompt
engineering techniques, including:

1. Zero-shot (single-turn and multi-turn versions) prompting (`zero_shot` and `zero_shot_multi_turn` folders).
2. Null-shot prompting (`null_shot` folder).
3. Few-shot prompting (`few_shot` folder).
4. Zero-shot chain-of-thought prompting (`zero_shot_cot` folder).
5. Null-shot chain-of-thought prompting (`null_shot_cot` folder).
6. Tree-of-thought prompting (`tot` folder).

We recommend participants start by taking a look at the `zero_shot` and `zero_shot_multi_turn` examples to understand
the basic implementation of zero-shot prompting. Participants who interest only in optimizing the prompt are welcome to
take a look at the `prompts` folder in each example to see the prompt used in the example and modify it to their needs.
Participants who interest in implementing
more elaborate prompt engineering technique may interest in taking a look at the implementation of the tree-of-thought
prompting in the `tot`
folder.

It is important to note that the examples provided in this repository are not exhaustive and are intended to serve as a
starting point for the participants to experiment with prompt engineering techniques. We encourage the participants to
explore and experiment with different prompt engineering techniques to improve the performance of their approach.
Furthermore, prompts provided in each example are not optimal and can be further improved by the participants.

## Folder structure

```
.
├── .env.example
├── README.md
├── few_shot
│ ├── few_shot.py
│ └── prompts
│    └── few_shot.txt
├── null_shot
│ ├── null_shot.py
│ └── prompts
│    └── null_shot.txt
├── null_shot_cot
│ ├── null_shot_cot.py
│ └── prompts
│    └── null_shot_cot.txt
├── requirements.txt
├── tot
│ ├── prompts
│ │ ├── evaluate.txt
│ │ ├── format.txt
│ │ └── task.txt
│ └── tot.py
├── zero_shot
│ ├── prompts
│ │ └── zero_shot.txt
│ └── zero_shot.py
├── zero_shot_cot
│ ├── prompts
│ │ └── zero_shot_cot.txt
│ └── zero_shot_cot.py
└── zero_shot_multi_turn
├── prompts
│ ├── 0.txt
│ └── 1.txt
└── zero_shot_multi_turn.py
```

## Installation

To run the examples, you need to install the required packages. You can install the required packages by running the
following command:

```bash
pip install -r requirements.txt
```

## Running the examples

To run the examples, you need to set the environment variables in the `.env` file. You can copy the `.env.example` file
and rename it to `.env`. Then, you need to set the `OPENAI_API_KEY` environment variable to your OpenAI API key. You can
get the OpenAI API key by following the instructions [here](https://platform.openai.com/docs/introduction). Please note
that we do not provide support for the OpenAI API key. It is the responsibility of the participants to obtain their own
OpenAI API key and secure it.

After setting the environment variables, you can run the examples by running the following command:

```bash
python <pe_folder>/<pe_name<.py
```

For example, to run the zero-shot example, you can run the following command:

```bash
python zero_shot/zero_shot.py
```

Please note that the examples provided in this repository are set to generate only one trial for `A` character. You can
modify the `run_evaluation` function in the examples to generate more trials for different characters.

For example, to generate 10 trials for `A` character, you can modify the `run_evaluation` function in the `zero_shot.py`
file as follows:

```python
run_evaluation("zero_shot", ZeroShotPrompting, num_trials=10, characters=["A"])
```

## Contributing

We welcome contributions to this repository to expand the examples and improve the prompt engineering techniques.
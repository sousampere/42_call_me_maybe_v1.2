# Please, star my project if you found it useful : )

*This project has been created as part of the 42 curriculum by gtourdia*

# 42 Call_me_maybe

Personnal implementation of the call_me_maybe project of school 42.

![Video](https://i.ibb.co/hx5gwN6T/Enregistrement-de-l-e-cran-2026-03-08-a-16-42-20.gif)


## Description

Call_Me_Maybe is a project part of the 42 curriculum that aims to learn to generate content using text-based generative AI, also known as LLM (Large Language Model).

Given a certaing JSON file containing prompts and another file containing function definitions :

```json
# Json file containing prompts :
[
  {
    "prompt": "What is the square root of 16?"
  },
  ...
]
```

```json
# Json file function definitions :
[[
  {
    "name": "fn_add_numbers",
    "description": "Add two numbers together and return their sum.",
    "parameters": {
      "a": {
        "type": "number"
      },
      "b": {
        "type": "number"
      }
    },
    "returns": {
      "type": "number"
    }
  },
  {
    "name": "fn_greet",
    "description": "Greet the given name.",
    "parameters": {
      "name": {
        "type": "string"
      }
    },
    "returns": {
      "type": "string"
    }
  },
  ...
]
```

The student has to create a program that takes all prompts and process them to create an output json file that contains, for each prompt, the corresponding function and its arguments. Example

### Prompt example :
```json
"prompt": "Greet gtourdia"
```

### Expected output:
### Prompt example :
```json
{
    "prompt": "Greet gtourdia", <- original prompt
    "name": "fn_greet", <- function name
    "parameters": {
        "name": "gtourdia" <- argument for the function
    }
}
```

This output file needs to be 100% valid JSON. Since we are working on a very small LLM, its output doesn't absolutely have to be valid, as long as it is mostly choosing the good functions. To get better results, we would have to use a better model. To make the LLM output an available function every time, we are expected to use constained decoding, which is the concept of selecting the highest probability token generated, checking if it matches our expectations (a function name, arg type, etc.) and add its decoded value to our current text output.

## Instructions

**[ Makefile & Execution ]**

The project uses uv for dependency management and a Makefile to automate core tasks.

-  `make install`: Install all project dependencies using `uv`, `pip`, or your preferred package manager.

-  `make run`: Execute the main function calling script.

-  `make debug`: Run the script using the built-in Python debugger (`pdb`) for troubleshooting.

-  `make lint`: Run code quality checks using `flake8` and `mypy` to ensure compliance with project standards.

-  `make lint-strict`: Run enhanced static analysis using `mypy --strict`.

-  `make clean`: Remove temporary files and caches, such as `__pycache__` and `mypy_cache`.

## Custom bonus

I Added the following bonuses:
- Custom visualizer, with the -v or --visualize flag
- Hardware acceleration with the -d or --device flag

![Video](https://i.ibb.co/hx5gwN6T/Enregistrement-de-l-e-cran-2026-03-08-a-16-42-20.gif)

## Additional informations

### Algorithm

The algorithm I made follows this simple execution pipeline:
- Preparation (get prompts, and function definitions from json files)
- Processing
    - For each prompt, generate the highest probability token for a function name. Skip each token until the generated on corresponds to the start of the name of a function. Repeat until only one function is remaining in the available ones. Ignore all tokens not corresponding to anu function.
    - After the function is found, for each of its argument, generate it using the appropriate function, depending on the expected arg (number, string).
- Export to the json output path

### Design decisions

I decided to follow the documentation provided by the qwen ingeneers to prompt it the right way. It makes the output way better.

### Performances analysis

Since this project uses Qwenn, I managed to reach very good result for simple function (that expect int/floats in input), but the nature of the LLM makes it unpredictable in generating good output for strings generation. The output quality depends on the difficulty of understanding the function.
For instance, the LLM will easily find the arguments for `"What is the sum of 1 and 3?"`, but will struggle a lot on questions like `"Replace every 'i' in 'I want an icecream' with the name of the current president of France"`.
This could have beed supervised if we had predictable function in input, but since the evaluator can make up any function he want, we cannot easily solve this problem, unless we use another more powerful LLM.

# Challenges faced

The most difficult challenge for me was to think about how I could implement the constained decoding. I ended up checking if any of my available function starts with the generated token. If it does, I add this token to my output and regenerate the logits based on the previous prompt + the generated token. Else, I make the token's value to negative infinity, and check the next one highest token.

# Testing strategy

I tested all possible errors that I could handle that came to my mind, and handled them as I could. I verified that the json output is 100% valid, and that its content is good.

# Example usage in companies

This program could be integrated in a company's workflow in the case of users entering data in an unpredictable format, that needs to be processed in some ways. For example, I could set up a chatbot in the website of my server-hosting company, that execute the prompts of the user by using the functions that are available, like ```"Open my port 8080"``` -> ```function open_port will be used with arg a (int) = 8080```.

## Ressources

On this project, we first need to parse informations from a configuration file. This implies ignoring comments and invalid flags.

- My knowledge since I've worked with LLM's before
- [Qwenn control tokens & chat template](https://qwen.readthedocs.io/en/latest/getting_started/concepts.html)
- Google Gemini was used for questions related to understanding constained decoding

## 🚀 Author

[gtourdia / @sousampere](https://github.com/sousampere)
Special thank to:

cyakisan, lbonnet, abonnet, htrapp, jeschwar

I am a student at the 42 Mulhouse school. Most of my public projects will be from this school, while I will keep private most of my other projects.


![42Mulhouse](https://camo.githubusercontent.com/242a608f6e84c19ca24b2fb5c5935d921ff5e79090a91d8b2be3c72626c66272/68747470733a2f2f6173736574732e6b6d302e6f6d65726c6f636c69656e74732e636f6d2f636f6d6d756e6974792f63666265356130622d373633372d343361302d393466392d3764663266633238386331642e6a7067)

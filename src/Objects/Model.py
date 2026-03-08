
from typing import Generator

from src import Small_LLM_Model

class Model(Small_LLM_Model):
    """ LLM Class with useful methods """
    def predict_token(self, prompt_message: str, previous_tokens: str = '', skip: int = 0):
        """ Get the next token from the original prompt + the previously
         generated tokens. """
        # Original prompt
        prompt = f"<|im_start|>user\n{prompt_message}<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n{previous_tokens}"

        # Encoding to tensors
        tensors = self.encode(prompt)

        # Calculating text token probabilities
        probabilities = self.get_logits_from_input_ids(tensors.tolist()[0])

        # Sorting most probable tokens
        sorted_tokens = sorted(probabilities, reverse=True)

        # Pick the highest probability token (Skiping unwanted tokens if needed)
        token = probabilities.index(sorted_tokens[skip])

        # Return the highest pronbability token
        return self.decode(token)

    def predict_multiple_tokens(self, prompt_message: str, previous_tokens: str = '', skip: int = 0) -> Generator:
        """ Get the next token from the original prompt + the previously
         generated tokens. """
        # Original prompt
        prompt = f"<|im_start|>user\n{prompt_message}<|im_end|>\n<|im_start|>assistant\n<think>\n\n</think>\n\n{previous_tokens}"

        # Encoding to tensors
        tensors = self.encode(prompt)

        # Calculating text token probabilities
        probabilities = self.get_logits_from_input_ids(tensors.tolist()[0])

        # Sorting most probable tokens
        sorted_tokens = sorted(probabilities, reverse=True)

        # Pick the highest probability token (Skiping unwanted tokens if needed)
        token = probabilities.index(sorted_tokens[skip])

        # print(prompt)

        while True:
            yield self.decode(probabilities.index(sorted_tokens[skip]))
            skip += 1

        # Return the highest pronbability token
        return self.decode(token)
    
    "To solve the prompt What is the sum of 2 and 4 ?, you will use the following function: {'name': 'fn_add_numbers', 'description': 'Add two numbers together and return their sum.', 'parameters': {'a': {'type': 'number'}, 'b': {'type': 'number'}}, 'returns': {'type': 'number'}}. Give each parameter, followed by '\n' character."
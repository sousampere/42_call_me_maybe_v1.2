from typing import Any, Generator

from src import Small_LLM_Model


class Model(Small_LLM_Model):
    """ LLM Class with useful methods """
    def predict_token(self, prompt_message: str,
                      previous_tokens: str = '',
                      skip: int = 0) -> Any:
        """ Get the next token from the original prompt + the previously
         generated tokens, as a string. """
        # Original prompt
        prompt = f"<|im_start|>user\n{prompt_message}<|im_end|>\n" + \
            f"<|im_start|>assistant\n<think>\n\n</think>\n\n{previous_tokens}"

        # Encoding to tensors
        tensors = self.encode(prompt)

        # Calculating text token probabilities
        probabilities = self.get_logits_from_input_ids(tensors.tolist()[0])

        # Sorting most probable tokens
        sorted_tokens = sorted(probabilities, reverse=True)

        # Pick the highest probability token
        # (Skiping unwanted tokens if needed)
        token = probabilities.index(sorted_tokens[skip])

        # Return the highest pronbability token
        return self.decode(token)

    def predict_multiple_tokens(self, prompt_message: str,
                                previous_tokens: str = '',
                                skip: int = 0) -> Generator[str]:
        """Returns a generator of the most probable token

        Args:
            prompt_message (str): original prompt
            previous_tokens (str, optional): previously generated tokens
            . Defaults to ''.
            skip (int, optional): fist n tokens to skip. Defaults to 0.

        Yields:
            Generator[str]: str token generator
        """
        # Original prompt
        prompt = f"<|im_start|>user\n{prompt_message}<|im_end|>\n" + \
            f"<|im_start|>assistant\n<think>\n\n</think>\n\n{previous_tokens}"

        # Encoding to tensors
        tensors = self.encode(prompt)

        # Calculating text token probabilities
        probabilities = self.get_logits_from_input_ids(tensors.tolist()[0])

        # Sorting most probable tokens
        sorted_tokens = sorted(probabilities, reverse=True)

        while True:
            yield self.decode(probabilities.index(sorted_tokens[skip]))
            skip += 1

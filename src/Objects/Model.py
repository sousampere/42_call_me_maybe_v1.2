
from src import Small_LLM_Model

class Model(Small_LLM_Model):
    """ LLM Class with useful methods """
    def predict_token(self, prompt_message: str, previous_tokens: str = '', skip: int = 0):
        """ Get the next token from the original prompt + the previously
         generated tokens. """
        # Original prompt
        prompt = f"<|im_start|>user\n{prompt_message}<|im_end|>\n<|im_start|>assistant\n{previous_tokens}"

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

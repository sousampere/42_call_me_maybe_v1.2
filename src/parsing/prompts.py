
from typing import List
import json
from pydantic import BaseModel


class PromptFileError(Exception):
    pass

class Prompt(BaseModel):
    prompt: str

def get_prompts(prompt_file_path: str) -> List[Prompt]:
    """ Load the prompts file as a list of Prompt object. """
    try:
        with open(prompt_file_path, 'r') as file:
            data = json.load(file)

        if (len(data) == 0):
            raise PromptFileError('No prompt found in your functions definition file.')

        # Validating prompt with pydantic
        prompts_list = []
        for prompt in data:
            prompts_list.append(Prompt(
                prompt=prompt['prompt']
            ))
        return prompts_list
    
    except FileNotFoundError:
        raise PromptFileError('Your prompts file was not found.')
    except json.JSONDecodeError:
        raise PromptFileError('Your prompts file contain invalid json.')
    except PermissionError:
        raise PromptFileError('Not enough permissions to open your prompts file.')
    except Exception:
        raise PromptFileError("Unable to use your prompts file. Please make "
                                       "sure that your file respects the json structure expected.")

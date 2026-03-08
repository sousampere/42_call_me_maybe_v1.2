

from typing import Any, Dict, List

from src import Prompt, FunctionDefinition, Model


class PromptProcessor():
    """ Object specialized in prompts processing """
    def __init__(self,
                 prompts: list[Prompt],
                 functions_definition: list[FunctionDefinition],
                 llm = Model):
        self.__prompts = prompts
        self.__functions_definition = functions_definition
        self.__llm = llm

    def get_available_functions(self) -> List[str]:
        """ Returns the list of available functions """
        available_functions = []
        for function in self.__functions_definition:
            available_functions.append(
                {'name': function.name,
                 'description': function.description})
        return available_functions

    def generate_fn_name(self, prompt: str) -> str:
        """ Given a prompt, returns the most useful
         function of the PromptProcessor's functions
          to solve the prompt """
        available_functions = self.get_available_functions()

        function_progress = ''
        while True:
            # Prompt creation
            prompt_message = f'Here are the different functions available: {available_functions}. To resolve the prompt, "{prompt.prompt}".'

            # Token generator
            for generation in self.__llm.predict_multiple_tokens(
                prompt_message=prompt_message,
                previous_tokens=function_progress):

                # Processing current token
                remaining_functions = []
                for function in available_functions:
                    if function['name'].startswith(function_progress + generation):
                        remaining_functions.append(function)
                if (len(remaining_functions) == 1):
                    return remaining_functions[0]['name']
                elif len(remaining_functions) > 1 and generation != '':
                    function_progress = function_progress + generation
                    available_functions = remaining_functions
                    break

    def generate_parameters(self, prompt_message: str, function_name: str) -> Dict[Any, Any]:
        """ Given a prompt and the function for this prompt,
         returns the arguments to execute correctly the function. """
        # Getting the function definition from its name
        for function_def in self.__functions_definition:
            if (function_def.name == function_name):
                definition = function_def
        
        # Getting parameters
        for param in definition.parameters:
            pass

    def generate_int_parameter(self, prompt_message: str, function: FunctionDefinition, previous_gen: str) -> int:
        prompt = f"To solve the prompt {prompt_message}, you will use the following function: {function.full_definition}. Provide each parameter, followed by '\n' character."
        
        function_progress = ''
        while True:
            for generation in self.__llm.predict_multiple_tokens(
                prompt_message=prompt_message,
                previous_tokens=previous_gen+argument_progress):

                # Skip token if it's not in the regex / invalid
                regex = '-0123456789.\n'
                stop = False
                for character in generation:
                    if character not in regex:
                        stop = True
                if stop:
                    continue

                # Skip token if there are two '.' characters
                if (argument_progress + generation).count('.') >= 2:
                    continue

                # Skip token if there are two '-' characters
                if (argument_progress + generation).count('-') >= 2:
                    continue

                # Skip token if there is a '-' character not at the beggining
                if (argument_progress + generation).count('-') == 1\
                    and (argument_progress + generation)[0] != '-':
                    continue

                argument_progress = argument_progress + generation
                if '\n' in argument_progress:
                    argument_progress = argument_progress.split('\n')[0]
                    if argument_progress is None:
                        continue
                    try:
                        return float(argument_progress)
                    except ValueError:
                        print(f'debug: Erreur de conversion de "{argument_progress}"')
                        argument_progress = ''
                break

    def generate_str_parameter(self, prompt_message: str, function: FunctionDefinition, previous_gen: str) -> int:
        prompt = f"To solve the prompt {prompt_message}, you will use the following function: {function.full_definition}. Provide each parameter, followed by '\n' character."
        
        argument_progress = ''
        while '\n' not in argument_progress:
            argument_progress = argument_progress + self.__llm.predict_token(
                prompt_message=prompt,
                previous_tokens=previous_gen + argument_progress
            )
        return (argument_progress.split('\n')[0])
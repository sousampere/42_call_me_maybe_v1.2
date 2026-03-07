
from typing import Dict, List
import json
from pydantic import BaseModel, model_validator


class FunctionsDefinitionError(Exception):
    pass


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Dict[str, str]]
    returns: Dict[str, str]
    full_definition: str

    @model_validator(mode='after')
    def validation(self) -> FunctionDefinition:
        
        for key in self.parameters.keys():
            print(self.parameters[key].keys())
            if 'type' not in self.parameters[key].keys():
                raise FunctionsDefinitionError('Unsupported argument type '
                                               f'for parameter {key} in '
                                               f'function {self.name}')
        return self



def get_functions_definition(functions_definition_path: str) -> List[FunctionDefinition]:
    """ Load the functions definition file as a list of dicts. """
    try:
        with open(functions_definition_path, 'r') as file:
            data = json.load(file)
        if (len(data) == 0):
            raise FunctionsDefinitionError('No function found in your functions definition file.')

        # Sending functions to pydantic to verify their content
        function_list = []
        for function in data:
            function_list.append(FunctionDefinition(
                name=function['name'],
                description=function['description'],
                parameters=function['parameters'],
                returns=function['returns'],
                full_definition=str(function)
                ))
        return function_list
    except FileNotFoundError:
        raise FunctionsDefinitionError('Your functions definition file was not found.')
    except json.JSONDecodeError:
        raise FunctionsDefinitionError('Your functions definition file contain invalid json.')
    except PermissionError:
        raise FunctionsDefinitionError('Not enough permissions to open your functions definition file.')
    except Exception:
        raise FunctionsDefinitionError("Unable to use your functions definition file. Please make "
                                       "sure that your file respects the json structure expected.")

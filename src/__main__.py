
from src import Model, Small_LLM_Model
from src import get_arguments
from src import get_functions_definition
from src import get_prompts
from src import PromptProcessor

def main() -> None:

    # Parsing
    args = get_arguments()

    # Loading model
    llm = Model(model_name=args.model, device=args.device)

    # Getting functions definitions
    functions_definition = get_functions_definition(
        args.functions_definition)

    # Getting prompts
    prompts = get_prompts(
        args.input)

    processor = PromptProcessor(
        prompts, functions_definition, llm
    )

    for prompt in prompts:
        output = processor.process(prompt=prompt)
        print(output)

    return None

if __name__ == '__main__':
    main()

    

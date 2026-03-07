
from src import Model, Small_LLM_Model
from src import get_arguments
from src import get_functions_definition

def main() -> None:

    # Parsing
    args = get_arguments()

    # Loading model
    llm = Model(model_name=args.model, device=args.device)

    # Getting functions definitions
    functions_definition = get_functions_definition(
        args.functions_definition)

    # Getting prompts
    functions_definition = get_functions_definition(
        args.functions_definition)

    output = ''
    while True:
        output = output + llm.predict_token('What is the sum of 2 and 2 ?', output, 2)
        print(output)

    return None

if __name__ == '__main__':
    main()

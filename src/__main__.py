
from src import Model
from src import get_arguments
from src import get_functions_definition
from src import get_prompts
from src import PromptProcessor
from src import Visualizer
import json
from pathlib import Path


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

    visualizer = Visualizer()

    if args.visualize:
        output = visualizer.process(processor)
    else:
        output = processor.process()

    try:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as output_file:
            json.dump(output, output_file)
    except Exception as e:
        print('Could not write to the json output. '
              f'More details: {e}')

    return None


if __name__ == '__main__':
    main()

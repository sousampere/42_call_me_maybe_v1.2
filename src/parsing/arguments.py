
from argparse import ArgumentParser, Namespace

# ajouter un arg pour selectionner le modele


def get_arguments() -> Namespace:
    """ Initialize the arguments for the program
     and return them """
    parser = ArgumentParser(
        prog="python -m src",
        description="A 42 project realised by gtourdia.",
        epilog="Made with ♥ by gtourdia :)"
    )

    # Functions definitions
    parser.add_argument(
        '-d', '--functions_definition',
        help='Path of the functions definitions file.',
        default='data/input/functions_definition.json',
        required=False
    )

    # Input file (prompts)
    parser.add_argument(
        '-i', '--input',
        help='Path of the prompt (input) file.',
        default='data/input/function_calling_tests.json',
        required=False
    )

    # Output file
    parser.add_argument(
        '-o', '--output',
        help='Path of the output file.',
        default='data/output/function_calling_result.json',
        required=False
    )

    # Verbose
    parser.add_argument(
        '-v', '--visualize',
        action='store_true',
        help='Activate vizualisation.',
        required=False
    )

    # Model
    parser.add_argument(
        '-m', '--model',
        help='Name of the used model.',
        default='Qwen/Qwen3-0.6B',
        required=False
    )

    # Device
    parser.add_argument(
        '--device',
        help='Physical accelerator (mps, cuda, cpu)',
        default='cpu',
        required=False
    )

    return parser.parse_args()

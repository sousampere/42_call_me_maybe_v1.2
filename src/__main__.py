
from src import Small_LLM_Model
from src import get_arguments

def main() -> None:

    # Parsing
    args = get_arguments()

    # Loading model
    llm = Small_LLM_Model(model_name=args.model, device=args.device)

    print(args)
    return None

if __name__ == '__main__':
    main()

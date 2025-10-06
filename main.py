import os

with open('key.txt', 'r') as file:
        key = file.readline().strip()

os.environ['OPENAI_API_KEY'] = key
os.environ['CHROMA_OPENAI_API_KEY'] = key

from crew.crew import crew

def main():

    dir = input('Diretório: ').strip()

    if not os.path.isdir(dir):
        print(f"O diretório '{dir}' não existe")
        return

    input_dir = {'diretorio' : dir}

    crew.kickoff(inputs=input_dir)
    print(crew.usage_metrics)


if __name__ == "__main__":
    main()
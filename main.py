import os

with open('key.txt', 'r') as file:
        key = file.readline().strip()

os.environ['OPENAI_API_KEY'] = key
os.environ['CHROMA_OPENAI_API_KEY'] = key

from crew.crew import crew
import asyncio



async def main():

    dir = input('Diretório: ').strip()

    if not os.path.isdir(dir):
        print(f"O diretório '{dir}' não existe")
        return

    input_dir = {'diretorio' : dir}

    await crew.kickoff_async(inputs=input_dir)



if __name__ == "__main__":
    asyncio.run(main())
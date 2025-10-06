import os

with open('key.txt', 'r') as file:
        key = file.readline().strip()

os.environ['OPENAI_API_KEY'] = key
os.environ['CHROMA_OPENAI_API_KEY'] = key

from crew.dev_crews.crews import crew_doc, crew_test, crew_review
import asyncio

async def main():

    dir = input('Diretório: ').strip()

    if not os.path.isdir(dir):
        print(f"O diretório '{dir}' não existe")
        return

    input_dir = {'diretorio' : dir}

    results = await asyncio.gather(
        crew_doc.kickoff_async(inputs=input_dir),
        crew_test.kickoff_async(inputs=input_dir),
        crew_review.kickoff_async(inputs=input_dir)
    )

    print(f"Doc crew metrics: {crew_doc.usage_metrics}")
    print(f"Test crew metrics: {crew_test.usage_metrics}")
    print(f"Review crew metrics: {crew_review.usage_metrics}")

if __name__ == "__main__":
    asyncio.run(main())
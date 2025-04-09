import argparse
from utils.web_scraper import scrape_url
from utils.file_loader import load_text_file
from utils.embedder import Embedder
from utils.mistral_interface import load_model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, help="URL to scrape")
    parser.add_argument("--file", type=str, help="Text file to load")
    parser.add_argument("--model_path", type=str, required=True, help="Path to Mistral GGUF model")
    args = parser.parse_args()

    if not args.url and not args.file:
        print("Provide either a --url or a --file")
        return

    # Load data
    if args.url:
        print(f"Scraping from URL: {args.url}")
        raw_text = scrape_url(args.url)
    else:
        print(f"Loading from file: {args.file}")
        raw_text = load_text_file(args.file)

    # Initialize embedder + index text
    embedder = Embedder()
    embedder.index_documents(raw_text)

    # Load Mistral model once
    print("Loading Mistral model...")
    llm = load_model(args.model_path)

    # Question loop
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == 'exit':
            break
        context = embedder.retrieve_context(query)
        prompt = f"[INST] Use the following context to answer the question:\n\n{context}\n\nQuestion: {query} [/INST]"
        output = llm(prompt, max_tokens=512, stop=["</s>"])
        print("\n🧠 Mistral says:", output["choices"][0]["text"].strip())

if __name__ == "__main__":
    main()

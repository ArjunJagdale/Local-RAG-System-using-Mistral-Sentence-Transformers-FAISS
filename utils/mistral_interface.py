from llama_cpp import Llama

def load_model(model_path):
    return Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=4,
        n_gpu_layers=0,
        verbose=False  # ⛔ Suppress unwanted logs
    )

def ask_mistral(model_path, question, context):
    llm = Llama(
        model_path=model_path,
        n_ctx=2048,
        verbose=False  # ⛔ Suppress logs during Q&A too
    )

    prompt = f"[INST] Use the following context to answer the question:\n\n{context}\n\nQuestion: {question} [/INST]"
    
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()

GLOBAL_LLM = None

class LLM:
    def __init__(self, model_name: str, 
                api_key: str = None, base_url: str = None, 
                model_path: str = None, n_ctx: int = 5000, n_threads: int = 4, verbose: bool = False,
                lang:str = "English"):
        if not api_key:
            self.llm = OpenAI(api_key=api_key, base_url=base_url)
        

        self.llm = Llama.from_pretrained(
            repo_id=model_name,
            filename=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
            verbose=verbose,
        )

        self.model = model
        self.lang = lang

    def generate(self, messages: list[dict]) -> str:
        if isinstance(self.llm, OpenAI):
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = self.llm.chat.completions.create(messages=messages, temperature=0, model=self.model)
                    break
                except Exception as e:
                    logger.error(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_retries - 1:
                        raise
                    sleep(3)
            return response.choices[0].message.content
        else:
            response = self.llm.create_chat_completion(messages=messages,temperature=0)
            return response["choices"][0]["message"]["content"]


def set_global_llm(api_key: str = None, base_url: str = None, model: str = None, lang: str = "English"):
    global GLOBAL_LLM
    GLOBAL_LLM = LLM(api_key=api_key, base_url=base_url, model=model, lang=lang)

def get_llm() -> LLM:
    if GLOBAL_LLM is None:
        logger.info("No global LLM found, creating a default one. Use `set_global_llm` to set a custom one.")
        set_global_llm()
    return GLOBAL_LLM


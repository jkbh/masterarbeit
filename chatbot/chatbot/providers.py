from openai import OpenAI
from transformers import AutoModelForCausalLM, AutoTokenizer

MISTRAL_INSTRUCT = "TheBloke/Mistral-7B-Instruct-v0.2-AWQ"


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI()

    def get_chat_completition(self, messages):
        completition = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )

        return completition


class MistralClient:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MISTRAL_INSTRUCT)
        self.model = AutoModelForCausalLM.from_pretrained(
            MISTRAL_INSTRUCT, low_cpu_mem_usage=True, device_map="cuda:0"
        )

    def get_chat_completition(self, messages):
        tokens = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, return_tensors="pt"
        ).cuda()

        completition = self.model.generate(tokens, max_new_tokens=512)
        completition = self.tokenizer.batch_decode(completition)
        return completition

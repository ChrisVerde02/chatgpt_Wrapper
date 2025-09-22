from openai import OpenAI

class ChatGPTWrapper:
    def __init__(self, api_key: str, model: str = "gpt-5"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.history = []

    def ask(self, prompt: str, role: str = "user", temperature: float = 0.7, max_tokens: int = 300) -> str:
        self.history.append({"role": role, "content": prompt})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            temperature=temperature,
            max_tokens=max_tokens
        )
        reply = response.choices[0].message.content.strip()
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset(self):
        self.history = []
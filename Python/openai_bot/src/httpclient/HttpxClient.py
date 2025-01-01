import os
import httpx


class HttpxClient:
    def __init__(self):
        self.__httpx_client = httpx.AsyncClient()
        self.__url = "https://api.openai.com/v1/chat/completions"
        self.__headers = {
            "Host": "api.openai.com",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_KEY')}",
        }

    async def post(self, question):
        data = await self._generate_payload_content_with_question(question)
        try:
            response = await self.__httpx_client.post(
                self.__url, headers=self.__headers, json=data
            )
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            return f"Failed to receive response: {response.status_code}"
        except httpx.HTTPError as exc:
            return f"An HTTP error occurred: {exc}"

    async def _generate_payload_content_with_question(self, question):
        return {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{question}"}],
        }

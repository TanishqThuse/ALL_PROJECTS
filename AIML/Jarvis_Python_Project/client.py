from openai import OpenAI

client = OpenAI(
    api_key="org-7pjyovieWtsPNyJE567NdtjM",
    )

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual ssistant named Jarvis, created by your Master Tanishq Thuse, you are skilled in explaining general tasks like Alexa and google cloud and complex programming concepts with creative flair."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
from llama_cpp import Llama

model = Llama(
    model_path="./models/llama-2-13b-chat.Q5_K_M.gguf",
    chat_format="llama-2",
    n_gpu_layers=-1,
    verbose=True,
)

response = model.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "You are an assistant that gives short and concise answers, formatted as lists",
        },
        {
            "role": "user",
            "content": "Please give me a list of persons that have coached the german national football team",
        },
    ],
    stream=False,
)


if response:
    response.object = "chat:"

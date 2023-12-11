from langchain.llms.llamacpp import LlamaCpp 
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = LlamaCpp(
    model_path="./models/llama-2-13b-chat.Q5_K_M.gguf",
    n_gpu_layers=-1,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

llm("I am going on trip to Hamburg an i want to visit the following attractions: 1. Speicherstadt 2.")



source .venv/bin/activate
pip install huggingface-hub langchain
CMAKE_ARGS="-DLLAMA_CUBLAS" pip install llama-cpp-python

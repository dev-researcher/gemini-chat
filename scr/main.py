from vertex_ai_client import VertexAIClient 
from prompt_samples import prompt_example

def main():
    client = VertexAIClient() response client.send_prompt(prompt_example)
    print (response)

if __name__ == "__main__":
    main()
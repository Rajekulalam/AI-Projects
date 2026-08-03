from transformers import pipeline

print("Loading AI model... (First time may take a few minutes)")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

print("AI is Ready!")
print("-" * 50)

while True:
    prompt = input("You: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = generator(
        prompt,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7
    )

    print("\nAI:")
    print(result[0]["generated_text"])
    print("-" * 50)
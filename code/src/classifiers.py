import openai
import yaml

# Load Config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

openai.api_key = config["llm"]["api_key"]

def classify_email(email_body):
    """Classifies an email using an LLM."""
    prompt = f"""
    Classify this email into one of the predefined request types.
    Email:
    {email_body}

    Provide:
    1. Request Type
    2. Confidence Score (0-100)
    3. Reasoning
    """

    response = openai.ChatCompletion.create(
        model=config["llm"]["model"],
        messages=[{"role": "system", "content": "You are an expert email classifier."},
                  {"role": "user", "content": prompt}],
        temperature=config["llm"]["temperature"]
    )

    output = response["choices"][0]["message"]["content"]
    lines = output.split("\n")

    return lines[0].split(":")[-1].strip(), float(lines[1].split(":")[-1].strip()), lines[2].split(":")[-1].strip()

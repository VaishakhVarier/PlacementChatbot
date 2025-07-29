import os
import random
from openai import OpenAI

# Use the new OpenAI client
client = OpenAI(
    api_key=os.getenv("Api_Key_Here"),
    base_url="https://api.groq.com/openai/v1"  # Important: Groq's base URL
)

fallback_responses = {
    "resume": [
        "Keep your resume concise — 1 page. Highlight internships, projects, and skills.",
        "Use strong action verbs and quantify achievements where possible."
    ],
    "interview": [
        "Practice common HR and technical questions. Mock interviews help.",
        "Be clear and structured in your answers. Use the STAR method."
    ],
    "companies": [
        "Top companies visiting include TCS, Infosys, Accenture, Capgemini, and L&T.",
        "Make a list of dream, core, and mass recruiters and target them accordingly."
    ],
    "preparation": [
        "Start with aptitude (Quant, LR, Verbal). Use PrepInsta or GeeksforGeeks.",
        "Revise DSA, OOP, DBMS, OS, and coding for technical rounds."
    ],
    "greeting": [
        "Hi there! I’m your Placement Support Bot. Ask me about resume, interviews, or prep tips."
    ],
    "default": [
        "Let me try to give you a better answer using Groq’s intelligence..."
    ]
}

def fallback_response(user_input):
    user_input = user_input.lower()
    for keyword, responses in fallback_responses.items():
        if keyword in user_input:
            return random.choice(responses)
    return random.choice(fallback_responses["default"])

def query_groq_llama(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful college placement support assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Groq API error: {str(e)}"

def chat():
    print("🎓 College Placement Support Bot (Groq-Enhanced)")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: All the best for your placements!")
            break

        logic_response = fallback_response(user_input)
        print("Bot (logic):", logic_response)

        if logic_response == fallback_responses["default"][0]:
            groq_reply = query_groq_llama(user_input)
            print("Bot (Groq):", groq_reply)

if __name__ == "__main__":
    chat()

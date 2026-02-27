import os
from dotenv import load_dotenv
import openai
from utils import data_fetcher, qualification

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_cricket_data():
    points = data_fetcher.fetch_points_table()
    results = data_fetcher.fetch_match_results()
    return points, results

def generate_analysis(query):
    points, results = get_cricket_data()

    prompt = open("models/analysis_prompt.txt", "r").read().format(
        user_input=query,
        points_table=points,
        results=results
    )

    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return res.choices[0].message["content"]

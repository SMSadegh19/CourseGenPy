import openai
import langchain
from langchain.llms import OpenAI

OPENAI_API_KEY="sk-xxxx"
openai.api_key=OPENAI_API_KEY

llm = OpenAI(openai_api_key=openai.api_key, temperature=0.0)

course_title = "Python programming for begginers"
target_audience = "10 to 12 age students that don't know anything about programming"
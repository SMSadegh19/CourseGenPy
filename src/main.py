import langchain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

import os
import openai

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file
# openai.api_key = os.environ['OPENAI_API_KEY']

OPENAI_API_KEY="sk-xxxxxxxxxxxxxx"
openai.api_key=OPENAI_API_KEY

llm = OpenAI(openai_api_key=openai.api_key, temperature=0.0, max_tokens=2000)
# chat = ChatOpenAI(openai_api_key=openai.api_key, temperature=0.0)

course_title = "Becoming a Football Data Analyst"
target_audience = "A bachelor graduate in Computer Engineering"

topics_parser = CommaSeparatedListOutputParser()
topics_format_instructions = topics_parser.get_format_instructions()
print(f'output format instruction: \n{topics_format_instructions}')


topic_generation_prompt = """\
We want to design a course with the following details:
Title: {course_title}
Target audience: {target_audience}

Suggest some topics for the whole course in my requested format:
{format_instructions}
"""

topics_prompt_template = PromptTemplate(
    template=topic_generation_prompt,
    input_variables=['course_title', 'target_audience'],
    partial_variables={"format_instructions": topics_format_instructions}
)

# Generating the Prompt
prompt = topics_prompt_template.format(course_title=course_title, target_audience=target_audience)
print(f'The prompt which is given to the LLM:\n{prompt}')

# Getting the output from LLM
output = llm(prompt)

# Parsing the output and getting the topics list
topics_list = topics_parser.parse(output)

print(topics_list)

subtopics_parser = CommaSeparatedListOutputParser()
subtopics_format_instructions = subtopics_parser.get_format_instructions()
print(f'output format instruction: \n{subtopics_format_instructions}')

subtopic_generation_prompt = """\
We want to design a course with the following details:
Title: {course_title}
Target audience: {target_audience}

Suggest some subtopics for the topic named as "{topic_name}" in my requested format:
{format_instructions}
"""



subtopics_prompt_template = PromptTemplate(
    template=subtopic_generation_prompt,
    input_variables=['course_title', 'target_audience', 'topic_name'],
    partial_variables={"format_instructions": subtopics_format_instructions}
)

topic_to_subtopics = {}
for topic in topics_list:
    print('________________________________________________________')
    print(f'topic: {topic}\n')
    prompt = subtopics_prompt_template.format(course_title=course_title, target_audience=target_audience, topic_name=topic)
    print(f'human:\n{prompt}')
    # Getting the output from LLM
    output = llm(prompt)
    print(f'llm:\n{output}')
    # Parsing the output and getting the topics list
    subtopics_list = topics_parser.parse(output)
    topic_to_subtopics[topic] = subtopics_list



content_generation_prompt = """\
We want to design a course with the following details:
Title: {course_title}
Target audience: {target_audience}

Please write the whole content (text) for the subtopic with name: \"{subtopic_name}\" \
(This subtopic is under the topic \"{topic_name}\")
"""
# note: Feel free to generate things other than text like code-snippets, and etc. in any place that is needed.
content_prompt_template = PromptTemplate(
    template=content_generation_prompt,
    input_variables=['course_title', 'target_audience', 'topic_name', 'subtopic_name'],
)


topics_to_subtopics_to_contents = {}
for topic in topic_to_subtopics:
    topics_to_subtopics_to_contents[topic] = {}
    for subtopic in topic_to_subtopics[topic]:
        prompt = content_prompt_template.format(course_title=course_title,
                                                target_audience=target_audience,
                                                topic_name=topic,
                                                subtopic_name=subtopic)
        output = llm(prompt)
        topics_to_subtopics_to_contents[topic][subtopic] = output
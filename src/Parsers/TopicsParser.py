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
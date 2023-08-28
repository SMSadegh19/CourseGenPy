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
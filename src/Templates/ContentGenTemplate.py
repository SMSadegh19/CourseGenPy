content_generation_prompt = """We want to design a course with the following details:
Title: {course_title}
Target audience: {target_audience}

Please write the whole content (text) for the subtopic with name: \"{subtopic_name}\" \
(This subtopic is under the topic \"{topic_name}\")

note: Feel free to generate things other than text like code-snippets, and etc. in any place that is needed.
"""
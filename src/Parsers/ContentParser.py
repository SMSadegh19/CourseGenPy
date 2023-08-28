prompt = content_prompt_template.format(course_title=course_title,
                                                target_audience=target_audience,
                                                topic_name=topic,
                                                subtopic_name=subtopic)
output = llm(prompt)
topics_to_subtopics_to_contents[topic][subtopic] = output
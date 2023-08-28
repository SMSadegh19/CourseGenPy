def dict_to_html(dictionary, output_file):
    html_content = "<html>\n<head>\n<title>Dictionary to HTML</title>\n</head>\n<body>\n"
    html_content += "<ul>\n"  # Start of table of contents

    for topic, subtopics in dictionary.items():
        # Add an anchor for each topic
        anchor = topic.replace(" ", "_")
        html_content += f"<li><a href=\"#{anchor}\">{topic}</a></li>\n"

    html_content += "</ul>\n"  # End of table of contents

    for topic, subtopics in dictionary.items():
        anchor = topic.replace(" ", "_")
        html_content += f"<h1 style=\"color:blue;\" id=\"{anchor}\">{topic}</h1>\n"

        for subtopic, content in subtopics.items():
            formatted_content = content.replace('\n', '<br>\n')
            html_content += f"<h2>{subtopic}</h2>\n<p>{formatted_content}</p>\n"

    html_content += "</body>\n</html>"

    with open(output_file, "w") as file:
        file.write(html_content)


output_file_path = course_title + ".html"
dict_to_html(topics_to_subtopics_to_contents, output_file_path)
print(f"HTML file saved at: {output_file_path}")
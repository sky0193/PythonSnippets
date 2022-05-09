#https://pypi.org/project/Wikipedia-API/
import wikipediaapi


def print_sections(sections, level=0):
        for s in sections:
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
                print_sections(s.sections, level + 1)


wiki_wiki = wikipediaapi.Wikipedia(
        language='de',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

p_wiki = wiki_wiki.page("Interface")

if not (p_wiki.exists()):
    print ("Page does not exist")

#Get Title
print(f"Page - Title: {p_wiki.title} \n\n")

#Get Summary
print(f"Page - Summary: {p_wiki.summary} \n\n")

#Get short Text

print(f"Page - short Text: {p_wiki.text} \n\n")

#Get sections
print("-------------------------------------------------------")
print("Print sections:\n")
print_sections(p_wiki.sections)
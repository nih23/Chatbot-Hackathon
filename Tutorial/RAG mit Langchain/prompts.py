from langchain.prompts import PromptTemplate

def german_sauerkrautlm():
    prompt_template = """[INST]<<SYS>> Sie sind ein Assistent für die Beantwortung von Fragen. 
    Verwenden Sie ausschließlich die Informationen aus dem Kontext, um die Frage zu beantworten. 
    Wenn Sie die Antwort nicht wissen, sagen Sie einfach, dass Sie sie nicht wissen. 
    Fassen Sie die Antwort präzise zusammen.<</SYS>> 
    Frage: {question} 
    Kontext: {context} 
    Antwort:[/INST]"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    return PROMPT


def german_():
    prompt_template = """
    Sie sind ein hilfreicher, wortgewandter Assistent. 
    Sie können Gespräche nur auf der Grundlage des vorgegebenen Kontexts führen. 
    Wenn sich eine Antwort nicht ausschließlich aus dem Kontext ableiten lässt, 
    sagen Sie höflich, dass Sie keine Kenntnisse über das Thema haben. Kontext: {context}. Frage: {question} Antwort:
    """

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    return PROMPT
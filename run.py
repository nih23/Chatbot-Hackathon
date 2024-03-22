from zenml import pipeline, step
from hackllm.backend.langchain_connector import getLLM_TGI


@step
def get_data(name_dataset: str):
    return "hello world test query"


@step
def llm_inference(input_one: str, llm: str):
    if(llm == "TGI"):
        llm = getLLM_TGI()
    res = llm(input_one)
    return res

@step
def visualize_data(input_one: str):
    print("visualize")


@pipeline
def llm_pipeline(name_dataset: str, llm: str):
  data = get_data(name_dataset)
  llm_output = llm_inference(data, llm)
  visualize_data(str(llm_output))
  

llm_pipeline(name_dataset = "ds1", llm = "TGI")
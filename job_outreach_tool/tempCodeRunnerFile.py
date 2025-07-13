from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://job-boards.greenhouse.io/coursera/jobs/5554771004?gh_src=6d6e4f994us")
page_data=loader.load().pop().page_content
print(page_data)
from pypdf import PdfReader
import os

def load_knowledge():

    knowledge = ""

    # Resume

    try:
        reader = PdfReader("../data/resume/resume.pdf")

        for page in reader.pages:
            text = page.extract_text()

            if text:
                knowledge += text + "\n"

    except:
        pass

    # GitHub Docs

    github_folder = "../data/github"

    if os.path.exists(github_folder):

        for filename in os.listdir(github_folder):

            if filename.endswith(".txt"):

                path = os.path.join(github_folder, filename)

                with open(path, "r", encoding="utf-8") as f:

                    knowledge += "\n" + f.read()

    return knowledge
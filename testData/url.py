import os
import time
import boto3
import json

def find_files_with_extensions(directory, extensions):
    file_paths = []
    filenames = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_paths.append(os.path.join(root, file))
                filenames.append(os.path.splitext(file)[0])
    return file_paths, filenames

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
        return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred while counting lines: {str(e)}")

def genrate_doc(path , outputfile):
    file_path = path  # Replace with the actual file path
    with open(file_path, "r") as file:
        file_contents = file.read()
    prompt = file_contents + "\n" + "Please provide a detailed and step-by-step explanation of the business logic implemented in the above software code, making sure that your response does not exceed 800 tokens. Use the format below to describe- \
    1. Main functionalities and processing steps: \
    2. Expected input: \
    3. Expected output:"
    payload = {
        "inputs":  
        [
        [
                {"role": "user", "content": prompt}
            ]  
        ],
    "parameters":{"max_new_tokens":800, "top_p":0.9, "temperature":0.6}
    }
    response = runtime.invoke_endpoint(EndpointName = ENDPOINT_NAME, ContentType="application/json", Body=json.dumps(payload),CustomAttributes="accept_eula=true")
    generation = json.loads(response['Body'].read().decode('utf-8'))
    final_response = generation[0]['generation']['content']
    with open(outputfile, "a") as file:
        file.write(file_contents + "\n" + "````" + "\n\n" + final_response)

def create_MD_files(filenames,path):
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join("docs", f"{filenames}.md")
        with open(file_path, 'w') as file:
            file.write("````" + "\n" +"Filepath: " + path + "\n")
        print(f"Created file: {file_path}")
        return file_path
    except Exception as e:
        print(f"An error occurred while creating files: {str(e)}")



ENDPOINT_NAME = "doc"
directory = 'Portal'
extensions = ['.py', '.java', '.cs', '.js', '.ts','php']
file_paths, filenames = find_files_with_extensions(directory, extensions)
no=0
for path in file_paths:
    line_count = count_lines_in_file(path)
    if line_count < 270:
        output_path=create_MD_files(filenames[no],path)
        print(output_path)
        genrate_doc(path,output_path)
        time.sleep(5)
    else:
       continue
    no = no + 1

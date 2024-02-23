from bardapi import Bard
import os
import time

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
    token = "YwhAX3g1ZM6bDsdIGARbjNsqZJ8d97nb6un8yPURrhuRSo-8rwJfF1t8_qd7DweRugZiDQ."
    bard = Bard(token=token)
    output=bard.get_answer(file_contents + "\n" + "here's detailed explaination what the above code does...")['content']
    with open(outputfile, "a") as file:
        file.write("```"+ file_contents + "\n" + output + "```")

def gen_improvment(path , outputfile):
    file_path = path  # Replace with the actual file path
    with open(file_path, "r") as file:
        file_contents = file.read()
    token = "YwhAX3g1ZM6bDsdIGARbjNsqZJ8d97nb6un8yPURrhuRSo-8rwJfF1t8_qd7DweRugZiDQ."
    bard = Bard(token=token)
    output=bard.get_answer(file_contents + "/n" + "here's are the some code improvement at security/coding practice/code health point of view along with modified code...")['content']
    with open(outputfile, "a") as file:
        file.write(output)

def create_text_files(filenames,path):
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join("web-goat-doc\docs", f"{filenames}.md")
        with open(file_path, 'w') as file:
            file.write("Filepath: " + path + "/n")
        print(f"Created file: {file_path}")
        return file_path
    except Exception as e:
        print(f"An error occurred while creating files: {str(e)}")

directory = 'WebGoat-main'
extensions = ['.py', '.java', '.c', '.js', '.ts']
file_paths, filenames = find_files_with_extensions(directory, extensions)
no=0 
for path in file_paths:
    line_count = count_lines_in_file(path)
    if line_count < 250:
        output_path=create_text_files(filenames[no],path)
        print(output_path)
        genrate_doc(path,output_path)
        time.sleep(15)
        #gen_improvment(path,output_path)
    else:
        output_path=create_text_files(filenames[no],path)
        with open(output_path, 'w') as file:
            file.write("\n" + "Sorry, file contain greater than 200 lines")
    no = no + 1



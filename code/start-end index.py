import os

folder_path = ""

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        with open(os.path.join(folder_path, filename), "r") as f:
            content = f.read()

        start_index = content.find("What this research")
        end_index1 = content.find("Material, data,")
        end_index2 = content.find("Materials, data,")
        end_index3 = content.find("How to cite this")

        if start_index != -1 and end_index1 != -1:
            new_content = content[start_index:end_index1]
            with open(os.path.join(folder_path, filename), "w") as f:
                f.write(new_content)
      
        elif start_index != -1 and end_index2 != -1:
            new_content = content[start_index:end_index2]
            with open(os.path.join(folder_path, filename), "w") as f:
                f.write(new_content)

        elif start_index != -1 and end_index3 != -1:
            new_content = content[start_index:end_index3]
            with open(os.path.join(folder_path, filename), "w") as f:
                f.write(new_content)

print("Done.")

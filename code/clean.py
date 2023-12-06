import os

input_folder = ""
output_folder = ""

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(input_folder, filename), "r") as input_file:
            text = input_file.read()
        
        text = text.replace("\n\n","\n")
    
        text = text.replace(" \n"," ")

        text = text.replace("","\n●")
        text = text.replace("-\n","-")

        text = text.replace("  ", " ")
        text = text.replace(" \n", " ")
        text = text.replace("●", "\n●")
        text = text.replace("•","\n●")
        text = text.replace("⚫","\n●")

        text = text.replace("What this research was about and why it is important", "\nWhat this research was about and why it is important \n")
        text = text.replace("What the researchers did","\nWhat the researchers did\n")
        text = text.replace("What the researchers found","\nWhat the researchers found\n")
        text = text.replace("Things to consider", "\nThings to consider\n")

        with open(os.path.join(output_folder, filename), "w") as output_file:
            output_file.write(text)
print("Done.")

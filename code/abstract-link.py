import os

def copy_before_hello(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    hello_index1 = content.find('What this research')
    hello_index2 = content.find('What this study')

    if hello_index1 >= 0 or hello_index2 >= 0:
        filename = os.path.basename(filepath)
        folder_path = os.path.dirname(filepath)

        new_filename = f"A_{filename}"
        new_filepath = os.path.join(folder_path, new_filename)

    if hello_index1 >= 0:
        with open(new_filepath, 'w') as f:
            f.write(content[:hello_index1])

    if hello_index2 >= 0:
        with open(new_filepath, 'w') as f:
            f.write(content[:hello_index2])



folder_path = ''
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder_path, filename)
        copy_before_hello(filepath)

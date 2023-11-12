import os
from PIL import Image

def list_files(directory):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sort the list of files
    files.sort()

    return files

def rename_files(file_list, counts_by_image_type, dimensions_by_image_type):
    local_counter = {}
    for cluster_num in counts_by_image_type.keys():
        local_counter[cluster_num] = 1
    counter = 0
    thresholds = [0]
    sum = 0
    for count in counts_by_image_type.values():
        sum += count
        thresholds.append(sum)
    for file_name in file_list:
        cumulative_sum = 0
        i = 1
        while counter > cumulative_sum:
            cumulative_sum += counts_by_image_type[i]
            i += 1
        (height, width) = dimensions_by_image_type[i]
        new_file_name = "ref_img_" + str(width) + "_" + str(height) + "_" + str(local_counter[i])
        output_path = "../data/updated-names/" + new_file_name
        local_counter[i] += 1

        # load image and save under new name/format
        with Image.open(file_name) as img:
            img.save(output_path = output_path, format = 'PNG')




# Example usage
directory_path = "../data/raw-names"
file_list = list_files(directory_path)
counts_by_image_type = {
    1: 8,
    2: 30,
    3: 23,
    4: 28,
    5: 30,
    6: 25,
    7: 34,
    8: 30,
    9: 33
}
dimensions_by_image_type = {
    1: (height, width)
}

print("List of files in sorted order:")
for file_name in file_list:
    print(file_name)

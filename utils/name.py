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
        i = get_cluster(counter, counts_by_image_type)
        ((or_height, or_width), (rd_height, rd_width)) = dimensions_by_image_type[i]
        new_file_name = "ref_img_" + str(or_height) + "_" + str(rd_height) + "_" + str(rd_width) + "_" + str(local_counter[i])
        output_path = "./data/updated-images/" + new_file_name
        local_counter[i] += 1
        counter += 1
        # load image and save under new name/format
        with Image.open("./data/raw-images/" + file_name) as img:
            print("Just saved " + output_path + ".PNG")
            img.save(output_path, format = 'PNG')

def get_cluster(counter, counts_by_image_type):
    i = 1 # 1
    sum = counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1 # 2
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1 # 3
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1 # 4
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1 # 5
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1  # 6
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1 # 7
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1  # 8
    sum += counts_by_image_type[i]
    if counter < sum:
        return i
    i += 1  # 9
    sum += counts_by_image_type[i]
    if counter < sum:
        return i

# Example usage
def main():
    directory_path = "./data/raw-images"
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

    # tuples in order of orange object, red object
    # within tuple, it is height and then width (both in cm)
    dimensions_by_image_type = {
        1: ((2, 5), (5, 5)),
        2: ((1, 2), (2.5, 5)),
        3: ((2, 2), (5, 10)),
        4: ((2, 5), (2.5, 10)),
        5: ((2, 2.5), (1, 5)),
        6: ((2, 2.5), (5, 5)),
        7: ((0.5, 2.5), (2.5, 5)),
        8: ((2, 5), (10, 10)),
        9: ((0.5, 2.5), (1, 5))
    }

    rename_files(file_list, counts_by_image_type, dimensions_by_image_type)

if __name__ == "__main__":
    main()

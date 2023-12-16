import os
print(os.getcwd())
# a = os.getcwd()
file = "rgbd_dataset_freiburg3_walking_halfsphere/rgbd_dataset_freiburg3_walking_halfsphere/rgb.txt"

# print(file)
a=[]
with open(file, 'r') as file:
    for _ in range(3):
        next(file)
    for line in file:
        a.append(line.split()[0])
        # print(line.split(), end='')  # end='' is used to avoid extra newlines as each line already contains one
map_dict ={}
for i in range(len(a)):
  map_dict[a[i]] = i+1
# print(map_dict)


def rename_images(input_folder,op_folder):
    # Get a list of files in the input folder
     # Get a list of files in the input folder
    files = os.listdir(input_folder)

    # Filter only image files (you might want to add more sophisticated checks)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    # print(len(image_files))
    # for i in image_files:
    #   print(i)
    # # Rename and move each image
    for old_filename in image_files:
        # print(old_filename)
        # Modify the filename as needed (you can use any logic here)
        new_filename = f"n{old_filename}"
        old_file = old_filename.split(".")
        old_file_join = old_file[0] + "." +  old_file[1]
        new_filename = str(map_dict[old_file_join])+".png"
        # print(old_file_join,new_filename)
        # print(new_filename)
        # # Full paths for the old and new filenames
        old_filepath = os.path.join(input_folder, old_filename)
        new_filepath = os.path.join(op_folder, new_filename)

        # # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {old_filename} to {new_filename}")


if __name__ == "__main__":
    # Specify your input folder
    input_folder = "rgbd_dataset_freiburg3_walking_halfsphere/rgbd_dataset_freiburg3_walking_halfsphere/rgb"
    op_folder = "rgbd_dataset_freiburg3_walking_halfsphere/rgbd_dataset_freiburg3_walking_halfsphere/ordered_dataset"

    # Call the function
    rename_images(input_folder,op_folder)
import numpy as np
import cv2


# Function that gets image with black coordinates(encrypted message).
# Then finds the message inside of it
def find_terrorist_message_in_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Set threshold level
    threshold_level = 50

    # Find coordinates of all pixels below threshold
    coords = np.column_stack(np.where(gray < threshold_level))

    coordinates_as_pair_list = [(coord[0], coord[1]) for coord in list(coords)]

    # Sort coordinates by column
    coordinates_as_pair_list.sort(key=lambda x: x[1])

    # Switch the column coords to characters by using 'chr'
    coords_as_char = [chr(coord[0]) for coord in coordinates_as_pair_list]

    # Create string from the character list
    terrorist_string = ''.join(coord for coord in coords_as_char)
    return terrorist_string


if __name__ == '__main__':
    img = cv2.imread("code.png")  # open image
    print(find_terrorist_message_in_image(img))



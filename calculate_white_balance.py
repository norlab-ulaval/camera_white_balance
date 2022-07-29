import matplotlib.pyplot as plt
import numpy as np
import cv2 # BGR
import sys

### Functions

def select_center_image(image_original):
    r = cv2.selectROI("ROI Selector", image_original, fromCenter=False)
    cv2.destroyAllWindows()
    image_cropped = image_original[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Image Cropped", image_cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_cropped

def print_ratios_from_mean_pixels(image, max_value_intesity):
    ratios = [np.mean((image[:,:,1])/(image[:,:,i])) for i in range(0,3)]
    print(f"Ratio G/B: {ratios[0]}\nRatio G/G: {ratios[1]}\nRatio G/R: {ratios[2]}")
    return

def show_evolution_width_image_and_ratio_from_width(image, max_value_intesity):
    fig = plt.figure()
    ax = fig.add_subplot()
    x_axis = np.linspace(0, image.shape[1], image.shape[1])
    color = ["blue", "green", "red"]
    ratio = [np.mean((image[int(image.shape[0]/2), :,1]/max_value_intesity)/(image[int(image.shape[0]/2), :,i]/max_value_intesity)) for i in range(0,3)]
    ax.table(
        cellText=[[f"{ratio[0]:.5f}"],[f"{ratio[1]:.5f}"],[f"{ratio[2]:.5f}"]],
        cellLoc="center",
        colWidths=[0.3]*1,
        colLabels=["Ratio Channel/Green"],
        rowLabels=["Blue", "Green", "Red"],
        zorder=5,
        loc=0   
    )
    for i in range(0,3):
        ax.plot(x_axis, image[int(image.shape[0]/2), :,i]/max_value_intesity, color=color[i])
    ax.set_xlabel("width camera image (pixel)")
    ax.set_ylabel("Channels intensity (normalized)")
    ax.set_ylim([0,1])
    plt.show()
    return

### Parameters
max_value_intesity = 255 # 8bits

def main():
    try:
        image = cv2.imread(sys.argv[1])
    except:
        print("Please enter a valid image file as first argument. The second argument is a boolean to display the ratio along one line of the image")
        exit()
    if image is None:
        print("File name not valid. Need to give an image format. Please enter a valid image file as first argument.")
        exit()
    image_center = select_center_image(image)
    print_ratios_from_mean_pixels(image_center, max_value_intesity)
    if sys.argv[2] == "True":
        print("Displaying the ratio not working for now. Segmentation fault.")
        show_evolution_width_image_and_ratio_from_width(image_center, max_value_intesity)

if __name__ == "__main__":
    main()

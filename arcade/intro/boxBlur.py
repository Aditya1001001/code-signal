""" Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral!
You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way:
Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x,
including x itself. All the pixels on the border of x are then removed.
Return the blurred image as an integer, with the fractions rounded down. """

def neighbour_sum(image,i,j):
    sum = 0
    for h in range(i-1,i+2):
        for k in range(j-1,j+2):
            sum += image[h][k]
    sum = math.floor(sum / 9)
    return sum

def boxBlur(image):
    height,width = len(image), len(image[0])
    output = []
    for i in range(1,height-1):
        temp = []
        for j in range(1, width-1):
            blurred_pixel = neighbour_sum(image,i,j)
            temp.append(blurred_pixel)
        output.append(temp)
    return output
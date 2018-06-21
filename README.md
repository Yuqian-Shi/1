# Turtle Shell
Code for assignments in Unimelb.

---

Your task is to write a program that will create an RGB image. The image will be a repeating turtle-shell-inspired pattern of size and colour based on the user's input.

Input:

    Using the first line of input, your program should ask the user for the size of the image: two integers separated by a space. The first integer will be the image's width, and the second will be the image's height.
    Using the second line of input, your program should ask the user for the 'background colour' of the image: three integers separated by spaces. The three integers will be the colour's red value, green value, and blue value.
    Finally, using the third line of input, your program should ask the user for the 'line colour' of the image: three integers separated by spaces. The three integers will be the colour's red value, green value, and blue value.

Your program should create a repeating turtle shell pattern as described below, and save this new image to a file called output.png.

Your program should work for any size and with any colours.
The pattern:

Here's a closeup of the pixel-level detail in the shell pattern:

In this case, the pattern is 30 pixels in width and 28 pixels in height. The background colour is (92, 112, 100) and the line colour is (199, 201, 179).
In this case, the pattern is 30 pixels in width and 28 pixels in height. The background colour is (92, 112, 100) and the line colour is (199, 201, 179).

The top left corner of the pattern will be the same for every image—that's where the pattern starts. The pattern continues from there as many times as it takes to fill up the whole image size.

Notice that the pattern might not line up nicely with the bottom edge or the right edge, and that's okay.

Here's an example of correct program interaction:

Enter size of image (width height): 255 127

Enter background colour (r g b): 0 255 0

Enter line colour (r g b): 0 0 0

output.png

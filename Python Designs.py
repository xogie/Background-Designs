from PIL import Image, ImageDraw
import os
import random
import time

def create_random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_gradient_background(width, height, color1, color2):
    """Create an image with a vertical gradient from color1 to color2."""
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for i in range(width):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / width))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / width))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / width))
        draw.line((i, 0, i, height), fill=(r, g, b))

    return image

def add_vertical_stripes(image, stripe_width, stripe_color, line_color):
    """Add vertical stripes with edge lines to the image."""
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for i in range(0, width, stripe_width * 2):
        # Draw the stripe
        draw.rectangle([i, 0, i + stripe_width, height], fill=stripe_color)
        # Draw lines on the edges of the stripe to make them pop
        if i > 0:
            draw.line([i - 1, 0, i - 1, height], fill=line_color, width=5)  # Left edge
        draw.line([i + stripe_width, 0, i + stripe_width, height], fill=line_color, width=5)  # Right edge

def add_horizontal_lines(image, line_spacing, line_color):
    """Add horizontal lines across the image."""
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for j in range(0, height, line_spacing * 2):
        draw.line([0, j, width, j], fill=line_color, width=5)

def add_diagonal_lines(image, line_spacing, line_color):
    """Add diagonal lines across the image."""
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # Draw diagonals from top left to bottom right
    for i in range(-height, width, line_spacing * 2):
        draw.line([i, 0, i + height, height], fill=line_color, width=5)

    # Draw diagonals from top right to bottom left
    for i in range(0, width + height, line_spacing * 2):
        draw.line([i, 0, i - height, height], fill=line_color, width=5)

def save_image(image, save_directory, filename):
    """Save the image to the specified directory."""
    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)
    save_path = os.path.join(save_directory, filename)
    image.save(save_path)
    print(f"Image saved to {save_path}")

def generate_and_save_image():
    # Define the dimensions
    width, height = 12080, 10920
    stripe_width = 400  # Adjusted stripe width for larger image size

    # Generate random colors
    color1 = create_random_color()  # Random dark color for the gradient start
    color2 = create_random_color()  # Random light color for the gradient end
    stripe_color = create_random_color()  # Random color for the stripes
    line_color = (200, 200, 200)  # Light grey color for the edges

    # Create the gradient background
    background = create_gradient_background(width, height, color1, color2)

    # Add the vertical stripes with edge lines
    add_vertical_stripes(background, stripe_width, stripe_color, line_color)

    # Optionally add horizontal and diagonal lines
    add_horizontal_lines(background, stripe_width, line_color)
    add_diagonal_lines(background, stripe_width, line_color)

    # Define the directory for saving the image
    save_directory = os.path.join(os.path.expanduser("~"), "Desktop")

    # Generate a unique filename with timestamp
    timestamp = int(time.time())
    filename = f"gradient_background_{timestamp}.png"

    # Save the image
    save_image(background, save_directory, filename)

# Run the image generation and saving function
generate_and_save_image()

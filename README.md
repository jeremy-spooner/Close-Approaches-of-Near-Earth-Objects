# Motivational Meme Generator
The Motivational Meme Generator is an application to generate memes, including an image with an overlaid quote. The user can choose a custom quote and image from a url or it can be randomized from default images and quotes.

## Functionality
* Interact with a variety of complex filetypes.
* Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Load, manipulate, and save images.
* Accept dynamic user input through a command-line tool and a web service.

## External Libraries
All required dependencies are listed in the root requirements.txt file.

## Running the Program
The project can be run from the command line or through a web server.

### Using Command Line
To run the application through the command line use:
`python meme.py [--body] [--author] [--path]`
The program takes three optional arguments:
* A string quote body
* A string quote author
* An image path

If any of the arguments are undefined through the command line then random options are selected.

### Using Web Server
To run the application using a web server run:
`python app.py`
The opening page will generate a random meme based on default images and quotes. You can also choose creator mode where you can upload an image from the internet and write your own quote and author.

## Modules

### MemeEngine
The Meme Engine Module is responsible for manipulating and drawing text onto images. It resizes the image to a default 500 pixel width and saves it to a new location.

### QuoteEngine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. A quote contains a body and an author:
`"This is a quote body" - Author`
It contains an ingestor class that can read quoptes for csv, docx, pdf, and txt file types.

### Udacity
This project is based on Udacity's Nanodegree program, Intermediate Python.
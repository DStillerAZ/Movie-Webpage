import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Yelly's Favourite Movies</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .page-header {
            border: 0;
            text-align: center;
        }

        .header-image {
            height: 200px;
            border-radius: 100px;
        }
        
        .image-container {
            float: left;
            
        }

        .page-title {
            color: #ca01fd;
            background-color: black;
            font-size: 32px;
            border-radius: 500px;
            text-align: center;
            padding: 75px;
        }

        .movie-border {
            background-color: black;
            border-radius: 285px;
            color: #ca01fd;
            font-size: 20px;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin: 15px 0;
            padding: 65px;
            font-family: "ubuntu";
            color: #B8008A;
        }
        .movie-tile:hover {
            background-color: #ca01fd;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body style="background-color:#14000F">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
        
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    
    <div class="container">
    <div class="page-header col-md-12">
<div class="image-container col-md-2">
<img class="header-image" src="https://c2.staticflickr.com/2/1341/1163426260_cb1e915674_b.jpg" alt="Purple jellyfish">
  </div>

<div class="page-title col-md-7 col-md-offset-2">
  Yelly's Favourite Movies
   </div>
  </div>
      {movie_tiles}
      </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''

<div class="movie-border col-md-6 col-lg-6 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
        movie_title=movie.title,
        poster_image_url=movie.poster_image_url,
        trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
    movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

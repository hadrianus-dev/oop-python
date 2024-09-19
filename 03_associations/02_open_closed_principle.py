class Artist:
    # Open for extension, closed for modification
    def __init__(self, type):
        self.type = type

    def showing(self):
        print(f'The {self.type} artist, is showing')

class Theater:
    # Open for extension, closed for modification
    def presentation(self, artist: Artist):
        print('-----The presentation is started')
        artist.showing()
        print('-----The public is applauding')

# Closed for modification
artist = Artist('Singer')
# Open for extension
theater = Theater()
# Open for extension
theater.presentation(artist)
# PyGame Practice Programs

### Basic pygame Data Types

#### pygame.Rect
    - Represent a rectangular space's location and size.
    - Contains the colliderect() method that checks whether they are colliding with another Rect object.

#### pygame.Surface
    - Surface objects are areas of colored pixels.
    - Represents a rectangular image, while a Rect object represents only a rectangular space and location.
    - Contains the blit() method that is used to draw the image on one Surface object onto another Surface object.

#### pygame.event.Event
    - Generates Event objects whenever the user provides keyboard, mouse, or other input.
    - The get() function returns a list of these Event objects.

#### pygame.font.Font
    - Uses the Font data type, which represents the typeface used for text in pygame.
    - Arguments of pygame.font.SysFont() are a string of the Font name, and an integer of the font size.

#### pygame.time.Clock
    - Helpful for keeping our games from running faster than the player can see.
    - Contains the tick() method, which can be passed the number of FPS we want the game to run.



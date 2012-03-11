import pyglet
# To avoid a particular bug crashing on my laptop
pyglet.options['graphics_vbo'] = False 

# Create game window and GUI
window = pyglet.window.Window()

# Initialise global objects like sprites of PC and NPC
player = pyglet.sprite.Sprite(pyglet.image.load("catcher.png"))

@window.event
def on_mouse_motion(x, y, dx, dy):
    player.x, player.y = x, 100

@window.event
def on_draw():
    window.clear()
    player.draw()

pyglet.app.run()

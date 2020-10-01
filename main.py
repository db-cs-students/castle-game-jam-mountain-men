"""
Title:Mountian Master
Creators: Hayden and Brady
Description: A adventure to reach the castle and find the 
treasure, make your way up a frosty Mountian that many have tried to take
on.
"""
## Tile map 1 test
scene.set_tile_map(img("""
    ........................................................................................................................................................................................................
    ............................................................................7...........................................................................................................................
    ....................................................................................ffffffffffffffffffff................................................................................................
    ..........................................................................7......ffffaaaaaaaaaaaaaaaaaaffff.............................................................................................
    .....................fffff......................................................ffaaaaaaaaaaaaaa9aaaaaaaaafff...........................................................................................
    .............................................................................fffaaaaaaaaaaaaaaaaaaaaaaaaaaaaff.................................................................................fffffffff
    ...........................................................................ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafff.............fff..............ffff............................................faaaaaaaaa
    ....................ffffff.....7......7..........................7......fffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffff.........ffaff...........fffaaaf.........................................ffaaaaaaaaaa
    ...................faaaaaaff.................ffffff.....7..............ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff......fffaaaffff........faaaaaaf.......................................faaaaaaaaaaaa
    .......7..........faaaaaaaaffff.............ffaaaaaff................fffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafffffffaaaaaaaaaf........faaaaaaf.......................................faaaaaaaaaaaa
    .............ffffffaaaaaaaaaaaaf...........ffaaaaaaaff......7.......ffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafffff....faaaaaaf.....................ffff.............faaaaaaaaaaaaa
    fffffffffffffaaaaaaaaaaaaaaaaaafffffffffffffaaaaaa9aaaff.......fffffaaaa9aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaff..faaaaaaaf.....................faaf............ffaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaa9aaaaaaaaaaaaaaaaaaaaaaaaaaaff.....ffaaaaaaaaaaaaaaaaaaaaaaa9aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafffaaaaaaaafff...................faaff..........faaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa9aaaaaaaaaaaaaaaaaafffffffaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaf.......ff.........faaaaf..........faaaaaaaaaaaaaaa
    aaaaaaaaaaaaa9aaaaaaaaaaaaaaaaaaaaaaaaaaaa9aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffffafffff....ffaaaaf.........ffaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaffffffaaaaaf....ffffffaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaafffffaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""))
scene.set_tile(15, img("""
    f f f f f f f f f f f f f f f f
    f f f f f f f f f f f f f f f f
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
"""),True)
scene.set_tile(7, img("""
    ....................
    ....................
    ....................
    ....................
    .....22...22........
    ....2222.2222.......
    ...22222222222......
    ...22222222222......
    ....222222222.......
    .....2222222........
    ......22222.........
    .......222..........
    ....................
    ....................
    ....................
    ....................
    ....................
    ....................
    ....................
    ....................
"""),True)
scene.set_tile(9, img("""
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
"""),True)
scene.set_tile(10, img("""
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeee
"""),True)
## sprite control and creation/location
mountianman1= sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . f f f f f f . . . .
    . . . . f f e e e e f 2 f . . .
    . . . f f e e e e f 2 2 2 f . .
    . . . f e e e f f e e e e f . .
    . . . f f f f e e 2 2 2 2 e f .
    . . . f e 2 2 2 f f f f e 2 f .
    . . f f f f f f f e e e f f f .
    . . f f e 4 4 e b f 4 4 e e f .
    . . f e e 4 d 4 1 f d d e f . .
    . . . f e e e 4 d d d d f . . .
    . . . . 4 d d e 4 4 4 e f . . .
    . . . . e d d e 2 2 2 2 f . . .
    . . . . f e e f 4 4 5 5 f f . .
    . . . . f f f f f f f f f f . .
    . . . . . f f . . . f f f . . .
"""))
controller.move_sprite(mountianman1)
scene.camera_follow_sprite(mountianman1)
mountianman1.set_position(20, 170)
mountianman1.ay = 100

## Jumping/Gravity 
can_double_jump = True
def jump():
    global can_double_jump
    if can_double_jump: 
        mountianman1.vy = -70
        can_double_jump = mountianman1.is_hitting_tile(CollisionDirection.BOTTOM)
controller.A.on_event(ControllerButtonEvent.PRESSED, jump)
controller.move_sprite(mountianman1, 170, 0)

def on_update():
    global can_double_jump
    if mountianman1.is_hitting_tile(CollisionDirection.BOTTOM):
        can_double_jump = True
game.on_update(on_update)


### background
scene.set_background_image(img("""
    99999999999999999999999999999999999999999999999999999999999999999f9999999999999999999999999999999999999999999999999999999999999999991999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999f1f999999999999999999999999999999999999999999999999999999991119999111199999999999999999999999999
    9999999911199999999999999999999999999999999999999999999999999999f11f99999999999999999999999999999999999999999999999999999991111111111199999999999999999999999999
    9999911111111199999999999999999999999999999999999999999999999999f111f9999999999999999999999999999999999999999999999999999991111111111119999999999999999999999999
    999911111111111119999999999999999999999999999999999999999999999f11111f999999999999999999999999999999999999999999999999999111111111111111999999999999999999999999
    999111111111111111999999999999999999999999999999999999999999999f111111ff9999999999999999999999999999999999999999999991111111111111111111999999999999999999999999
    99911111111111111119999999999999999999999999999999999999999999f11f111111ff99999999999999999999999999999999999999999111111111111111111111199999999999999999999999
    9991111111111111111199999999999995555599999999999999999999999f111111f1111f99999999999999999999999999999999999999999111111111111111111111119999999999999999999999
    999111111111111111119999999999999555555999999999999999999999f1111111111111f9999999999999999999999999999999999999999111111111111111111111111999999999999999999999
    999911111111111111119999999999995555559999999999999999999999f1111111111117f9999999999999999999999999999999999999999111111111111111111111111999999999999999999999
    999111111111111111999999999999995555559999999999999999999999f1111177777777f9999999999999999999999999999999999999999911111111111111111111111199999999999999999999
    99911111111111111999999999999999555599999999999999999999999f77777777777777f9999999999999999999999999999999999999999911111111111111111111111999999999999999999999
    9999911111111119999999999999999999999999999999999999999999f777777777777777f9999999999999999999999999999999999999999991111111111111111111111199999999999999999999
    9999999991111999999999999999999999999999999999999999999999f7777777777777777f999999999999999999999999999999999999999999999111111111111111111119999999999999999999
    999999999999999999999999999999999999999999999999999999999f77777777777777777f999999999999999999999999999999999999999999999911111111111111111111999999999999999999
    99999999999999999999999999999999999999999999999999999999f7777777777777777777f99999999999999fffffff99999999999999999999999111111111111111111111199999999999999999
    9999999999999999999999999999999999999999999999999999999f777777777777777777777f999999999999f1111111fffffff9999999999999999991111111111111111111119999999999999999
    999999999999999999999999999999999999999999999999999999f77777777777777777777777f9999999999f11111111111111f9999999999999999999991111111111111111199999999999999999
    9999999999999999999999999999999999999999999999999fffff7777777777777777777777777f99999999f1111111111111111f199999999999999999f99991111111111119999999999999999999
    999999999999999999999999999999999999999999999ffff7171f77777777777777777777777777f9999999f1111111111111111119999999999999999f7f9999991111111199999999999999999999
    9999999999999999999999999999999999999999999f17777777f777777777777777777777777777f999999f7111111111111111177f99999999999999f777f999999999999999999999999999999999
    99999999999999999999999ffffff199ff9999999ff77717717f77777777777777777777777777777f9999f77711111111111111777f9999999999999f77777f99999999999999999999999999999999
    9999999999999999999999f771717fff77ff999ff717117777f7777777777777777777777777777777f99f7777777711111111777777f99999999999f7777777ff999999999999999999999999999999
    999999999999999999999f77717777777771fff77777777777f7777777777777777777777777777777f9f77777777771111177777777f99999999999f777777777ff9999999999999999999999999999
    9999999999999999999ff7777777777777777777777777777f777777777777777777777777777777777f777777777777717777777777f9999999999f777777777777fff9999999999999999999999999
    999999999ffffffffff777777777777777777777777777777f777777777777777777777777777777777f777777777777777777777777f999999999f7777777777777777ff99999999999999999999999
    99999ffff7777777777777777777777777777777777777777f7777777777777777777777777777777777f77777777777777777777777f99999999f777777777777777777f99999999999999999999999
    99fff7177177777777777777777777777777777777777777f77777777777777777777777777777777777f777777777777777777777777f9999999f777777777777777777f99999999999999999999999
    9f777777777777777777777777777777777777777777777f7777777777777777777777777777777777777f777777777777777777777777ff9999f7777777777777777777ff9999999999999999999999
    f7777777777777777777777777777777777777777777777f7777777777777777777777777777777777777f77777777777777777777777777f99f7777777777777777777777fff9999999999999999999
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777f777777777777777777777777777fff7777777777777777777777777fff9999999999999999
    77777777777777777777777777777777777777777777777777777777777777777777777777777777777777ff7777777777777777777777777ff77777777777777777777777777777ff99999999999999
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777f7777777777777777777777777f777777777777777777777777777777fff999999999999
    77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ff77777777777777777777777ff777777777777777777777777777777ff999999999999
    77777777777777777777777777777777777777777777777777777777777777777fff77777777777777777777777ffffffff77777777777777777ff7777777777777777777777777777f9999999999999
    77777777777777777777777777777777777777777777777777777777777777777777ffffff777777777777777777777777f7777777777777777777ff777777777777777777777777777ffff999999999
    77777777777777777777777777777777777777777777777777777777777777777777777777fff777777777777777777777f777777777777777777777fff777777777777777777777777777f999999999
    7777777777777777777777777777777777777777777777777777777777777777777777777777f777777777777777777777f777777777777777777777777fff7777777777777777777777777fff999999
    7777777777777777777777777777777777777777777777777777777777777777777777777777f777777777777777777777f777777777777777777777777777ff77777777777777777777777777ff9999
    7777777777777777777777777777777777777777777777777777777777777777777777777777f777777777777777777777ffff777777777777777777777777777777777777777777777777777777ff99
    7777777777777777777777777777777777777777777777777777777777777777777777777777f7777777777777777777777777fffff777777777777777777777777777777777777777777777777777ff
    777777777777777777777777777777777777777777777777777777777777777777777777777ff777777777777777777777777777777f7777777777777777777777777777777777777777777777777777
    77777777777777777777777777777777777777777777777777777777777777777777777777777ffff777777777777777777777777777f777777777777777777777777777777777777777777777777777
    777777777777777777777777777777777777777777777777777777777777777777777777777777777ffff777777777777777777777777ff7777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777ff777777777777777777777777f777777777777777777777777777777777777777777777777
    777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ff77777777777777777777777f77777777777777777777777777777777777777777777777
    77777777777777f77777777777777777777777777777777777777777777777777777777777777777777777777fff77777777777777777777777777777777777777777777777777ffff77777777777777
    777777777777ff7fffffffffff777777777777777777777777777777777777777777777777777777777777777777fff7777777777777777777777777777777777777777777ffffff77fff77777777777
    77777777777f77777777777777f7777777777777777777777777777777777777777777777777777777777777777777f77777777777777777777777777777777777777777fffff777f777f77777777777
    7777777777f777777777777777f7777777777777777777777777777777777777777777777777777777777777777777f77777777777777777777777777777777777777777f77fffffff77f77777777777
    777777777f7777777777777777f777777777777777777777777777777777777777777777777777777777777777777ff7777777777777777777777777777777777777777f7ff777777ff77fff77777777
    77777777f77777777777777777f77777777777777777777777777777777777777777777777777777777777777777777ffff77777777777777777777777777777777777fff777777777777777f7777777
    7777777f777777777777777777fffff77777777777777777777777777777777777777777777777777777777777777777777ff7777777777777777777777777777777fff777777777777777777ff77777
    7777fff777777777777777777777777fffff77777777777777777777777777777777777777777777777777777777777777777ff777777777777777777777777777ff77777777777777777777777f7777
    7fff777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777ff777777777777777777777777f77777777777777777777777777f777
    7f77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777f77
    7f777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777f7
    7f77777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    f777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))


#Rules


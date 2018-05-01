# 3 way to run function in package.
# 1
import package.sound.echo
package.sound.echo.echo_test()
# 2
from package.sound import echo
echo.echo_test()
# 3
from package.sound.echo import echo_test
echo_test()

# Nope 1 !
# import package.sound.echo.echo_test
# echo_test()

# Nope 2 !
# import package
# sound.echo.echo_test()

from package.graphic import *
render.render_test()
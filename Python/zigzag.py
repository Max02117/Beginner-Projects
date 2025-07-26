import time

indent = 0   # текущий отступ
indent_increasing = True   # направление движения

try:
    while True:
        print(' ' * indent + '********')
        time.sleep(0.1)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
    
except KeyboardInterrupt:
    pass
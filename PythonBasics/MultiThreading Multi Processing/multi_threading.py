import time
import threading

square_result = []
cube_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(0.3)
        print('Square ', str(n*n))
        square_result.append(n*n)

def calc_cube(numbers):
    global cube_result
    for n in numbers:
        time.sleep(0.3)
        print('Cube ', str(n*n*n))
        cube_result.append(n*n*n)

t = time.time()
arr = [4,7,9,15]

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print('square_result', square_result)
print('cube_result', cube_result)

print('Total time taken ', time.time() - t)
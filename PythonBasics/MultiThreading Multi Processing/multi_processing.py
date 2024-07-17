import time
import multiprocessing

def calc_square(numbers, square_result):
    for indx, n in enumerate(numbers):
        time.sleep(1)
        print('Square ', str(n*n))
        square_result[indx] = n*n

def calc_cube(numbers, cube_result):
    for n in numbers:
        time.sleep(1)
        print('Cube ', str(n*n*n))
        cube_result.put(n*n*n)

if __name__ == '__main__':
    print("********* Start ***********")
    t = time.time()
    arr = [4,7,9,15]
    square_result = multiprocessing.Array('i', 4)
    cube_result = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=calc_square, args=(arr,square_result))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,cube_result))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('square_result', square_result[:])
    while cube_result.empty() is False:
        print('cube_result', cube_result.get())

    print('Total time taken ', time.time() - t)
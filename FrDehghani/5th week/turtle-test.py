
# import turtle as t
# t.forward(20)
# # print(t.pos())  # (20 , 0)
# t.done()
# ---------------------------------
import time

# start = time.monotonic()
# # Simulate a delay
# time.sleep(2)
# end = time.monotonic()
#
# elapsed_time = end - start
# print(f"Elapsed time: {elapsed_time} seconds")
# for i in range(50):
#     print(time.monotonic()-time.time())
#     time.sleep(3)
# =============================================
print('*'*40)
time_list = ['time', 'monotonic', 'perf_counter', 'process_time', 'thread_time']

for i in time_list:
    print(time.get_clock_info(i))

# =============================================
print('*'*40)
print(time.monotonic())
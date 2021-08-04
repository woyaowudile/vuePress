import time

async def async_function():
    time.sleep(1)
    return 1

async def async_function2():
    time.sleep(2)
    return 2

async def await_coroutine():
    result2 = await async_function2()
    print(result2)
    result1 = await async_function()
    print(result1)
    

def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
        
run(await_coroutine())

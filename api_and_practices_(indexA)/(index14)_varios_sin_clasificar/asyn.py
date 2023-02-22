from asyncio import \
    run, sleep, wait
    
lista =[9,5,3,2,1,4,6,7,8,10]

async def print_num(n):
    await sleep(n)
    print(n)

run(wait([print_num (n) for n in lista]))
    

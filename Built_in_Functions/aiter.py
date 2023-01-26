import asyncio


class AsincIteratorWraper:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            val = next(self._it)
        except StopIteration:
            raise StopIteration
        return val


async def it(sequence):
    async for letter in AsincIteratorWraper(sequence):
        print(letter)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.gather(it('012345')))
finally:
    loop.close()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


class Reader:
    def __init__(self, a_str):
        self.a_str = a_str

    async def readline(self):
        ...

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self.readline()
        if value == b'':
            raise StopIteration
        print("----------------------------------------------------")
        return value


r = Reader("python")

import time

from fastapi import FastAPI

app = FastAPI()


def sleep():
    time.sleep(5)
    return "Done"


async def async_sleep():
    time.sleep(5)
    return "Done"


@app.get("/sync")
def read_sync():
    """
    パスオペレーション、sleep関数とも async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    print("Calling sleep")
    val = sleep()
    print("Sleep done")
    return {"Hello": val}


@app.get("/async-sync")
async def read_async_sync():
    """
    パスオペレーションは async で定義、sleep関数は async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    print("Calling sleep")
    val = sleep()
    print("Sleep done")
    return {"Hello": val}


@app.get("/async")
async def read_async():
    """
    パスオペレーション、sleep関数とも async で定義。
    呼び出すときは await あり。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    print("Calling async sleep")
    val = await async_sleep()
    print("Async sleep done")
    return {"Hello": val}


@app.get("/async-noreturn")
async def read_async_noreturn():
    """
    パスオペレーション、sleep関数とも async で定義。
    呼び出すときは await なし。
    バックグラウンド実行になる。
    関数の戻り値は使えない。
    """
    print("Calling async sleep")
    async_sleep()
    print("Async sleep done")
    return {"Hello": "World"}

import time

from fastapi import BackgroundTasks, FastAPI

from .lib import Common

app = FastAPI()


def sleep():
    c = Common()
    time.sleep(5)
    print("Sleep done")
    return c.name


async def async_sleep():
    c = Common()
    time.sleep(5)
    print("Async sleep done")
    return c.name


@app.get("/sync")
def read_sync():
    """
    パスオペレーション、sleep関数とも async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    print("Calling sleep")
    val = sleep()
    print("Done")
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
    print("Done")
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
    print("Done")
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
    print("Done")
    return {"Hello": "World"}


@app.get("/async-background")
async def read_async_background(background_tasks: BackgroundTasks):
    """
    パスオペレーションは async で定義、sleep関数は async なしで定義。
    background_tasks に追加することでバックグラウンド実行になる。
    関数の戻り値は使えない。
    """
    print("Calling sleep")
    background_tasks.add_task(sleep)
    print("Done")
    return {"Hello": "World"}

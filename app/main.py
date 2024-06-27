import time

from fastapi import BackgroundTasks, FastAPI

from .lib import Common

app = FastAPI()


def sleep():
    c = Common()
    c.get_logger()
    assert c.logger is not None

    c.logger.info("Sleep begin")
    print("Sleep begin")
    time.sleep(2)
    c.logger.info("Sleep done")
    print("Sleep done")
    return c.name


async def async_sleep():
    c = Common()
    c.get_logger()
    assert c.logger is not None

    c.logger.info("Async sleep begin")
    print("Async sleep begin")
    time.sleep(2)
    c.logger.info("Async sleep done")
    print("Async sleep done")
    return c.name


@app.get("/sync")
def read_sync():
    """
    パスオペレーション、sleep関数とも async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    print("Begin")
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
    print("Begin")
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
    print("Begin")
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
    print("Begin")
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
    print("Begin")
    background_tasks.add_task(sleep)
    print("Done")
    return {"Hello": "World"}

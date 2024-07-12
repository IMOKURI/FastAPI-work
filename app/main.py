import logging
import time

from fastapi import BackgroundTasks, FastAPI

from .lib import Common

app = FastAPI()
logger = logging.getLogger("uvicorn")


def sleep():
    c = Common()
    c.get_logger()
    assert c.logger is not None

    c.logger.info("Sleep begin")
    time.sleep(2)
    c.logger.info("Sleep done")

    return c.name


async def async_sleep():
    c = Common()
    c.get_logger()
    assert c.logger is not None

    c.logger.info("Async sleep begin")
    time.sleep(2)
    c.logger.info("Async sleep done")

    return c.name


def sleep_with(count):
    c = Common()
    c.get_logger()
    assert c.logger is not None

    c.logger.info(f"Sleep {count} begin")
    if count == 0:
        try:
            raise
        except Exception:
            time.sleep(count + 2)
    elif count == 1:
        raise
    else:
        time.sleep(count)
    c.logger.info(f"Sleep {count} done")

    return c.name


@app.get("/sync")
def read_sync():
    """
    パスオペレーション、sleep関数とも async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    logger.info("Begin")
    val = sleep()
    logger.info("Done")
    return {"Hello": val}


@app.get("/async-sync")
async def read_async_sync():
    """
    パスオペレーションは async で定義、sleep関数は async なしで定義。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    logger.info("Begin")
    val = sleep()
    logger.info("Done")
    return {"Hello": val}


@app.get("/async")
async def read_async():
    """
    パスオペレーション、sleep関数とも async で定義。
    呼び出すときは await あり。
    関数の戻り値が使える。
    処理完了までブロックされる。
    """
    logger.info("Begin")
    val = await async_sleep()
    logger.info("Done")
    return {"Hello": val}


@app.get("/async-noreturn")
async def read_async_noreturn():
    """
    パスオペレーション、sleep関数とも async で定義。
    呼び出すときは await なし。
    バックグラウンド実行になる。
    関数の戻り値は使えない。
    """
    logger.info("Begin")
    async_sleep()
    logger.info("Done")
    return {"Hello": "World"}


@app.get("/async-background")
async def read_async_background(background_tasks: BackgroundTasks):
    """
    パスオペレーションは async で定義、sleep関数は async なしで定義。
    background_tasks に追加することでバックグラウンド実行になる。
    関数の戻り値は使えない。
    """
    logger.info("Begin")
    background_tasks.add_task(sleep)
    logger.info("Done")
    return {"Hello": "World"}


@app.get("/async-background-with-error")
async def read_async_background_with_error(background_tasks: BackgroundTasks):
    """
    エラーハンドリングのテスト
    """
    logger.info("Begin")
    background_tasks.add_task(sleep_with, 1)
    logger.info("Done")
    return {"Hello": "World"}


@app.get("/async-background-catch-error")
async def read_async_background_catch_error(background_tasks: BackgroundTasks):
    """
    エラーハンドリングのテスト
    """
    logger.info("Begin")
    background_tasks.add_task(sleep_with, 0)
    logger.info("Done")
    return {"Hello": "World"}

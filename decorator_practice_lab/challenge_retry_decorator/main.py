def retry_decorator(func):
    def wrapper(*args, **kwargs):
        last_exception = None

        # ① 最大3回のループを用意
        for attempt in range(1, 4):
            try:
                # ② 関数を試しに実行
                return func(*args, **kwargs)
            except Exception as e:
                # ③ 失敗した例外を保持
                last_exception = e
                print(f"Attempt {attempt} failed: {e!r}")
        # ④ 3回とも失敗したら最後の例外を再送出
        raise last_exception

    return wrapper

@retry_decorator
def sometimes_fails():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"

if __name__ == "__main__":
    try:
        result = sometimes_fails()
    except Exception as e:
        result = f"All retries failed: {e}"
    print(result)
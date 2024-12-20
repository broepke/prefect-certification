from prefect import flow, task
import pandas as pd


@task(persist_result=True)
def my_task():
    df = pd.DataFrame(dict(a=[2, 3], b=[4, 5]))
    return df


@flow(log_prints=True)
def my_flow():
    res = my_task()
    print(res)


if __name__ == "__main__":
    my_flow()

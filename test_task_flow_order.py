from prefect import flow, task


@task(name="add two")
def add_two(y):
    return y + 2


@task(name="double")
def double_me(x):
    return x * 2

@task(name="double plus two")
def double_plus_two(z):
    a = double_me(z)
    b = add_two(a)
    return b

@flow(log_prints=True)
def my_flow(input_number):
    res = double_plus_two(input_number)
    print("The final number is:", res)


if __name__ == "__main__":
    my_flow.from_source(
        source="https://github.com/broepke/prefect-certification.git",
        entrypoint="test_task_flow_order.py:my_flow",
    ).deploy(
        name="double-plus-two",
        work_pool_name="dka-managed",
        parameters={"input_number": 11},
    )

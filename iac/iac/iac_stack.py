from aws_cdk import Duration, Stack
from aws_cdk.aws_iam import Effect, PolicyStatement
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_fn = PythonFunction(
            self,
            "HelloFn",
            entry="../server/server/handlers",
            index="hello_handler.py",
            runtime=Runtime.PYTHON_3_12,
            memory_size=1769,  # 1vCPUフルパワー @see https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/gettingstarted-limits.html
            timeout=Duration.minutes(15),
        )
        hello_fn.add_to_role_policy(
            PolicyStatement(
                effect=Effect.ALLOW,
                actions=["kendra:Query", "bedrock:InvokeModel"],
                resources=["*"],
            )
        )

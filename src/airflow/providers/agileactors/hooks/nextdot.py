class UserAPIHook:
    def __init__(
        self,
        username: str,
        access_token: str,
    ) -> None:
        self._name = username
        self._tkn = access_token

    def test_connection(self) -> bool:  # noqa: PLR6301
        return True

    def connect(self) -> bool:
        print(f"Successfully connected as <{self._name}")

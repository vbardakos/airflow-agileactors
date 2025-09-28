from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self


class SubmitDotOperator:
    """
    Adds a new dot for user
    :param connection: User connection info fmt dot://username@token:role
    :param title: Dot Title
    :param content: Dot Content
    :param mentions: List of people and groups
    :param params: Dot metadata (role, timedelta etc)
    """

    def __init__(
        self,
        connection: str,
        title: str,
        content: str,
        mentions: Iterable | None = None,
        params: dict[str, Any] | None = None,
    ) -> None:
        self.__conn = connection
        self.__title = title
        self.__content = content
        self.__mentions = mentions or ()
        self.__kwargs = params or {}

    def execute(self, content) -> Any:  # noqa: ARG002
        """
        There's no going back if you execute me
        """
        print(
            "Dot successfully posted:",
            f"Title: {self.__title}",
            f"Content: {self.__content}",
            f"Mentions: {list(self.__mentions)}",
            sep="\n======\n",
        )

    @classmethod
    def test_instance(cls) -> Self:
        """
        There's going back if you execute me
        """
        return cls(
            "dot://mockuser@secrettoken:adminSome mock title",
            "Some more random text to fill the field",
            ["@foo", "@bar", "@baz"],
        )

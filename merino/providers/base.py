from abc import ABC, abstractmethod
from typing import Any


class BaseProvider(ABC):
    """
    Abstract class for suggestion providers.
    """

    @abstractmethod
    async def initialize(self) -> None:
        """
        Abstract method for defining an initialize method for bootstrapping the Provider.
        This allows us to use Async API's within as well as initialize providers in parallel

        """
        ...

    @abstractmethod
    async def query(self, query: str) -> list[dict[str, Any]]:
        ...

    @abstractmethod
    def enabled_by_default(self) -> bool:
        ...

    def hidden(self) -> bool:
        return False

    def availability(self) -> str:
        if self.hidden():
            return "hidden"
        elif self.enabled_by_default():
            return "enabled_by_default"
        else:
            return "disabled_by_default"

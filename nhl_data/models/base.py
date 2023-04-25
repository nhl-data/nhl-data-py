from abc import ABC, abstractmethod


class Model(ABC):
    """
    Base class that all Models from the NHL API are based off of.
    """

    @abstractmethod
    def from_response(cls, data: dict):  # pragma: no cover
        """
        Helper function which removes specific keywords / fields from the
        response data depending on the Model, and incorporates other models
        when applicable.
        It preserves the dataclass' `__init__` method, making initialization
        easier for all subclasses.

        This should be called rather than the model's `__init__` method.
        This is because this method will account for possible data fields that may be
        included from some response data, that is not accounted for in models.
        Additionally, it replaces all camelCase fields to snake_case.

        :param data: dictionary containing all the data (e.g. the response data)
        :return: an instance of the model
        """
        raise NotImplementedError

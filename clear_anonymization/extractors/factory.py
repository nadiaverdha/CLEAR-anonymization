"""Factory function for creating extractor instances."""

from __future__ import annotations

from clear_anonymization.extractors.base import BaseExtractor

__all__ = ["make_extractor"]


def make_extractor(method: str, **kwargs) -> BaseExtractor:
    """Create an extractor of the requested type with the given parameters.

    :param method: llm for now
    :param kwargs: Passed to the concrete detector constructor.
    :return: A concrete extractor instance.
    :raises ValueError: If method is not "llm".
    """
    if method == "llm":
        from clear_anonymization.extractors.llm import LLMExtractor

        return LLMExtractor(**kwargs)

    if method == "rulechef":
        from clear_anonymization.extractors.clear_rulechef import RuleChefExtractor

        return RuleChefExtractor(**kwargs)
    else:
        raise ValueError(f"Unknown detector method: {method}. Use llm")

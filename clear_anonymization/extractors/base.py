"""Abstract base class for NER extractors."""

from __future__ import annotations

from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def predict(self, text) -> dict:
        pass

    def predict_batch(self, text: list[str]) -> list[dict]:
        pass

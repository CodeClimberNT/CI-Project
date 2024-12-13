"""Symbolic regression package for genetic programming."""

from .base import INode, NodeType, get_nodes
from .config.settings import GeneticParams
from .core.genetic_programming import GeneticProgram
from .core.tree import Node
from .operators.definitions import BINARY_OPS, UNARY_OPS
from .utils.data_handler import load_data, split_data
from .utils.logging_config import setup_logger
from .utils.metrics import Metrics
from .utils.plotting import (
    plot_evolution_metrics,
    plot_expression_behavior,
    plot_operator_distribution,
    plot_prediction_analysis,
    plot_variable_importance,
)

__all__ = [
    "INode",
    "NodeType",
    "get_nodes",
    "UNARY_OPS",
    "BINARY_OPS",
    "GeneticParams",
    "Metrics",
    "Node",
    "GeneticProgram",
    "load_data",
    "split_data",
    "plot_evolution_metrics",
    "plot_expression_behavior",
    "plot_operator_distribution",
    "plot_prediction_analysis",
    "plot_variable_importance",
    "setup_logger",
]

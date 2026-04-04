from __future__ import print_function
import pandas as pd
import numpy as np


def read_motif(motif_file):
    """Read motif data from a file path or DataFrame.

    Parameters
    ----------
        motif_file : str or pd.DataFrame or None
            Path to file containing the transcription factor DNA binding motif data
            in the form of TF-gene-weight(0/1) as a tab-separated file without a header,
            or a pandas DataFrame with columns 'source', 'target', 'weight' (or positional).
            If None, returns (None, [], []).

    Returns
    -------
        motif_data : pd.DataFrame or None
            Motif data as a DataFrame with positional columns [0, 1, 2].
        motif_tfs : list
            Sorted list of unique TFs.
        motif_genes : list
            Sorted list of unique genes.
    """
    if motif_file is None:
        return None, [], []

    if isinstance(motif_file, str):
        motif_data = pd.read_csv(motif_file, sep="\t", header=None)
        motif_tfs = sorted(set(motif_data[0]))
        motif_genes = sorted(set(motif_data[1]))
        return motif_data, motif_tfs, motif_genes

    if isinstance(motif_file, pd.DataFrame):
        if ("source" not in motif_file.columns) or (
            "target" not in motif_file.columns
        ):
            print('renaming motif columns to "source", "target" and "weight" ')
            motif_file.columns = ["source", "target", "weight"]
        motif_data = pd.DataFrame(motif_file.values)
        motif_tfs = sorted(set(motif_file["source"]))
        motif_genes = sorted(set(motif_file["target"]))
        return motif_data, motif_tfs, motif_genes

    raise Exception(
        "Please provide a pandas dataframe for motif data with column names as "
        "'source', 'target', and 'weight', or a file path string."
    )


def read_expression(expression_file, start=1, end=None, with_header=False):
    """Read expression data from a file path or DataFrame.

    Parameters
    ----------
        expression_file : str or pd.DataFrame or None
            Path to file containing the gene expression data or a pandas DataFrame.
            By default, the expression file does not have a header, and the cells
            are separated by a tab. Pass with_header=True if the expression data
            includes the sample names.
            If None, returns (None, [], None).
        start : int
            First sample (1-indexed). Default: 1.
        end : int or None
            Last sample (1-indexed, inclusive). Default: None (all samples).
        with_header : bool
            If True, reads the expression file with a header row.

    Returns
    -------
        expression_data : pd.DataFrame or None
            Expression data as a DataFrame (genes x samples).
        expression_genes : list
            List of gene names.
        expression_samples : pd.Index or None
            Sample names/indices.
    """
    if expression_file is None:
        return None, [], None

    if isinstance(expression_file, str):
        if with_header:
            expression_data = pd.read_csv(
                expression_file, sep="\t", index_col=0
            )
        else:
            expression_data = pd.read_csv(
                expression_file, sep="\t", header=None, index_col=0
            )
        expression_data = expression_data.iloc[:, (start - 1):end]
        expression_genes = expression_data.index.tolist()
        expression_samples = expression_data.columns.astype(str)
        return expression_data, expression_genes, expression_samples

    if isinstance(expression_file, pd.DataFrame):
        expression_data = expression_file.iloc[:, (start - 1):end]
        expression_genes = expression_data.index.tolist()
        expression_samples = expression_data.columns.astype(str)
        return expression_data, expression_genes, expression_samples

    raise Exception(
        "Please provide a pandas dataframe for expression data or a file path string."
    )


def read_ppi(ppi_file):
    """Read PPI data from a file path or DataFrame.

    Parameters
    ----------
        ppi_file : str or pd.DataFrame or None
            Path to file containing the PPI data or a pandas DataFrame.
            The PPI can be symmetrical; if not, it will be transformed into
            a symmetrical adjacency matrix.
            If None, returns (None, []).

    Returns
    -------
        ppi_data : pd.DataFrame or None
            PPI data as a DataFrame.
        ppi_tfs : list
            Sorted list of unique TFs in the PPI.
    """
    if ppi_file is None:
        return None, []

    if isinstance(ppi_file, str):
        ppi_data = pd.read_csv(ppi_file, sep="\t", header=None)
        ppi_tfs = sorted(set(pd.concat([ppi_data[0], ppi_data[1]])))
        return ppi_data, ppi_tfs

    if isinstance(ppi_file, pd.DataFrame):
        ppi_data = ppi_file
        ppi_tfs = sorted(set(pd.concat([ppi_data[0], ppi_data[1]])))
        return ppi_data, ppi_tfs

    raise Exception(
        "Please provide a pandas dataframe for PPI data or a file path string."
    )

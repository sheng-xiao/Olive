# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------

from olive.data.config import DataConfig


def dummy_data_config_template(input_shapes, input_types, input_names=None) -> DataConfig:
    """
    Convert the dummy data config to the data container.
    input_names: list
        The input names of the model.
    input_shapes: list
        The input shapes of the model.
    input_types: list
        The input types of the model.
    """
    return DataConfig(
        name="dummy_data_config_template",
        type="DummyDataContainer",
        params_config={
            "input_shapes": input_shapes,
            "input_types": input_types,
            "input_names": input_names,
        },
    )


def huggingface_data_config_template(model_name, task, **kwargs) -> DataConfig:
    """
    Convert the huggingface data config to the data container.
    model_name: str
        The model name of huggingface.
    task: str
        The task type of huggingface.
    **kwargs: dict
        The additional arguments.
        - `data_name`: str, data name in huggingface dataset, e.g.: "glue", "squad"
        - `subset`: str, subset of data, e.g.: "train", "validation", "test"
        - `split`: str, split of data, e.g.: "train", "validation", "test"
        - `input_cols`: list, input columns of data
        - `label_cols`: list, label columns of data
        - `batch_size`: int, batch size of data
        and other arguments in
            - olive.data.component.load_dataset.huggingface_dataset
            - olive.data.component.pre_process_data.huggingface_pre_process
    """
    return DataConfig(
        name="huggingface_data_config_template",
        type="HuggingfaceContainer",
        params_config={
            "model_name": model_name,
            "task": task,
            **kwargs,
        },
    )
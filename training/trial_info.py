import dataclasses
from dataclasses import dataclass
from pathlib import Path
from uuid import UUID, uuid1

import pandas as pd

from config.structure import get_project_structure
from models.efficient_net.efficient_nets import EfficientNets
from utils.folders import create_date_folder, mkdir_if_not_exists


@dataclass
class TrialInfo:
    model_info: EfficientNets
    load_weights: bool
    advprop: bool

    # auto-generated
    output_folder: Path = None
    trial_id: UUID = uuid1()

    def __post_init__(self):
        date_folder = create_date_folder(get_project_structure()['training_trials'])

        self.output_folder = date_folder / str(self.trial_id)
        mkdir_if_not_exists(self.output_folder)

    def drop_trial_info(self, path=None):
        if not path:
            path = get_project_structure()['training_trials'] / 'trials_info.csv'

        dictionary = dataclasses.asdict(self)
        dictionary['index'] = [0]
        df = pd.DataFrame.from_records(dictionary, index='index')
        if path.exists():
            df.to_csv(path, mode='a', header=False)
        else:
            df.to_csv(path, header=True)
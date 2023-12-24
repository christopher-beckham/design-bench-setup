from design_bench.datasets.discrete.gfp_dataset import GFPDataset
from design_bench.datasets.discrete.tf_bind_8_dataset import TFBind8Dataset
from design_bench.datasets.discrete.tf_bind_10_dataset import TFBind10Dataset
from design_bench.datasets.discrete.cifar_nas_dataset import CIFARNASDataset 
from design_bench.datasets.discrete.nas_bench_dataset import NASBenchDataset
from design_bench.datasets.discrete.utr_dataset import UTRDataset
from design_bench.datasets.discrete.chembl_dataset import ChEMBLDataset
from design_bench.datasets.continuous.toy_continuous_dataset import ToyContinuousDataset
from design_bench.datasets.continuous.hopper_controller_dataset import HopperControllerDataset
from design_bench.datasets.continuous.superconductor_dataset import SuperconductorDataset
from design_bench.datasets.continuous.ant_morphology_dataset import AntMorphologyDataset
from design_bench.datasets.continuous.dkitty_morphology_dataset import DKittyMorphologyDataset


"""
register('TFBind8-Exact-v0',
         'design_bench.datasets.discrete.tf_bind_8_dataset:TFBind8Dataset',
         'design_bench.oracles.exact:TFBind8Oracle',

         # keyword arguments for building the dataset
         dataset_kwargs=dict(
             max_samples=None,
             distribution=None,
             max_percentile=50,
             min_percentile=0),

         # keyword arguments for building the exact oracle
         oracle_kwargs=dict(
             noise_std=0.0))

"""

if __name__ == '__main__':

    #TFBind8Dataset()
    #TFBind10Dataset()
    #CIFARNASDataset()
    #NASBenchDataset()
    #UTRDataset()
    #ChEMBLDataset()
    #ToyContinuousDataset()
    #HopperControllerDataset()
    #SuperconductorDataset()
    #AntMorphologyDataset()
    #DKittyMorphologyDataset() 

    ds = TFBind8Dataset()
    print(ds.x, ds.y)



    pass

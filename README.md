# DeepCPI

## Usage

### 1) Install

```bash
conda create -n deep-cpi python=3.9
conda activate deep-cpi
# Install [PyTorch](https://pytorch.org/get-started/locally/)

git clone https://github.com/vivym/deep-cpi.git
cd deep-cpi
pip install -e .
```

### 2) Training

```bash
python tools/train.py fit configs/gru_cpi_v1.yaml
python tools/train.py fit configs/gru_cpi_v2.yaml
python tools/train.py fit configs/gru_cpi_v3.yaml
python tools/train.py fit configs/gru_cpi_v4.yaml
python tools/train.py fit configs/lstm_cpi_v1.yaml
```

### 3) Tensorboard

```bash
tensorboard --logdir ./wandb
```

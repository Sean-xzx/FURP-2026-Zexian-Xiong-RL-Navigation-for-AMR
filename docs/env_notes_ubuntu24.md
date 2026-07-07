# Ubuntu 24.04 Environment Notes

## System

- OS: Ubuntu 24.04.4 LTS
- GPU: NVIDIA GeForce RTX 3060
- VRAM: 12GB
- NVIDIA driver: 595.71.05
- CUDA shown by nvidia-smi: 13.2

## Conda Environment

- Environment name: irsim_rl
- Python version: 3.10

## Verified

- Git clone / commit / push works
- `src/eval/metrics.py` works
- `src/eval/evaluate_csv.py` works
- `nvidia-smi` detects RTX3060
- PyTorch GPU version installed
- `torch.cuda.is_available()` returns True
- CUDA tensor operation test passed

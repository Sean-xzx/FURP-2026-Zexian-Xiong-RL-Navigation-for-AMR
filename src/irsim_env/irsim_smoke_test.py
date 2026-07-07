import sys

import irsim
import torch


def main():
    print("=== IR-SIM Smoke Test ===")

    print("Python:", sys.version.split()[0])
    print("IR-SIM version:", getattr(irsim, "__version__", "unknown"))
    print("IR-SIM module:", irsim.__file__)

    print("\n=== IR-SIM API Check ===")
    print("has irsim.make:", hasattr(irsim, "make"))
    print("has irsim.EnvBase:", hasattr(irsim, "EnvBase"))
    print("has irsim.EnvBase3D:", hasattr(irsim, "EnvBase3D"))

    print("\n=== PyTorch CUDA Check ===")
    print("torch version:", torch.__version__)
    print("cuda available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("gpu:", torch.cuda.get_device_name(0))
        x = torch.randn(256, 256).cuda()
        y = x @ x
        print("cuda tensor device:", y.device)
        print("cuda tensor test: OK")
    else:
        print("cuda tensor test: SKIPPED")

    print("\nSmoke test finished.")


if __name__ == "__main__":
    main()

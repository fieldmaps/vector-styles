import subprocess
from pathlib import Path

cwd = Path(__file__).parent


def upload(src, dest):
    subprocess.run(
        [
            "rclone",
            "sync",
            "--progress",
            "--exclude=.*",
            "--s3-no-check-bucket",
            "--s3-chunk-size=256M",
            src,
            dest,
        ]
    )


if __name__ == "__main__":
    # upload(cwd / "dist/fonts", "r2://fieldmaps-data/fonts")
    upload(cwd / "dist/styles", "r2://fieldmaps-data/styles")
    upload(
        cwd / "dist/styles/light",
        "r2://fieldmaps-data/esri/VectorTileServer/resources/styles",
    )

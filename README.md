# Transmission Builds

This repository contains build scripts for compiling the Transmission BitTorrent client and creating Debian packages (.deb). CI packages are produced when the GitHub Actions workflow is run manually.

## GitHub Actions

Workflow `.github/workflows/build.yaml` runs **only** on **`workflow_dispatch`**. Pushes to `main` do **not** trigger builds — use **Actions** → run workflow → choose **`all`** or a specific version.

## Features

- Builds via GitHub Actions (manual trigger)
- Debian packages that install Transmission in `/opt/Krate/vendor/transmission-daemon_${VERSION}`
- CI uses a **single reference image** (`matrix.py`); **one `.deb` per Transmission version** combination, for recent **Debian and Ubuntu** on **amd64**
- Upstream versions: **4.0.6**, **4.1.0**, **4.1.1**, **4.1.3**
- Static compilation for server usage
- Web interface support
- JSON-RPC API support
- Automated metadata generation
- Package signing and verification

## Build Process

When you start the workflow, the job sequence includes:
1. Environment setup with all required dependencies
2. Download and compilation of Transmission
3. Static linking of all components
4. Creation of Debian packages
5. Generation of JSON metadata
6. Package signing and verification
7. Create or update the GitHub Release (when the workflow completes successfully)

## Available Packages

Packages are available in the GitHub Releases of this repository. Each release includes:
- A `.deb` file installable with `dpkg -i`
- A `.json` file containing package metadata
- Documentation and changelog
- Package signatures

### Package Structure

The Debian package installs Transmission in a dedicated directory structure:
- Base installation path: `/opt/Krate/vendor/transmission-daemon_${VERSION}`
- Binaries in `/opt/Krate/vendor/transmission-daemon_${VERSION}/usr/bin`
- Libraries in `/opt/Krate/vendor/transmission-daemon_${VERSION}/usr/lib`
- Web interface in `/opt/Krate/vendor/transmission-daemon_${VERSION}/usr/share/transmission/web`
- Documentation in `/opt/Krate/vendor/transmission-daemon_${VERSION}/usr/share/doc/transmission`
- Systemd service file in `/opt/Krate/vendor/transmission-daemon_${VERSION}/usr/lib/systemd/system`

The package uses Debian alternatives to manage the binaries, making them available in the system PATH.

## Installation

### Manual Installation
1. Download the `.deb` for the Transmission version you need
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

### Automated Installation
The packages can be installed automatically using the JSON metadata and package management tools.

### Build Configuration
The build process is configured through:
- `build.yaml`: GitHub Actions workflow configuration
- `matrix.py`: Build matrix configuration for upstream versions (single reference OS in CI)

## License

This repository is licensed under the terms specified in the LICENSE file.

Transmission is distributed under the terms of the [GNU General Public License v2](https://www.gnu.org/licenses/gpl-2.0.html) or later.

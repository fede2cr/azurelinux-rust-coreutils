# azurelinux-rust-coreutils
Rpm package of rust coreutils for azurelinux

## Description

Ubuntu 25.10 will try to release with the version of Coreutils that has been built in rust, meaning higher security and way better perfomance for many of the commands. The reason behind this repo, is to test rust-coreutils in AzureLinux 3, and if it works properly to suggest it for AzureLinux 4. Specially if used in conjunction with the "oxidizr" tool, made to replace the GNU Coreutils for the Rust Coreutils.

*Note*: This is a proposal for AzureLinux 4, which is why we are downloading a newer version of Rust, as part of the installation process that follows. This is only required for compiling the RPM, and no
t for running the rust-coreutils.

## Instructions

RPMs are being built and release using GitHub actions, so you only need to download the package and install it.

Start with a brand new AzureLinux 3 VM. Then, inside of it, run:

```
sudo tdnf -y update
sudo tdnf -y install cargo lsb-release
sudo tdnf -y install https://github.com/fede2cr/azurelinux-rust-coreutils/releases/download/v0.1.0-2/rust-coreutils-0.1.0-1.azl3.$(uname -m).rpm
cargo install --git https://github.com/fede2cr/oxidizr --branch azurelinux
sudo .cargo/bin/oxidizr enable -e coreutils
ls -l $(which ls)
ls --version
```

Great. Now do your benchmarks and stress testing here.

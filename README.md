# azurelinux-rust-coreutils
Rpm package of rust coreutils for azurelinux

## Description

Ubuntu 25.10 will try to release with the version of Coreutils that has been built in rust, meaning higher security and way better perfomance for many of the commands. The reason behind this repo, is to test rust-coreutils in AzureLinux 3, and if it works properly to suggest it for AzureLinux 4. Specially if used in conjunction with the "oxidizr" tool, made to replace the GNU Coreutils for the Rust Coreutils.

*Note*: This is a proposal for AzureLinux 4, which is why we are downloading a newer version of Rust, as part of the installation process that follows. This is only required for compiling the RPM, and no
t for running the rust-coreutils.

## Instructions

Start with a brand new AzureLinux 3 VM.

Then, inside of it, run:

```
sudo tdnf update -y
sudo tdnf install -y lsb-release git rpmdevtools cargo gcc rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo.env"
rpmdev-setuptree
git clone https://github.com/fede2cr/azurelinux-rust-coreutils.git
cd azurelinux-rust-coreutils/rust-coreutils
spectool -g rust-coreutils.spec
rpmbuild -ba rust-coreutils.spec
sudo tdnf install -y $HOME/rpmbuild/RPMS/$(uname -m)/rust-coreutils-0*rpm
cd
git clone https://github.com/fede2cr/oxidizr
cd oxidizr
git checkout azurelinux
cargo build
sudo target/debug/oxidizr enable -e coreutils -v
ls -l $(which ls)
```

Great. Now do your benchmarks and stress testing here.

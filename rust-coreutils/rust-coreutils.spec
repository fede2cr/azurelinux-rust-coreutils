#
# spec file for package rust-coreutils
#

Name:           rust-coreutils
Version:        0.0.30
Release:        1%{?dist}
Summary:        Core utilities rewritten in Rust

License:        MIT OR Apache-2.0
Source0:            https://github.com/uutils/coreutils/archive/refs/tags/%{version}.tar.gz
#URL:            https://github.com/uutils/coreutils/archive/refs/tags/%{version}.tar.gz
#Source0:        %{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc

%description
Rust-coreutils is a reimplementation of the GNU core utilities in Rust.

%prep
%setup -q

%build
cargo build --release

%install
install -Dm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Tue Oct 10 2023 Your Name <your.email@example.com> - 1.0.0-1
- Initial package
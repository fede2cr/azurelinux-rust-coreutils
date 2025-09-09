#
# spec file for package rust-coreutils
#

Name:           rust-coreutils
Version:        %{version}
Release:        1%{?dist}
Summary:        Core utilities rewritten in Rust

License:        MIT OR Apache-2.0
Source0:        https://github.com/uutils/coreutils/archive/refs/tags/%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc

%description
Rust-coreutils is a reimplementation of the GNU core utilities in Rust.

%prep
%setup -n coreutils-%{version} 

%build
cargo build --release --features unix

%install
install -Dm0755 target/release/coreutils %{buildroot}%{_bindir}/coreutils

mkdir -v -p %{buildroot}%{_libdir}/cargo/bin/coreutils
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/[
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/arch
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/b2sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/base32
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/base64
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/basename
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/cat
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/chcon
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/chgrp
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/chmod
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/chown
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/chroot
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/cksum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/comm
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/cp
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/csplit
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/cut
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/date
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/dd
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/df
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/dir
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/dircolors
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/dirname
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/du
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/echo
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/env
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/expand
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/expr
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/factor
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/false
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/fmt
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/fold
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/groups
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/hashsum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/head
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/hostid
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/id
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/install
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/join
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/link
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/ln
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/logname
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/ls
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/md5sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/mkdir
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/mkfifo
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/mknod
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/mktemp
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/mv
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/nice
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/nl
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/nohup
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/nproc
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/numfmt
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/od
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/paste
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/pathchk
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/pinky
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/pr
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/printenv
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/printf
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/ptx
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/pwd
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/readlink
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/realpath
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/relpath
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/rm
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/rmdir
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/runcon
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/seq
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha1sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha224sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha256sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha3-224sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha3-256sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha3-384sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha3-512sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha384sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha3sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sha512sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/shake128sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/shake256sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/shred
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/shuf
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sleep
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sort
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/split
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/stat
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/stdbuf
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sum
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/sync
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tac
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tail
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tee
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/test
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/timeout
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/touch
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tr
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/true
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/truncate
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tsort
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/tty
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/uname
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/unexpand
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/uniq
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/unlink
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/users
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/vdir
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/wc
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/who
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/whoami
ln -v -sf ../../../../bin/coreutils %{buildroot}%{_libdir}/cargo/bin/coreutils/yes

%files
%{_bindir}/coreutils
%{_libdir}/cargo/bin/coreutils/[
%{_libdir}/cargo/bin/coreutils/arch
%{_libdir}/cargo/bin/coreutils/b2sum
%{_libdir}/cargo/bin/coreutils/base32
%{_libdir}/cargo/bin/coreutils/base64
%{_libdir}/cargo/bin/coreutils/basename
%{_libdir}/cargo/bin/coreutils/cat
%{_libdir}/cargo/bin/coreutils/chcon
%{_libdir}/cargo/bin/coreutils/chgrp
%{_libdir}/cargo/bin/coreutils/chmod
%{_libdir}/cargo/bin/coreutils/chown
%{_libdir}/cargo/bin/coreutils/chroot
%{_libdir}/cargo/bin/coreutils/cksum
%{_libdir}/cargo/bin/coreutils/comm
%{_libdir}/cargo/bin/coreutils/cp
%{_libdir}/cargo/bin/coreutils/csplit
%{_libdir}/cargo/bin/coreutils/cut
%{_libdir}/cargo/bin/coreutils/date
%{_libdir}/cargo/bin/coreutils/dd
%{_libdir}/cargo/bin/coreutils/df
%{_libdir}/cargo/bin/coreutils/dir
%{_libdir}/cargo/bin/coreutils/dircolors
%{_libdir}/cargo/bin/coreutils/dirname
%{_libdir}/cargo/bin/coreutils/du
%{_libdir}/cargo/bin/coreutils/echo
%{_libdir}/cargo/bin/coreutils/env
%{_libdir}/cargo/bin/coreutils/expand
%{_libdir}/cargo/bin/coreutils/expr
%{_libdir}/cargo/bin/coreutils/factor
%{_libdir}/cargo/bin/coreutils/false
%{_libdir}/cargo/bin/coreutils/fmt
%{_libdir}/cargo/bin/coreutils/fold
%{_libdir}/cargo/bin/coreutils/groups
%{_libdir}/cargo/bin/coreutils/hashsum
%{_libdir}/cargo/bin/coreutils/head
%{_libdir}/cargo/bin/coreutils/hostid
%{_libdir}/cargo/bin/coreutils/id
%{_libdir}/cargo/bin/coreutils/install
%{_libdir}/cargo/bin/coreutils/join
%{_libdir}/cargo/bin/coreutils/link
%{_libdir}/cargo/bin/coreutils/ln
%{_libdir}/cargo/bin/coreutils/logname
%{_libdir}/cargo/bin/coreutils/ls
%{_libdir}/cargo/bin/coreutils/md5sum
%{_libdir}/cargo/bin/coreutils/mkdir
%{_libdir}/cargo/bin/coreutils/mkfifo
%{_libdir}/cargo/bin/coreutils/mknod
%{_libdir}/cargo/bin/coreutils/mktemp
%{_libdir}/cargo/bin/coreutils/mv
%{_libdir}/cargo/bin/coreutils/nice
%{_libdir}/cargo/bin/coreutils/nl
%{_libdir}/cargo/bin/coreutils/nohup
%{_libdir}/cargo/bin/coreutils/nproc
%{_libdir}/cargo/bin/coreutils/numfmt
%{_libdir}/cargo/bin/coreutils/od
%{_libdir}/cargo/bin/coreutils/paste
%{_libdir}/cargo/bin/coreutils/pathchk
%{_libdir}/cargo/bin/coreutils/pinky
%{_libdir}/cargo/bin/coreutils/pr
%{_libdir}/cargo/bin/coreutils/printenv
%{_libdir}/cargo/bin/coreutils/printf
%{_libdir}/cargo/bin/coreutils/ptx
%{_libdir}/cargo/bin/coreutils/pwd
%{_libdir}/cargo/bin/coreutils/readlink
%{_libdir}/cargo/bin/coreutils/realpath
%{_libdir}/cargo/bin/coreutils/relpath
%{_libdir}/cargo/bin/coreutils/rm
%{_libdir}/cargo/bin/coreutils/rmdir
%{_libdir}/cargo/bin/coreutils/runcon
%{_libdir}/cargo/bin/coreutils/seq
%{_libdir}/cargo/bin/coreutils/sha1sum
%{_libdir}/cargo/bin/coreutils/sha224sum
%{_libdir}/cargo/bin/coreutils/sha256sum
%{_libdir}/cargo/bin/coreutils/sha3-224sum
%{_libdir}/cargo/bin/coreutils/sha3-256sum
%{_libdir}/cargo/bin/coreutils/sha3-384sum
%{_libdir}/cargo/bin/coreutils/sha3-512sum
%{_libdir}/cargo/bin/coreutils/sha384sum
%{_libdir}/cargo/bin/coreutils/sha3sum
%{_libdir}/cargo/bin/coreutils/sha512sum
%{_libdir}/cargo/bin/coreutils/shake128sum
%{_libdir}/cargo/bin/coreutils/shake256sum
%{_libdir}/cargo/bin/coreutils/shred
%{_libdir}/cargo/bin/coreutils/shuf
%{_libdir}/cargo/bin/coreutils/sleep
%{_libdir}/cargo/bin/coreutils/sort
%{_libdir}/cargo/bin/coreutils/split
%{_libdir}/cargo/bin/coreutils/stat
%{_libdir}/cargo/bin/coreutils/stdbuf
%{_libdir}/cargo/bin/coreutils/sum
%{_libdir}/cargo/bin/coreutils/sync
%{_libdir}/cargo/bin/coreutils/tac
%{_libdir}/cargo/bin/coreutils/tail
%{_libdir}/cargo/bin/coreutils/tee
%{_libdir}/cargo/bin/coreutils/test
%{_libdir}/cargo/bin/coreutils/timeout
%{_libdir}/cargo/bin/coreutils/touch
%{_libdir}/cargo/bin/coreutils/tr
%{_libdir}/cargo/bin/coreutils/true
%{_libdir}/cargo/bin/coreutils/truncate
%{_libdir}/cargo/bin/coreutils/tsort
%{_libdir}/cargo/bin/coreutils/tty
%{_libdir}/cargo/bin/coreutils/uname
%{_libdir}/cargo/bin/coreutils/unexpand
%{_libdir}/cargo/bin/coreutils/uniq
%{_libdir}/cargo/bin/coreutils/unlink
%{_libdir}/cargo/bin/coreutils/users
%{_libdir}/cargo/bin/coreutils/vdir
%{_libdir}/cargo/bin/coreutils/wc
%{_libdir}/cargo/bin/coreutils/who
%{_libdir}/cargo/bin/coreutils/whoami
%{_libdir}/cargo/bin/coreutils/yes
%license LICENSE
%doc README.md

%changelog
* Wed Apr  9 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.30.0-1
- Initial package
* Wed May 16 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.1.0-1
- Upgrade to 0.1.0 from upstream
* Tue Sep  9 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.1.0-3
- Dynamic version in rpm

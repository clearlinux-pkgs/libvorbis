#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9259A8F2D2D44C84 (giles@thaumas.net)
#
Name     : libvorbis
Version  : 1.3.7
Release  : 27
URL      : http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.xz
Source0  : http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.xz
Source1  : http://downloads.xiph.org/releases/vorbis/libvorbis-1.3.7.tar.xz.asc
Summary  : Vorbis Library Development
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libvorbis-lib = %{version}-%{release}
Requires: libvorbis-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32ogg)
BuildRequires : pkgconfig(ogg)

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed 
and variable bitrates from 16 to 128 kbps/channel.

%package dev
Summary: dev components for the libvorbis package.
Group: Development
Requires: libvorbis-lib = %{version}-%{release}
Provides: libvorbis-devel = %{version}-%{release}
Requires: libvorbis = %{version}-%{release}

%description dev
dev components for the libvorbis package.


%package dev32
Summary: dev32 components for the libvorbis package.
Group: Default
Requires: libvorbis-lib32 = %{version}-%{release}
Requires: libvorbis-dev = %{version}-%{release}

%description dev32
dev32 components for the libvorbis package.


%package doc
Summary: doc components for the libvorbis package.
Group: Documentation

%description doc
doc components for the libvorbis package.


%package lib
Summary: lib components for the libvorbis package.
Group: Libraries
Requires: libvorbis-license = %{version}-%{release}

%description lib
lib components for the libvorbis package.


%package lib32
Summary: lib32 components for the libvorbis package.
Group: Default
Requires: libvorbis-license = %{version}-%{release}

%description lib32
lib32 components for the libvorbis package.


%package license
Summary: license components for the libvorbis package.
Group: Default

%description license
license components for the libvorbis package.


%prep
%setup -q -n libvorbis-1.3.7
cd %{_builddir}/libvorbis-1.3.7
pushd ..
cp -a libvorbis-1.3.7 build32
popd
pushd ..
cp -a libvorbis-1.3.7 buildavx2
popd
pushd ..
cp -a libvorbis-1.3.7 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656134087
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffast-math -ffat-lto-objects -flto=auto -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffast-math -ffat-lto-objects -flto=auto -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffast-math -ffat-lto-objects -flto=auto -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffast-math -ffat-lto-objects -flto=auto -fstack-protector-strong -ftree-loop-vectorize -fzero-call-used-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export SOURCE_DATE_EPOCH=1656134087
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvorbis
cp %{_builddir}/libvorbis-1.3.7/COPYING %{buildroot}/usr/share/package-licenses/libvorbis/884d21ba4c65504f86801ecefe2d75f6195ef683
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/vorbis/codec.h
/usr/include/vorbis/vorbisenc.h
/usr/include/vorbis/vorbisfile.h
/usr/lib64/libvorbis.so
/usr/lib64/libvorbisenc.so
/usr/lib64/libvorbisfile.so
/usr/lib64/pkgconfig/vorbis.pc
/usr/lib64/pkgconfig/vorbisenc.pc
/usr/lib64/pkgconfig/vorbisfile.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvorbis.so
/usr/lib32/libvorbisenc.so
/usr/lib32/libvorbisfile.so
/usr/lib32/pkgconfig/32vorbis.pc
/usr/lib32/pkgconfig/32vorbisenc.pc
/usr/lib32/pkgconfig/32vorbisfile.pc
/usr/lib32/pkgconfig/vorbis.pc
/usr/lib32/pkgconfig/vorbisenc.pc
/usr/lib32/pkgconfig/vorbisfile.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libvorbis/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbis.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbis.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbis.so.0.4.9
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisenc.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisenc.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisenc.so.2.0.12
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisfile.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisfile.so.3
/usr/lib64/glibc-hwcaps/x86-64-v3/libvorbisfile.so.3.3.8
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbis.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbis.so.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbis.so.0.4.9
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisenc.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisenc.so.2
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisenc.so.2.0.12
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisfile.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisfile.so.3
/usr/lib64/glibc-hwcaps/x86-64-v4/libvorbisfile.so.3.3.8
/usr/lib64/libvorbis.so.0
/usr/lib64/libvorbis.so.0.4.9
/usr/lib64/libvorbisenc.so.2
/usr/lib64/libvorbisenc.so.2.0.12
/usr/lib64/libvorbisfile.so.3
/usr/lib64/libvorbisfile.so.3.3.8

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvorbis.so.0
/usr/lib32/libvorbis.so.0.4.9
/usr/lib32/libvorbisenc.so.2
/usr/lib32/libvorbisenc.so.2.0.12
/usr/lib32/libvorbisfile.so.3
/usr/lib32/libvorbisfile.so.3.3.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvorbis/884d21ba4c65504f86801ecefe2d75f6195ef683

%define _unpackaged_files_terminate_build 1

Name: libkaldi-vosk
Version: 5.5
Release: alt1.a25f216
Requires: libfst
Requires: liblapack
Requires: libopenblas
Requires: libxblas

Summary: Fork of kaldi used with vosk-api
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/alphacep/kaldi/tree/vosk

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: python3
BuildRequires: libfst-devel
BuildRequires: libopenblas-devel
BuildRequires: libblas-devel
BuildRequires: liblapack-devel
BuildRequires: libclapack-devel
BuildRequires: gcc-c++

Source0: %{name}-%{version}.tar

%description
Kaldi is a toolkit for speech recognition, intended for use by speech
recognition researchers and professionals. Fork of http://kaldi-asr.org.

%package -n %name-devel
Summary: Header files for Kaldi speech recognition toolkit
Group: System/Libraries
Requires: %name libfst-devel liblapack-devel libopenblas-devel

%description -n %name-devel
Header files for Kaldi - toolkit for speech recognition, intended
for use by speech recognition researchers and professionals. Fork
of http://kaldi-asr.org.

%prep
%setup -q

%build
%cmake \
    -DKALDI_BUILD_EXE=OFF \
    -DKALDI_BUILD_TEST=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DKALDI_VERSION=%version \
    -DMATHLIB=OpenBLAS
%cmake_build

%install
%cmake_install

%files
%_libdir/libkaldi-matrix.so
%_libdir/libkaldi-base.so
%_libdir/libkaldi-chain.so
%_libdir/libkaldi-cudamatrix.so
%_libdir/libkaldi-decoder.so
%_libdir/libkaldi-feat.so
%_libdir/libkaldi-fstext.so
%_libdir/libkaldi-gmm.so
%_libdir/libkaldi-hmm.so
%_libdir/libkaldi-ivector.so
%_libdir/libkaldi-kws.so
%_libdir/libkaldi-lat.so
%_libdir/libkaldi-lm.so
%_libdir/libkaldi-nnet.so
%_libdir/libkaldi-nnet2.so
%_libdir/libkaldi-nnet3.so
%_libdir/libkaldi-online.so
%_libdir/libkaldi-online2.so
%_libdir/libkaldi-rnnlm.so
%_libdir/libkaldi-transform.so
%_libdir/libkaldi-tree.so
%_libdir/libkaldi-util.so

%files -n %name-devel
%_prefix/lib/cmake/kaldi/*.cmake
%_includedir/kaldi/*/*.h

%changelog
* Fri Jun 2 2023 Andrew Guschin <guschin@altlinux.org> 5.5-alt1.a25f216
- Initial build.

Name: piper
Version: 0.2.900
Release: 1%{?dist}
Summary:  GTK application to configure gaming mice

License: GPLv2
URL: https://github.com/libratbag/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: ratbagd

Requires: ratbagd%{?_isa}

%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*

%changelog

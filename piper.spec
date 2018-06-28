Name: piper
Version: 0.2.900
Release: 1%{?dist}
Summary: GTK application to configure gaming mice

License: GPLv2
URL: https://github.com/libratbag/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: libratbag-ratbagd
BuildRequires: pygobject3-devel
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: libratbag-ratbagd%{?_isa}

%{?python_provide:%python_provide python3-%{name}}

%description
Piper is a GTK+ application to configure gaming mice, using libratbag
via ratbagd.

%prep
%autosetup -p1
sed -i '/meson_install.sh/d' meson.build

%build
%meson
%meson_build

%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Jun 28 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.900-1
- Initial SPEC release.

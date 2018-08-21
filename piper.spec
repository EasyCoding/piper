Name: piper
Version: 0.2.901
Release: 1%{?dist}

License: GPLv2+ and LGPLv2+
URL: https://github.com/libratbag/%{name}
Summary: GTK application to configure gaming mice
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: libratbag-ratbagd >= 0.9.902
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: pygobject3-devel
BuildRequires: python3-devel
BuildRequires: gettext-devel
BuildRequires: meson

Requires: hicolor-icon-theme
Requires: libratbag-ratbagd
Requires: python3-evdev
Requires: gtk3

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
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

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
* Tue Aug 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.901-1
- Updated to version 0.2.901.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.900-3.20180214git5f6ed20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.900-2.20180214git5f6ed20
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.900-1.20180214git5f6ed20
- Initial SPEC release.

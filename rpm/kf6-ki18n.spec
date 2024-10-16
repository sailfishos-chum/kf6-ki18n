%global  kf_version 6.6.0

Name:		kf6-ki18n
Version: 6.6.0
Release:	0%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon for localization
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND ODbl-1.0
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:	kf6-extra-cmake-modules >= kf_version
BuildRequires:	gettext
BuildRequires:	kf6-rpm-macros
BuildRequires:	perl
BuildRequires:	python3-base
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	pkgconfig(iso-codes)


%description
KDE Frameworks 6 Tier 1 addon for localization.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	gettext
Requires:	python3-base
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6I18n.so.*
%{_kf6_libdir}/libKF6I18nLocaleData.so.*
%{_kf6_datadir}/qlogging-categories6/ki18n*
%{_kf6_qmldir}/org/kde/i18n/localeData/
%{_kf6_qtplugindir}/kf6/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n6/
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n6/
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n6/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n6/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n6/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n6/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n6/
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n6/
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n6/

%files devel
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nLocaleData.so
%{_kf6_libdir}/cmake/KF6I18n/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

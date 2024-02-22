%define url_ver	%(echo %{version}|cut -d. -f1)
%define _empty_manifest_terminate_build 0

# filter out plugins from provides
#global __provides_exclude_from %{_libdir}/%{name}/.*\\.so

Name:		geary
Version:	44.1
Release:	1
Summary:	A lightweight email program designed around conversations
License:	LGPLv2+
Group:		Networking/Mail
URL:		https://wiki.gnome.org/Apps/Geary
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		fix-libunwind-missing-symbol.patch
# Fix accessibility issues with initializer of constants
Patch1:   9bd4c829.patch

BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:	xml2po
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(enchant)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(folks)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:	pkgconfig(javascriptcoregtk-4.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsecret-1)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libunwind-llvm)
BuildRequires:	libstemmer-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	pkgconfig(webkit2gtk-4.0)
BuildRequires:	pkgconfig(webkit2gtk-web-extension-4.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:  libytnef-devel
BuildRequires:  typelib(GMime)
BuildRequires:	valadoc
Requires:	hicolor-icon-theme
Requires: 	gsettings-desktop-schemas

%description
Geary is a new email reader for GNOME designed to let you read your email
quickly and effortlessly. Its interface is based on conversations, so you
can easily read an entire discussion without having to click from message
to message.
Geary is still in early development and has limited features today, but
we're planning to add lightning-fast searching, multiple account support,
and much more. Eventually we'd like Geary to have an extensible plugin
architecture so that developers will be able to add all kinds of nifty
features in a modular way.

%prep
%autosetup -p1

%build
%meson -Dprofile=release -Dtnef=disabled -Dc_args=-I/usr/include/libstemmer
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README.md THANKS COPYING
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Geary.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Geary*
%{_datadir}/icons/hicolor/*/actions/*.*
%{_datadir}/metainfo/org.gnome.Geary.appdata.xml
%{_libdir}/%{name}/
#{_libdir}/libgeary-client.so
%{_datadir}/dbus-1/services/org.gnome.Geary.service
